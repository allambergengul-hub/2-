"""Assemble the invitation video.

usage: python3 -I build.py <uploads_dir> <work_dir> <out.mp4>
"""
import json, os, re, subprocess, sys, wave
import numpy as np

U, WD, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(WD, exist_ok=True)
FPS = 24
SR = 48000


def run(args):
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-3000:])
    return r.stderr


def lufs(path):
    err = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=framelog=quiet", "-f", "null", "-"])
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", err)[-1])


def load(path):
    w = wave.open(path)
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    return x.reshape(-1, w.getnchannels()).mean(1)


# ---------------------------------------------------------------- clips
# src: file; a/b: cut points in the source (s); tempo: speed factor;
# st: pitch shift (semitones); pre/post: frozen-frame padding (s);
# w0/w1: first word start / last sound end in the source (s)
CLIPS = [
    dict(src="096ca9cf-grok_video_2026-11-26-15-13-19.mp4", a=0.0, b=6.0, tempo=1.0, st=0, intro=True),
    dict(src="650cb676-grok_video_2026-11-26-15-02-12.mp4", a=0.0, b=5.77, tempo=0.99, st=-0.71, pre=0.8, w0=0.08, w1=5.30),
    dict(src="1f242d58-grok_video_2026-11-26-15-03-43.mp4", a=0.15, b=9.845, tempo=0.811, st=0.51, w0=0.30, w1=9.35),
    dict(src="ce2e77e4-grok_video_2026-11-26-15-05-33.mp4", a=0.0, b=7.85, tempo=0.847, st=-0.95, w0=0.0, w1=7.45),
    dict(src="df869b52-grok_video_2026-11-26-15-11-53.mp4", a=0.12, b=12.04, tempo=0.874, st=1.15, post=2.5, w0=0.27, w1=11.30),
]
# transitions between consecutive clips: (type, duration)
TRANS = [("fadewhite", 0.8), ("circleopen", 0.5), ("hblur", 0.5), ("fade", 0.5)]
CARD_AT = 0.55  # seconds into the last clip ("Өтетін орны...")

