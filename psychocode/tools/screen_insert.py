"""Insert a video into a moving, angled green screen with per-frame perspective tracking.
Usage: python3 tools/screen_insert.py BG.mp4 SCREEN.mp4 OUT_RAW_DIR
Writes corners.json and composited frames as a raw stream to stdout-encoded mp4 (via ffmpeg)."""
import sys, json, subprocess, numpy as np
from PIL import Image
from scipy import ndimage

bg, scr, out = sys.argv[1], sys.argv[2], sys.argv[3]
def probe(f, k):
    return subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries",f"stream={k}","-of","csv=p=0",f]).decode().split()[0]
W, H = int(probe(bg,"width")), int(probe(bg,"height"))
fps = 24
dur_a = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",bg]).decode())
dur_b = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",scr]).decode())
N = int(round(dur_a * fps))

def frames(path, w, h, vf):
    p = subprocess.Popen(["ffmpeg","-loglevel","error","-i",path,"-vf",vf,"-f","rawvideo","-pix_fmt","rgb24","-"], stdout=subprocess.PIPE)
    while True:
        buf = p.stdout.read(w*h*3)
        if len(buf) < w*h*3: break
        yield np.frombuffer(buf, np.uint8).reshape(h, w, 3)

def greenness(f):
    f = f.astype(np.int16); return f[...,1] - np.maximum(f[...,0], f[...,2])

def fit_quad(mask):
    ys, xs = np.where(mask); x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    w, h = x1-x0, y1-y0
    def line_h(rows):  # y = a x + b
        p = np.array(rows, float); return np.polyfit(p[:,0], p[:,1], 1)
    def line_v(cols):  # x = a y + b
        p = np.array(cols, float); return np.polyfit(p[:,1], p[:,0], 1)
    top, bot, lef, rig = [], [], [], []
    for x in range(x0+int(.25*w), x0+int(.75*w)):
        c = np.where(mask[:,x])[0]
        if len(c): top.append((x, c.min())); bot.append((x, c.max()))
    for y in range(y0+int(.2*h), y0+int(.8*h)):
        c = np.where(mask[y])[0]
        if len(c): lef.append((c.min(), y)); rig.append((c.max(), y))
    t, b, l, r = line_h(top), line_h(bot), line_v(lef), line_v(rig)
    def inter(hl, vl):
        y = (hl[0]*vl[1] + hl[1]) / (1 - hl[0]*vl[0]); return [vl[0]*y + vl[1], y]
    return [inter(t,l), inter(t,r), inter(b,r), inter(b,l)]  # TL TR BR BL

# pass 1: corners per frame
corners = []
for f in frames(bg, W, H, f"fps={fps}"):
    g = greenness(f); m = ndimage.binary_closing(g > 60, iterations=3)
    lab, n = ndimage.label(m); sizes = ndimage.sum(m, lab, range(1, n+1))
    m = ndimage.binary_fill_holes(lab == (np.argmax(sizes)+1))
    corners.append(fit_quad(m))
C = np.array(corners)  # N x 4 x 2
# temporal smoothing (centered moving average, 9 frames)
k = 9; pad = np.pad(C, ((k//2, k//2), (0,0), (0,0)), mode="edge")
Cs = np.stack([pad[i:i+len(C)].mean(0) for i in range(k)]).mean(0) if False else np.array([pad[i:i+k].mean(0) for i in range(len(C))])
json.dump({"raw": C.tolist(), "smooth": Cs.tolist()}, open(out + "/corners.json", "w"))

def coeffs(dst, src):  # maps output (dst quad) -> input (src rect) for PIL PERSPECTIVE
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u*x, -u*y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v*x, -v*y]); B.append(v)
    return np.linalg.solve(np.array(A, float), np.array(B, float))

# pass 2: composite
SW, SH = 880, 1920
speed = dur_b / dur_a
enc = subprocess.Popen(["ffmpeg","-loglevel","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(fps),"-i","-",
                        "-c:v","libx264","-crf","14","-preset","medium","-pix_fmt","yuv420p", out + "/video_only.mp4"], stdin=subprocess.PIPE)
sgen = frames(scr, SW, SH, f"setpts=PTS/{speed},fps={fps},scale={SW}:{SH}")
last = None
for i, f in enumerate(frames(bg, W, H, f"fps={fps}")):
    try: s = next(sgen); last = s
    except StopIteration: s = last
    q = Cs[min(i, len(Cs)-1)]
    c = q.mean(0); q = c + (q - c) * 1.03  # expand 3% so content reaches the rounded edges
    co = coeffs(q.tolist(), [[0,0],[SW,0],[SW,SH],[0,SH]])
    warped = np.asarray(Image.fromarray(s).transform((W, H), Image.PERSPECTIVE, tuple(co), Image.BICUBIC)).astype(np.float32)
    g = greenness(f).astype(np.float32)
    a = np.clip((g - 25) / 55, 0, 1)
    big = ndimage.binary_dilation(ndimage.binary_closing(g > 60, iterations=3), iterations=6)
    lab, n = ndimage.label(big); sizes = ndimage.sum(big, lab, range(1, n+1))
    a *= (lab == (np.argmax(sizes)+1))
    fg = f.astype(np.float32)
    spill = a > 0
    fg[...,1] = np.where(spill, np.minimum(fg[...,1], np.maximum(fg[...,0], fg[...,2]) + 8), fg[...,1])
    o = fg * (1 - a[...,None]) + warped * a[...,None]
    enc.stdin.write(o.clip(0,255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
print("frames", i+1, "speed", round(speed, 3))
