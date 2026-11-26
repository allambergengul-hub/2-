"""Render the venue card as a transparent 720x1264 PNG overlay (drawn at 2x, downscaled)."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONTS = sys.argv[1]
OUT = sys.argv[2]
W, H = 720, 1264
S = 2  # supersampling

HEADING = "Өтетін орны:"
LINES = ["Ақтау қаласы, 31-микрорайон", "Жерұйық мейрамханасы"]
DATE = "05.12.2026 | 18:00"

MAROON = (106, 40, 18, 255)
BROWN = (74, 40, 20, 255)
GOLD = (190, 146, 62, 255)
GOLD_DARK = (150, 100, 30, 255)
IVORY = (255, 248, 234)


def font(name, size, weight):
    f = ImageFont.truetype(f"{FONTS}/{name}", size * S)
    f.set_variation_by_axes([weight])
    return f


f_head = font("PlayfairDisplay-Italic[wght].ttf", 50, 700)
f_body = font("CormorantGaramond[wght].ttf", 39, 700)
f_date = font("PlayfairDisplay[wght].ttf", 34, 700)

# panel geometry (in 1x units)
px0, px1 = 44, W - 44
pad_top, gap_head, gap_div, line_h, gap_date, pad_bot = 26, 8, 14, 46, 10, 30
head_h, div_h, date_h = 60, 14, 46
ph = pad_top + head_h + gap_head + div_h + gap_div + line_h * len(LINES) + gap_date + date_h + pad_bot
py1 = H - 46
py0 = py1 - ph

img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))

# soft shadow
sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle(
    [px0 * S, (py0 + 8) * S, px1 * S, (py1 + 8) * S], radius=28 * S, fill=(40, 20, 5, 120))
sh = sh.filter(ImageFilter.GaussianBlur(14 * S))
img.alpha_composite(sh)

d = ImageDraw.Draw(img)
# panel + double gold frame
d.rounded_rectangle([px0 * S, py0 * S, px1 * S, py1 * S], radius=28 * S, fill=IVORY + (238,))
d.rounded_rectangle([(px0 + 8) * S, (py0 + 8) * S, (px1 - 8) * S, (py1 - 8) * S],
                    radius=22 * S, outline=GOLD, width=3 * S)
d.rounded_rectangle([(px0 + 15) * S, (py0 + 15) * S, (px1 - 15) * S, (py1 - 15) * S],
                    radius=17 * S, outline=GOLD[:3] + (150,), width=1 * S)


def center_text(text, f, y, fill, shadow=None):
    w = d.textlength(text, font=f, features=["lnum"])
    x = (W * S - w) / 2
    if shadow:
        d.text((x + 1.5 * S, y * S + 1.5 * S), text, font=f, fill=shadow, features=["lnum"])
    d.text((x, y * S), text, font=f, fill=fill, features=["lnum"])


y = py0 + pad_top
center_text(HEADING, f_head, y, MAROON, shadow=(190, 146, 62, 110))
y += head_h + gap_head

# ornamental divider: line — diamond — line
cy = (y + div_h / 2) * S
cx = W * S / 2
half = 150 * S
d.line([cx - half, cy, cx - 16 * S, cy], fill=GOLD, width=2 * S)
d.line([cx + 16 * S, cy, cx + half, cy], fill=GOLD, width=2 * S)
r = 7 * S
d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=GOLD)
for sx in (-1, 1):
    ex = cx + sx * (half + 6 * S)
    d.ellipse([ex - 3 * S, cy - 3 * S, ex + 3 * S, cy + 3 * S], fill=GOLD)
y += div_h + gap_div

for line in LINES:
    center_text(line, f_body, y, BROWN)
    y += line_h
y += gap_date
center_text(DATE, f_date, y, GOLD_DARK)

img = img.resize((W, H), Image.LANCZOS)
img.save(OUT)
print("panel", py0, py1)