# ---------------------------------------------------------------- video segments
for i, c in enumerate(CLIPS):
    vf = [f"trim=start={c['a']}:end={c['b']}", "setpts=PTS-STARTPTS"]
    if c["tempo"] != 1.0:
        vf.append(f"setpts=PTS/{c['tempo']}")
    vf.append(f"framerate=fps={FPS}" if c["tempo"] < 1.0 else f"fps={FPS}")  # blend frames when slowing
    if c.get("pre"):
        vf.append(f"tpad=start_duration={c['pre']}:start_mode=clone")
    if c.get("post"):
        vf.append(f"tpad=stop_duration={c['post']}:stop_mode=clone")
    vf.append("format=yuv420p")
    out = f"{WD}/v{i}.mp4"
    run(["ffmpeg", "-y", "-i", f"{U}/{c['src']}", "-map", "0:v:0", "-an", "-vf", ",".join(vf),
         "-c:v", "libx264", "-crf", "10", "-preset", "fast", out])
    n = int(subprocess.run(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
         "stream=nb_read_frames", "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip())
    c["len"] = n / FPS

# ---------------------------------------------------------------- speech audio, stage 1: cut + tempo + pitch
for i, c in enumerate(CLIPS):
    if c.get("intro"):
        continue
    af = [f"atrim=start={c['a']}:end={c['b']}", "asetpts=PTS-STARTPTS", "pan=mono|c0=0.5*c0+0.5*c1",
          "highpass=f=80"]
    p = 2 ** (c["st"] / 12)
    if c["tempo"] != 1.0 or c["st"]:
        af.append(f"rubberband=tempo={c['tempo']}:pitch={p:.5f}:formant=preserved:pitchq=quality:"
                  "transients=mixed:detector=soft")
    run(["ffmpeg", "-y", "-i", f"{U}/{c['src']}", "-vn", "-af", ",".join(af), "-ar", str(SR),
         "-c:a", "pcm_s16le", f"{WD}/s1_{i}.wav"])

# ---------------------------------------------------------------- tonal matching (long-term spectrum)
bands = 125 * 2 ** (np.arange(0, 19) / 3)  # 1/3-octave centres 125 Hz .. 8 kHz
ltas = {}
for i, c in enumerate(CLIPS):
    if c.get("intro"):
        continue
    x = load(f"{WD}/s1_{i}.wav")
    N, H = 4096, 1024
    acc = np.zeros(N // 2 + 1)
    win = np.hanning(N)
    for k in range(0, len(x) - N, H):
        fr = x[k:k + N]
        if np.sqrt(np.mean(fr ** 2)) < 0.03:
            continue
        acc += np.abs(np.fft.rfft(fr * win)) ** 2
    fq = np.fft.rfftfreq(N, 1 / SR)
    db = []
    for f0 in bands:
        m = (fq >= f0 / 2 ** (1 / 6)) & (fq < f0 * 2 ** (1 / 6))
        db.append(10 * np.log10(acc[m].mean() + 1e-12))
    db = np.array(db)
    ltas[i] = db - db.mean()
target = np.mean(list(ltas.values()), axis=0)
for i, db in ltas.items():
    corr = target - db
    corr = np.convolve(np.pad(corr, 1, mode="edge"), [0.25, 0.5, 0.25], "valid")  # smooth
    corr = np.clip(corr, -4, 4)
    corr[bands < 200] = np.clip(corr[bands < 200], -2, 2)  # don't chase rumble below the voice
    CLIPS[i]["eq"] = ";".join(f"entry({f:.0f},{g:.2f})" for f, g in zip(bands, corr))
    CLIPS[i]["eq_dbg"] = [round(float(g), 1) for g in corr]

# ---------------------------------------------------------------- stage 2: EQ + gentle compression, then loudness match
SPEECH_LUFS = -14.0
for i, c in enumerate(CLIPS):
    if c.get("intro"):
        continue
    af = [f"firequalizer=gain_entry='{c['eq']}':gain='cubic_interpolate(f)'",
          "acompressor=threshold=-22dB:ratio=2.5:attack=8:release=160:makeup=1",
          "equalizer=f=3000:t=q:w=1:g=2.5"]  # presence lift for intelligibility over music
    run(["ffmpeg", "-y", "-i", f"{WD}/s1_{i}.wav", "-af", ",".join(af), "-c:a", "pcm_s16le", f"{WD}/s2_{i}.wav"])
    g = SPEECH_LUFS - lufs(f"{WD}/s2_{i}.wav")
    pre = c.get("pre", 0)
    d2 = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                               f"{WD}/s2_{i}.wav"], capture_output=True, text=True).stdout)
    af = [f"volume={g:.2f}dB", "afade=t=in:d=0.03", f"afade=t=out:st={d2 - 0.04:.4f}:d=0.04",
          f"adelay={int(pre * 1000)}:all=1" if pre else "anull",
          f"apad=whole_dur={c['len']:.4f}", f"atrim=end={c['len']:.4f}", "aformat=channel_layouts=stereo"]
    run(["ffmpeg", "-y", "-i", f"{WD}/s2_{i}.wav", "-af", ",".join(af), "-ar", str(SR), "-c:a", "pcm_s16le",
         f"{WD}/s3_{i}.wav"])
    c["gain"] = round(g, 2)
    c["lufs_after"] = lufs(f"{WD}/s3_{i}.wav")

# ---------------------------------------------------------------- timeline
t = 0.0
for i, c in enumerate(CLIPS):
    c["start"] = t
    if i < len(TRANS):
        t += c["len"] - TRANS[i][1]
total = CLIPS[-1]["start"] + CLIPS[-1]["len"]

# speech intervals on the output timeline (for music ducking)
speech = []
for c in CLIPS:
    if c.get("intro"):
        continue
    off = c["start"] + c.get("pre", 0)
    s = off + max(c["w0"] - c["a"], 0) / c["tempo"]
    e = off + (c["w1"] - c["a"]) / c["tempo"]
    speech.append([s, e])
merged = [speech[0][:]]
for s, e in speech[1:]:
    if s - merged[-1][1] < 2.0:
        merged[-1][1] = e
    else:
        merged.append([s, e])

# ---------------------------------------------------------------- music bed with ducking automation
MUSIC_LUFS = -16.0   # music level when nobody speaks
DUCK_DB = -21.0      # extra attenuation under speech
mus_src = f"{WD}/music_src.wav"
run(["ffmpeg", "-y", "-i", f"{U}/13389632-VID_20261126_113300_647.mp4", "-vn", "-ar", str(SR), "-ac", "2",
     "-c:a", "pcm_s16le", mus_src])
# The song itself ends at ~43.7 s (rest of the clip is silent). If the video is longer, repeat one chorus
# cycle ("Тәй-тәй басқан құлыным…", period 6.666 s) with a short equal-power crossfade at a point where
# both copies line up (waveform correlation ~0.7), so the song keeps going in time.
SONG_END, LOOP_P, SPLICE = 43.7, 6.666354, 18.21
w = wave.open(mus_src)
m = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, 2).astype(np.float32)
m = m[:int(SONG_END * SR)]
while len(m) / SR < total + 0.5:
    i, p, xf = int(SPLICE * SR), int(LOOP_P * SR), int(0.06 * SR)
    ramp = np.sin(np.linspace(0, np.pi / 2, xf))[:, None]
    head, tail = m[:i], m[i - p:]
    mid = head[-xf:] * ramp[::-1] + tail[:xf] * ramp
    m = np.concatenate([head[:-xf], mid, tail[xf:]])
mus_raw = f"{WD}/music_raw.wav"
with wave.open(mus_raw, "w") as o:
    o.setnchannels(2); o.setsampwidth(2); o.setframerate(SR)
    o.writeframes(np.clip(m[:int((total + 0.5) * SR)], -32768, 32767).astype(np.int16).tobytes())
mg = MUSIC_LUFS - lufs(mus_raw)
att, rel = 0.35, 0.6
terms = []
for s, e in merged:
    s0 = s - 0.25 - att  # fully ducked 0.25 s before the first word
    e0 = e + 0.15        # start rising 0.15 s after the last sound
    terms.append(f"clip((t-{s0:.3f})/{att},0,1)*clip(({e0 + rel:.3f}-t)/{rel},0,1)")
duck = "+".join(terms)
lin = 10 ** (DUCK_DB / 20)
vol_expr = f"(1-({1 - lin:.4f})*min(1,{duck}))"
fade_out = 2.0
music_af = (f"volume={mg:.2f}dB,volume='{vol_expr}':eval=frame,"
            f"atrim=end={total:.3f},afade=t=out:st={total - fade_out:.3f}:d={fade_out}")

# ---------------------------------------------------------------- final render
inputs = []
for i in range(len(CLIPS)):
    inputs += ["-i", f"{WD}/v{i}.mp4"]
inputs += ["-loop", "1", "-framerate", str(FPS), "-i", f"{WD}/card.png"]  # idx n
n = len(CLIPS)
for i, c in enumerate(CLIPS):
    if not c.get("intro"):
        inputs += ["-i", f"{WD}/s3_{i}.wav"]
inputs += ["-i", f"{U}/096ca9cf-grok_video_2026-11-26-15-13-19.mp4"]  # intro sound effect
inputs += ["-i", mus_raw]

fc = []
# video: chain xfades
prev = "[0:v]"
for i in range(1, n):
    typ, dur = TRANS[i - 1]
    off = CLIPS[i]["start"]
    lbl = f"[x{i}]"
    fc.append(f"{prev}[{i}:v]xfade=transition={typ}:duration={dur}:offset={off:.4f}{lbl}")
    prev = lbl
card_t = CLIPS[-1]["start"] + CLIPS[-1].get("pre", 0) + CARD_AT
fc.append(f"[{n}:v]format=rgba,trim=duration={total:.3f},fade=t=in:st={card_t:.3f}:d=0.7:alpha=1[card]")
fc.append(f"{prev}[card]overlay=x=0:y='18*max(0,1-(t-{card_t:.3f})/0.7)':eof_action=pass:format=auto,"
          f"fade=t=out:st={total - 1.2:.3f}:d=1.2,format=yuv420p[vout]")

# audio
ai = n + 1
mix = []
for i, c in enumerate(CLIPS):
    if c.get("intro"):
        continue
    d = int(round(c["start"] * 1000))
    fc.append(f"[{ai}:a]adelay={d}:all=1[sp{i}]")
    mix.append(f"[sp{i}]")
    ai += 1
fc.append(f"[{ai}:a]atrim=end={CLIPS[0]['len']:.3f},afade=t=out:st={CLIPS[0]['len'] - 0.8:.3f}:d=0.8,"
          f"aresample={SR},aformat=channel_layouts=stereo[sfx]")
mix.append("[sfx]")
ai += 1
fc.append(f"[{ai}:a]{music_af}[mus]")
mix.append("[mus]")
fc.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=longest,"
          f"atrim=end={total:.3f},alimiter=limit=0.89:attack=5:release=60:level=false[aout]")

with open(f"{WD}/filter.txt", "w") as fh:
    fh.write(";\n".join(fc))
run(["ffmpeg", "-y", *inputs, "-filter_complex_script", f"{WD}/filter.txt", "-map", "[vout]", "-map", "[aout]",
     "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-profile:v", "high", "-pix_fmt", "yuv420p",
     "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-ar", str(SR), "-movflags", "+faststart",
     "-t", f"{total:.3f}", OUT])

report = dict(total=round(total, 2), merged_speech=[[round(a, 2), round(b, 2)] for a, b in merged],
              card_at=round(card_t, 2), music_gain=round(mg, 2),
              clips=[{k: (round(v, 3) if isinstance(v, float) else v) for k, v in c.items() if k != "eq"}
                     for c in CLIPS])
json.dump(report, open(f"{WD}/report.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(report, ensure_ascii=False, indent=1))
