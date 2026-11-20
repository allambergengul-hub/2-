"""Builds the whole film: one sub-composition per act, one frame per sentence.
Run from the project root: python3 tools/build.py
"""
import re, json, os
from html.parser import HTMLParser

SRC = open("tools/gen_frames.py").read()
SRC = SRC[: SRC.index("\nD = 3")]
SRC = SRC.replace('proj = sys.argv[1]', 'proj = "."')
g = {}
exec(SRC, g)
CSS, fonts, F_INTRO = g["CSS"], g["fonts"], g["F"]
stage, char, phone, post, thought, clock = g["stage"], g["char"], g["phone"], g["post"], g["thought"], g["clock"]
CAR, BEACH, HOUSE, APPBAR = g["CAR"], g["BEACH"], g["HOUSE"], g["APPBAR"]

# ---------------- helpers ----------------
def Y(t): return f'<span class="x3d">{t}</span>'
def H(t, size=100, x=130, y=330, w=None, center=False, cls="w3d"):
    st = f"left:0;right:0;text-align:center;" if center else f"left:{x}px;"
    ww = f"width:{w}px;" if w else ""
    return f'<div class="h {cls}" style="position:absolute;{st}top:{y}px;font-size:{size}px;{ww}">{t}</div>'
def K(t, x=130, y=250, center=False):
    st = "left:0;right:0;text-align:center;" if center else f"left:{x}px;"
    return f'<div style="position:absolute;{st}top:{y}px;font-size:28px;font-weight:800;letter-spacing:.2em;color:var(--muted);text-transform:uppercase">{t}</div>'
def CHIP(t, x, y, dark=False):
    return f'<div class="chip{" dark" if dark else ""}" style="position:absolute;left:{x}px;top:{y}px">{t}</div>'
def G(x, y, w, inner, h=None, ry=0, rot=0, pad=56, extra=""):
    hh = f"height:{h}px;" if h else ""
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;perspective:1800px"><div class="glass" style="position:relative;width:{w}px;{hh}padding:{pad}px;'
            f'transform:rotateY({ry}deg) rotate({rot}deg);{extra}">{inner}</div></div>')
def P(t, size=40, col="var(--ivory)", w=800, mt=0):
    return f'<div style="font-size:{size}px;font-weight:700;color:{col};line-height:1.35;max-width:{w}px;margin-top:{mt}px">{t}</div>'
def BIG(t, size=150, col="#fff"):
    nw = "white-space:nowrap;" if re.search(r"\d", t) else ""
    return f'<div class="h" style="font-size:{size}px;color:{col};{nw}">{t}</div>'
def DOT(c): return f'<span style="display:inline-block;width:22px;height:22px;border-radius:50%;background:{c};box-shadow:0 0 18px {c};margin-right:18px;vertical-align:middle"></span>'
def ROW(c, t, size=40): return f'<div style="font-size:{size}px;font-weight:800;margin:16px 0">{DOT(c)}{t}</div>'
def STRIKE(t): return f'<span style="position:relative;color:var(--muted)">{t}<span style="position:absolute;left:-2%;right:-2%;top:52%;height:12px;background:var(--coral);border-radius:6px;transform:rotate(-3deg)"></span></span>'
def BAR(label, val, maxv, col, w=900, unit=""):
    pct = val / maxv * 100
    return (f'<div style="margin:22px 0"><div style="display:flex;justify-content:space-between;font-size:32px;font-weight:800;margin-bottom:12px"><span>{label}</span><span style="color:{col}">{unit}</span></div>'
            f'<div style="height:44px;width:{w}px;border-radius:22px;background:rgba(255,255,255,.08)"><div style="height:100%;width:{pct:.1f}%;border-radius:22px;background:linear-gradient(90deg,{col},{col}cc);box-shadow:0 0 30px {col}66"></div></div></div>')
def GRID(n, on, cols=15, size=40, col="#3ddc97", off="rgba(255,255,255,.08)", hi=None):
    cells = ""
    for i in range(n):
        c = col if i in on else off
        if hi is not None and i == hi: c = "#ffd21f"
        sh = f"box-shadow:0 0 16px {c};" if (i in on or i == hi) else ""
        cells += f'<div style="width:{size}px;height:{size}px;border-radius:8px;background:{c};{sh}"></div>'
    return f'<div style="display:grid;grid-template-columns:repeat({cols},{size}px);gap:10px">{cells}</div>'
def CHAPTER(num, title, sub):
    return stage("70%") + char("front", 1380, 300, 720) + \
        f'<div style="position:absolute;left:130px;top:300px"><div class="h" style="font-size:220px;color:transparent;-webkit-text-stroke:3px rgba(255,210,31,.8)">{num}</div>' \
        f'<div class="h w3d" style="font-size:96px;margin-top:10px">{title}</div><div style="font-size:38px;font-weight:700;color:var(--muted);margin-top:24px">{sub}</div></div>'
def TC(kicker, title, pose="front", side="r", size=100, extra="", lx=None):
    """text + character"""
    if side == "r":
        return stage(lx or "72%") + extra + char(pose, 1350, 300, 730) + K(kicker, 130, 300) + H(title, size, 130, 360, 1150)
    return stage(lx or "26%") + extra + char(pose, 230, 300, 730, flip=(pose in ("ldiag", "left", "rdiag", "right"))) + K(kicker, 880, 300) + H(title, size, 880, 360, 950)
def CARDCHAR(card, pose="front", side="r", head=""):
    if side == "r":
        return stage("74%") + card + char(pose, 1380, 300, 730) + head
    return stage("24%") + card + char(pose, 200, 300, 730) + head
def NEQ(a, b, kicker):
    return stage("50%") + K(kicker, center=True, y=220) + \
        G(150, 380, 700, BIG(a, 64), pad=60) + '<div class="h x3d" style="position:absolute;left:910px;top:400px;font-size:180px">≠</div>' + \
        G(1110, 380, 660, BIG(b, 64, "var(--y)"), pad=60)
def QUOTE(t, pose, layout): return thought(t, pose, layout)

def phone_post(user, color, inner, cap, likes, x=260, ry=16):
    return phone(x, 40, ry, 4, APPBAR + f'<div class="post"><div class="top"><div class="av" style="background:{color}"></div>{user}</div>{inner}<div class="cp">{cap} <span class="heart">♥ {likes}</span></div></div>')
def MONEY(amount, label, col="#0f3d2e", acc="#3ddc97"):
    return (f'<div style="height:420px;background:linear-gradient(160deg,{col},#06150f);display:flex;flex-direction:column;justify-content:center;padding:0 34px;color:#fff">'
            f'<div style="font-size:22px;letter-spacing:.2em;color:{acc};font-weight:800">{label}</div><div style="font-family:Unbounded;font-weight:900;font-size:50px;white-space:nowrap;margin-top:14px">{amount}</div></div>')
def CHAT():
    msgs = [("l", "Тағы кешіктің бе?"), ("r", "Жұмыс көп болды..."), ("l", "Әрқашан солай."), ("r", "Сөйлесейікші.")]
    s = ""
    for side, m in msgs:
        al = "flex-start" if side == "l" else "flex-end"
        bg = "#e9eaf2" if side == "l" else "#4a6cff"
        c = "#151830" if side == "l" else "#fff"
        s += f'<div style="display:flex;justify-content:{al};margin:16px 22px"><div style="background:{bg};color:{c};padding:16px 22px;border-radius:22px;font-size:26px;font-weight:700;max-width:340px">{m}</div></div>'
    return '<div style="padding-top:90px">' + s + '</div>'

# ---------------- frames: (sentence, html) ----------------
TH = []  # theory
TH.append(("Ең алдымен, өзімізді басқалармен салыстыру қазіргі заманның ғана мәселесі емес.",
  stage("50%") + K("Ең алдымен", center=True, y=200) + H(f"Бұл — {STRIKE('жаңа')} мәселе емес.", 92, center=True, y=260) +
  G(260, 560, 1400, '<div style="display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:36px"><span style="color:var(--muted)">Ежелгі заман</span><span style="flex:1;height:6px;margin:0 30px;background:linear-gradient(90deg,rgba(255,255,255,.1),var(--y));border-radius:3px"></span><span class="x3d" style="font-family:Unbounded">Бүгін</span></div>', pad=50)))
TH.append(("Бұл адамның психологиясында бұрыннан бар құбылыс.",
  TC("Психология", f"Бұрыннан бар<br/>{Y('құбылыс.')}", "rdiag")))
TH.append(("1954 жылы психолог Леон Фестингер әлеуметтік салыстыру теориясын ұсынды.",
  CARDCHAR(G(130, 170, 1080, BIG("1954", 210, "var(--y)") + P("Психолог <b>Леон Фестингер</b>", 50, mt=10) + '<div style="height:5px;width:160px;background:var(--y);margin:34px 0;border-radius:3px"></div>' + BIG("Әлеуметтік салыстыру теориясы", 66), ry=10, pad=70), "left")))
TH.append(("Оның негізгі идеясы бойынша, адамдар кейде өз қабілеттерін, пікірлерін және жетістіктерін бағалау үшін басқа адамдармен салыстырады.",
  stage("50%") + K("Негізгі идея", center=True, y=110) +
  ''.join(G(130, 230 + i * 220, 560, f'<div class="h" style="font-size:54px">{t}</div>', pad=44) for i, t in enumerate(["Қабілет", "Пікір", "Жетістік"])) +
  '<svg style="position:absolute;left:0;top:0" width="1920" height="1080"><g stroke="#ffd21f" stroke-width="6" fill="none" stroke-linecap="round"><path d="M720 300 C 900 300, 1000 520, 1160 540"/><path d="M720 520 L 1160 540"/><path d="M720 740 C 900 740, 1000 560, 1160 540"/></g></svg>' +
  G(1180, 410, 600, f'<div style="font-size:30px;font-weight:800;color:var(--muted);letter-spacing:.16em">БАҒАЛАУ ҮШІН</div><div class="h x3d" style="font-size:76px;margin-top:16px">Басқалар</div>', pad=56)))
TH.append(("Мысалы, сіз жаңа жұмысқа орналастыңыз делік.",
  CARDCHAR(G(160, 200, 700, '<div style="display:flex;gap:40px;align-items:center"><div style="width:190px;height:230px;border-radius:24px;background:#2b3060;overflow:hidden;position:relative"><img src="assets/char/face.png" style="position:absolute;left:10px;top:20px;width:170px"/></div><div><div style="font-size:26px;letter-spacing:.2em;color:var(--muted);font-weight:800">ҚЫЗМЕТКЕР</div><div class="h" style="font-size:52px;margin-top:10px">Жаңа<br/>маман</div></div></div><div style="margin-top:40px;height:16px;background:repeating-linear-gradient(90deg,#fff 0 6px,transparent 6px 12px);opacity:.6"></div><div style="margin-top:22px;font-size:30px;font-weight:800;color:var(--y)">1-КҮН</div>', ry=12, rot=-3), "ldiag", "r",
    K("Мысалы", 130, 860) + H(f"Жаңа {Y('жұмыс.')}", 86, 130, 900))))
for q, pose, lay in [("Өз жұмысыңызды жақсы<br/>атқарып жүрсіз бе?", "front", 0), ("Жалақыңыз<br/>жеткілікті ме?", "ldiag", 1), ("Қаншалықты<br/>тәжірибелісіз?", "face", 2)]:
    TH.append((q.replace("<br/>", " "), QUOTE(q, pose, lay)))
TH.append(("Мұндай сұрақтарға жауап іздегенде айналаңыздағы адамдарға қарайсыз.",
  stage("50%") + char("front", 830, 300, 700) +
  ''.join(G(x, y, 330, f'<div style="display:flex;align-items:center;gap:18px"><div style="width:64px;height:64px;border-radius:50%;background:{c}"></div><div><div style="font-size:28px;font-weight:800">{n}</div><div style="font-size:22px;color:var(--muted);font-weight:700">{r}</div></div></div>', pad=28)
          for x, y, c, n, r in [(160, 200, "#ff6b5b", "Әріптес", "Бөлім"), (1420, 200, "#7cc4ff", "Дос", "Мектеп"), (160, 640, "#3ddc97", "Таныс", "Желі"), (1420, 640, "#b28cff", "Көрші", "Аула")]) +
  H(f"Айналаңызға {Y('қарайсыз.')}", 70, center=True, y=60)))
TH.append(("Әріптесіңіз сізден көп ақша табуы мүмкін.",
  CARDCHAR(G(130, 230, 1060, K("Айлық табыс", 0, 0).replace("position:absolute;left:0px;top:0px;", "") + BAR("Сіз", 300, 450, "#ffd21f", 940, "300 000 ₸") + BAR("Әріптес", 450, 450, "#ff6b5b", 940, "450 000 ₸"), pad=60), "rdiag", "r",
           H(f"Әріптес {Y('көбірек')} табады.", 64, 130, 760))))
TH.append(("Досыңыз қызметте жоғарылауы мүмкін.",
  CARDCHAR(G(160, 230, 900, '<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">ЖАҢАЛЫҚ</div><div class="h" style="font-size:60px;margin-top:20px">Досыңыз — <span style="color:var(--mint)">аға менеджер</span></div><div style="display:flex;gap:18px;margin-top:40px;align-items:center;font-size:36px;font-weight:800"><span style="color:var(--muted)">Менеджер</span><span style="color:var(--mint);font-size:50px">→</span><span>Аға менеджер ▲</span></div>', ry=10, pad=64), "left", "r")))
TH.append(("Сіз еріксіз өз жағдайыңызды олардың жағдайымен салыстырасыз.",
  stage("50%") + G(150, 300, 660, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">МЕН</div>{BIG("300 000 ₸", 70, "var(--y)")}{P("Қызмет: маман", 34, "var(--muted)")}', pad=60, ry=14) +
  '<div class="h x3d" style="position:absolute;left:880px;top:330px;font-size:160px">⇄</div>' +
  G(1110, 300, 660, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">ОЛАР</div>{BIG("450 000 ₸", 70)}{P("Қызмет: аға менеджер", 34, "var(--muted)")}', pad=60, ry=-14) +
  H(f"Еріксіз {Y('салыстырасыз.')}", 80, center=True, y=760)))
TH.append(("Бұл кейде пайдалы.",
  stage("50%") + '<div style="position:absolute;left:810px;top:180px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#7ff0bf,#3ddc97 45%,#0f8a55);box-shadow:0 40px 80px rgba(0,0,0,.5),0 0 120px rgba(61,220,151,.4);display:flex;align-items:center;justify-content:center;font-size:170px;color:#fff;font-weight:900">✓</div>' +
  H(f"Кейде — {Y('пайдалы.')}", 120, center=True, y=600)))
TH.append(("Өйткені салыстыру арқылы адам өзінің қай бағытта дамуы керектігін түсінуі мүмкін.",
  TC("Өйткені", f"Салыстыру —<br/>{Y('бағдар')} береді.", "back", "l", 96,
     '<svg style="position:absolute;left:300px;top:120px" width="700" height="500"><defs><linearGradient id="ar" x1="0" x2="1"><stop offset="0" stop-color="rgba(255,210,31,0)"/><stop offset="1" stop-color="#ffd21f"/></linearGradient></defs><path d="M40 460 C 200 380, 380 300, 600 80" stroke="url(#ar)" stroke-width="22" fill="none" stroke-linecap="round"/><path d="M560 70 L620 60 L610 120" stroke="#ffd21f" stroke-width="22" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')))
TH.append(("Бірақ мәселе салыстырудың өзінде емес.",
  stage("50%") + K("Бірақ", center=True, y=330) + H(f"Мәселе {STRIKE('салыстыруда')} емес.", 82, center=True, y=400)))
TH.append(("Мәселе — біз кімді таңдайтынымызда және сол салыстырудан қандай қорытынды шығаратынымызда.",
  stage("50%") + K("Мәселе мынада", center=True, y=170) +
  G(170, 330, 740, f'<div class="h x3d" style="font-size:150px">01</div><div class="h" style="font-size:68px;margin-top:10px">Кімді<br/>таңдаймыз?</div>', pad=60, ry=12) +
  G(1010, 330, 740, f'<div class="h x3d" style="font-size:150px">02</div><div class="h" style="font-size:68px;margin-top:10px">Қандай қорытынды<br/>шығарамыз?</div>', pad=60, ry=-12)))
TH.append(("Психологияда жоғары бағытталған әлеуметтік салыстыру деген ұғым бар.",
  CARDCHAR(G(130, 210, 1100, '<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">ПСИХОЛОГИЯЛЫҚ ҰҒЫМ</div><div class="h x3d" style="font-size:84px;margin-top:24px">Жоғары бағытталған</div><div class="h" style="font-size:84px">салыстыру</div><div style="font-size:34px;font-weight:600;color:var(--muted);margin-top:28px;font-style:italic">upward social comparison</div>', ry=10, pad=70), "left")))
TH.append(("Бұл — өзімізді бізден табыстырақ, әдемірек немесе қабілеттілеу деп қабылдайтын адамдармен салыстыру.",
  stage("50%") + H("Бізден «жоғары» адамдармен", 70, center=True, y=150) +
  ''.join(G(170 + i * 560, 400, 460, f'<div style="font-size:90px;color:var(--y);font-weight:900">▲</div><div class="h" style="font-size:56px;margin-top:10px">{t}</div>', pad=50) for i, t in enumerate(["Табыстырақ", "Әдемірек", "Қабілеттірек"]))))
TH.append(("Мысалы, сіз айына 300 мың теңге табасыз.",
  CARDCHAR(G(160, 260, 960, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">СІЗДІҢ ТАБЫСЫҢЫЗ</div>{BIG("300 000 ₸", 116, "var(--y)")}<div style="font-size:40px;font-weight:700;color:var(--muted)">айына</div>', pad=70, ry=10), "front")))
TH.append(("Бірақ әлеуметтік желіден айына бірнеше миллион табатын адамды көрдіңіз.",
  stage("35%") + phone_post("biznes.guru", "#3ddc97", MONEY("5 000 000 ₸", "АЙЛЫҚ ТАБЫС"), "Жұмыстан кеттім, енді...", "48 200") +
  K("Әлеуметтік желіде", 1020, 330) + H(f"Айына<br/>{Y('миллиондар.')}", 86, 1020, 390)))
TH.append(("Сол сәтте өз табысыңыз аз болып көрінуі мүмкін.",
  stage("50%") + G(170, 380, 520, f'{BIG("300 000 ₸", 54, "var(--muted)")}', pad=40) + G(760, 200, 1000, f'{BIG("5 000 000 ₸", 98)}', pad=70) +
  H(f"Өз табысыңыз — {Y('аз')} сияқты.", 76, center=True, y=780)))
TH.append(("Ал сіздің өміріңізде сізден аз табатын, мүмкіндігі шектеулі адам да бар екенін ұмытып кетесіз.",
  stage("50%") + '<div style="position:absolute;left:200px;top:700px;width:480px;height:380px;background:linear-gradient(#2a2f58,#1d2142);border-top:4px solid #7cc4ff;box-shadow:0 0 60px rgba(124,196,255,.4)"></div>' +
  '<div style="position:absolute;left:720px;top:520px;width:480px;height:560px;background:linear-gradient(#3b4170,#252a52);border-top:4px solid #ffd21f"></div>' +
  '<div style="position:absolute;left:1240px;top:240px;width:480px;height:840px;background:linear-gradient(#4a5190,#2b3060);border-top:4px solid #fff"></div>' +
  '<div class="h" style="position:absolute;left:230px;top:730px;font-size:44px;color:#7cc4ff">150 000 ₸</div><div class="h" style="position:absolute;left:750px;top:550px;font-size:52px;color:var(--y)">300 000 ₸</div><div class="h" style="position:absolute;left:1270px;top:270px;font-size:60px">5 млн ₸</div>' +
  char("right", 860, 160, 380, pool=False) + G(160, 470, 520, '<div style="font-size:32px;font-weight:800;color:#7cc4ff">Бұл адамды ұмытамыз</div>', pad=26)))
TH.append(("Біз көбіне өзімізден озық адамдарға назар аударамыз.",
  stage("50%") + '<div style="position:absolute;left:760px;top:0;width:400px;height:1080px;background:linear-gradient(rgba(255,210,31,.35),rgba(255,210,31,0));clip-path:polygon(35% 0,65% 0,100% 100%,0 100%)"></div>' +
  char("back", 840, 320, 700) + H(f"Назар — тек {Y('жоғарыға.')}", 76, center=True, y=100)))
TH.append(("Осылайша өзіміздің жетістіктерімізді байқамай қаламыз.",
  CARDCHAR(G(160, 200, 900, K("Сіздің жетістіктеріңіз", 0, 0).replace("position:absolute;left:0px;top:0px;", "") + ''.join(f'<div style="font-size:40px;font-weight:800;margin:22px 0;opacity:{o}">✓ {t}</div>' for t, o in [("Тұрақты жұмыс", .45), ("Жаңа дағды", .35), ("Денсаулық", .28), ("Отбасы", .2)]), pad=64, ry=10), "rdiag", "r",
           H(f"Байқамай {Y('қаламыз.')}", 70, 160, 860))))
TH.append(("Бір маңызды нәрсе бар.",
  stage("50%") + CHIP("Маңызды", 840, 380) + H(f"Бір {Y('маңызды')} нәрсе.", 110, center=True, y=500)))
TH.append(("Басқа адамның жетістігі сіздің сәтсіздігіңізді білдірмейді.",
  NEQ("Басқаның жетістігі", "Сіздің сәтсіздігіңіз", "Есте сақтаңыз")))
TH.append(("Біреудің 25 жасында үй алғаны сіздің 30 жаста үй алуыңыз кеш деген сөз емес.",
  stage("50%") + H(f"30 жас — {Y('кеш емес.')}", 92, center=True, y=110) +
  '<div style="position:absolute;left:200px;top:470px;width:1520px;height:8px;background:rgba(255,255,255,.25);border-radius:4px"></div><div style="position:absolute;left:200px;top:760px;width:1520px;height:8px;background:rgba(255,255,255,.25);border-radius:4px"></div>' +
  '<div style="position:absolute;left:200px;top:500px;font-size:34px;font-weight:800;color:var(--muted)">Біреу</div><div style="position:absolute;left:200px;top:790px;font-size:34px;font-weight:800;color:var(--muted)">Сіз</div>' +
  G(700, 370, 480, '<div class="h" style="font-size:44px;white-space:nowrap">25 жас · Үй ✓</div>', pad=34) + G(1130, 660, 480, '<div class="h x3d" style="font-size:44px;white-space:nowrap">30 жас · Үй ✓</div>', pad=34)))
TH.append(("Әр адамның бастапқы мүмкіндігі, жағдайы, таңдауы және өмір жолы әртүрлі.",
  stage("50%") + H(f"Әркімнің жолы — {Y('әртүрлі.')}", 80, center=True, y=110) +
  ''.join(G(160 + (i % 2) * 820, 330 + (i // 2) * 300, 760, f'<div style="display:flex;align-items:center;gap:30px"><div class="h x3d" style="font-size:80px">0{i+1}</div><div class="h" style="font-size:50px">{t}</div></div>', pad=46) for i, t in enumerate(["Бастапқы мүмкіндік", "Жағдай", "Таңдау", "Өмір жолы"]))))
TH.append(("Бірақ біз мұны білгенімізбен, эмоциямызды әрдайым басқара алмаймыз.",
  NEQ("Білемін", "Сеземін", "Бірақ")))

SO = []  # social media
SO.append(("Енді ең қызықты бөлігіне келейік.", CHAPTER("02", "Әлеуметтік желі", "Ең қызықты бөлігі")))
SO.append(("Неліктен әлеуметтік желілерде өзімізді өзгелермен салыстыру жиі кездеседі?",
  stage("65%") + phone(1200, 40, -18, 4, APPBAR + post("arman_auto", "#ff6b5b", CAR, "Арман орындалды!", "2 450", 300) + post("aru.travels", "#7cc4ff", BEACH, "Мальдив", "5 120", 300)) +
  K("Сұрақ", 130, 300) + H(f"Неге дәл<br/>{Y('желіде')}<br/>жиі?", 110, 130, 360)))
SO.append(("Себебі біз көбіне адамдардың күнделікті өмірін емес, олардың таңдаулы сәттерін көреміз.",
  stage("50%") + H(f"{STRIKE('Күнделікті өмір')} → {Y('таңдаулы сәттер')}", 66, center=True, y=140) +
  '<div style="position:absolute;left:160px;top:420px;display:flex;gap:22px">' + ''.join(f'<div style="width:140px;height:240px;border-radius:18px;background:{"linear-gradient(160deg,#ffd21f,#ff9d00)" if i == 6 else "rgba(255,255,255,.07)"};box-shadow:{"0 0 60px rgba(255,210,31,.6)" if i == 6 else "none"};border:2px solid rgba(255,255,255,.12)"></div>' for i in range(10)) + '</div>' +
  '<div style="position:absolute;left:1010px;top:690px;font-size:32px;font-weight:800;color:var(--y)">← жарияланады</div><div style="position:absolute;left:160px;top:690px;font-size:32px;font-weight:800;color:var(--muted)">көрінбейді</div>'))
on_hard = set()
SO.append(("Бір адам бір жыл бойы қиындықпен жұмыс істеуі мүмкін.",
  stage("50%") + H(f"365 күн — {Y('қиын еңбек.')}", 80, center=True, y=100) + f'<div style="position:absolute;left:310px;top:260px">{GRID(365, set(), cols=31, size=34, off="rgba(255,107,91,.35)")}</div>'))
SO.append(("Бірақ әлеуметтік желіге тек жаңа көлігінің суретін салады.",
  stage("50%") + H(f"Желіге — тек {Y('1 күн.')}", 80, center=True, y=100) + f'<div style="position:absolute;left:310px;top:260px;opacity:.35">{GRID(365, set(), cols=31, size=34, off="rgba(255,107,91,.5)")}</div>' +
  f'<div style="position:absolute;left:640px;top:330px;width:640px;height:400px;border-radius:30px;overflow:hidden;container-type:inline-size;box-shadow:0 50px 100px rgba(0,0,0,.7),0 0 0 4px #ffd21f">{CAR}</div>'))
SO.append(("Біреу қарым-қатынасында қиындық көріп жүруі мүмкін.",
  stage("35%") + phone(260, 40, 16, 4, CHAT()) + K("Шынайы өмір", 1020, 330) + H(f"Қарым-қатынаста<br/>{Y('қиындық.')}", 92, 1020, 390)))
SO.append(("Бірақ интернетке тек бақытты сәттерін жариялайды.",
  stage("35%") + phone_post("aigerim.love", "#ff6b5b", '<div style="height:420px;background:linear-gradient(160deg,#ff9a8b,#ff6a88 55%,#ff99ac);display:flex;align-items:center;justify-content:center;font-family:Unbounded;font-weight:900;font-size:40px;color:#fff">♥ Бақыттымыз</div>', "5 жыл бірге!", "12 900") +
  K("Желіде", 1020, 330) + H(f"Тек<br/>{Y('бақытты')}<br/>сәттер.", 104, 1020, 390)))
SO.append(("Біреу қарызға батып жүрсе де, сырт көзге бай болып көрінуі мүмкін.",
  stage("50%") + K("Сырт көзге", 170, 200) + K("Шындығында", 1060, 200) +
  '<div style="position:absolute;left:170px;top:300px;perspective:1600px"><div style="width:640px;height:400px;border-radius:30px;transform:rotateY(14deg) rotate(-4deg);background:linear-gradient(135deg,#2a2a2e,#0b0b0d 55%,#3a3a40);box-shadow:inset 0 1px 0 rgba(255,255,255,.3),0 50px 80px rgba(0,0,0,.6);padding:44px;color:#e9e9ee;position:relative"><div style="width:84px;height:62px;border-radius:12px;background:linear-gradient(135deg,#f5d77a,#b8902e)"></div><div style="font-size:36px;letter-spacing:.16em;margin-top:60px;font-weight:700">4400 •••• •••• 2525</div><div style="position:absolute;right:44px;bottom:36px;font-family:Unbounded;font-weight:900;font-size:36px;font-style:italic">PREMIUM</div></div></div>' +
  G(1060, 300, 700, '<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">НЕСИЕ ҚАРЫЗЫ</div><div class="h" style="font-size:80px;color:var(--coral);margin-top:16px">−12,4 млн ₸</div>' + ROW("#ff6b5b", "Мерзімі өткен: 3 ай", 32) + ROW("#ff6b5b", "Айлық төлем: 410 000 ₸", 32), pad=56)))
SO.append(("Біз экраннан осы әдемі сәттерді көреміз де, оны өз өміріміздің шынайы жағдайымен салыстырамыз.",
  stage("50%") + phone(1180, 40, -16, 4, APPBAR + post("arman_auto", "#ff6b5b", CAR, "Арман орындалды!", "2 450", 300) + post("dana.home", "#3ddc97", HOUSE, "Өз үйіміз!", "8 900", 300), 1) +
  char("rdiag", 260, 300, 730) + '<div class="h x3d" style="position:absolute;left:820px;top:380px;font-size:200px">⇄</div>' + H(f"Экран vs {Y('шындық')}", 70, 120, 110)))
SO.append(("Бірақ бұл — әділ салыстыру емес.",
  stage("50%") + '<svg style="position:absolute;left:560px;top:200px" width="800" height="560" viewBox="0 0 800 560"><g transform="rotate(-12 400 120)"><line x1="80" y1="120" x2="720" y2="120" stroke="#ffd21f" stroke-width="14" stroke-linecap="round"/><path d="M80 120 L30 260 L130 260 Z M720 120 L670 260 L770 260 Z" fill="none" stroke="#ffd21f" stroke-width="8"/><rect x="20" y="260" width="120" height="16" rx="8" fill="#ffd21f"/><rect x="660" y="260" width="120" height="16" rx="8" fill="#ffd21f"/></g><line x1="400" y1="120" x2="400" y2="520" stroke="#ffd21f" stroke-width="14"/><rect x="300" y="510" width="200" height="22" rx="11" fill="#ffd21f"/></svg>' +
  H(f"Бұл — {Y('әділ емес.')}", 116, center=True, y=780)))
SO.append(("Сіз өзіңіздің өміріңіздің барлық қиындықтарын білесіз.",
  CARDCHAR(G(160, 230, 960, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">ӨЗ ӨМІРІҢІЗ</div>{BIG("100%", 190, "var(--y)")}<div style="font-size:40px;font-weight:700;color:var(--muted)">барлық қиындығын көресіз</div>', pad=70, ry=10), "front")))
SO.append(("Ал басқа адамның өмірінен тек оның көрсеткісі келген бөлігін көресіз.",
  CARDCHAR(G(160, 230, 960, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">БАСҚАНЫҢ ӨМІРІ</div>{BIG("5%", 190)}<div style="font-size:40px;font-weight:700;color:var(--muted)">тек көрсеткісі келгені</div>', pad=70, ry=10), "rdiag")))
SO.append(("Осы айырмашылықты түсіну өте маңызды.", stage("50%") + H(f"100% {Y('≠')} 5%", 220, center=True, y=300) + H("Айырмашылықты түсініңіз.", 60, center=True, y=650, cls="")))
SO.append(("Әлеуметтік желідегі сурет адамның толық өмірін көрсетпейді.",
  stage("50%", False) + '<div style="position:absolute;left:0;right:0;top:560px;height:4px;background:rgba(124,196,255,.6)"></div><div style="position:absolute;left:0;right:0;top:564px;bottom:0;background:linear-gradient(rgba(74,124,255,.25),rgba(20,23,45,0))"></div>' +
  '<svg style="position:absolute;left:560px;top:250px" width="800" height="830" viewBox="0 0 800 830"><polygon points="400,0 520,310 280,310" fill="#f5f1e8"/><polygon points="280,310 520,310 700,520 620,760 400,830 160,740 90,520" fill="rgba(124,196,255,.35)" stroke="rgba(124,196,255,.7)" stroke-width="4"/></svg>' +
  CHIP("Пост", 1020, 380) + '<div class="h" style="position:absolute;left:1280px;top:760px;font-size:56px;color:#7cc4ff">Толық өмір</div>' + H(f"Сурет — тек {Y('ұшы.')}", 80, center=True, y=90)))
SO.append(("Сондықтан біреудің жариялаған суретіне қарап, оның өмірі мінсіз деп ойлау дұрыс емес.",
  stage("50%") + H(f"Оның өмірі {STRIKE('мінсіз')}", 110, center=True, y=380) + H("деп ойлау — қате.", 64, center=True, y=600, cls="")))
SO.append(("Адам өзін үнемі өзгелермен салыстыра берсе, бірте-бірте өзінің жетістіктерін бағаламай бастауы мүмкін.",
  CARDCHAR(G(160, 230, 960, K("Өзін бағалау", 0, 0).replace("position:absolute;left:0px;top:0px;", "") + BAR("1-ай", 90, 100, "#3ddc97", 840) + BAR("6-ай", 55, 100, "#ffd21f", 840) + BAR("1-жыл", 20, 100, "#ff6b5b", 840), pad=64), "back", "r",
           H(f"Бірте-бірте {Y('төмендейді.')}", 64, 160, 870))))
SO.append(("Мысалы, сіз бір ай бойы жаңа дағды үйрендіңіз.",
  CARDCHAR(G(160, 230, 820, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800;margin-bottom:28px">30 КҮН · ЖАҢА ДАҒДЫ</div>{GRID(30, set(range(30)), cols=10, size=58)}', pad=60, ry=10), "front", "r", H(f"1 ай — {Y('еңбек.')}", 70, 160, 860))))
SO.append(("Бұрын жасай алмаған жұмысты енді орындай аласыз.",
  stage("50%") + G(170, 330, 700, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">БҰРЫН</div>{BIG("0%", 160, "var(--muted)")}', pad=60, ry=12) +
  '<div class="h x3d" style="position:absolute;left:910px;top:420px;font-size:120px">→</div>' +
  G(1060, 330, 700, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800">ҚАЗІР</div>{BIG("100%", 160, "var(--mint)")}', pad=60, ry=-12)))
SO.append(("Бірақ интернеттен осы саланың маманын көрдіңіз.",
  stage("35%") + phone_post("pro.master", "#b28cff", MONEY("10 жыл", "ТӘЖІРИБЕ", "#2a1f5c", "#b28cff"), "Мастер-класс бүгін!", "31 400") + K("Интернетте", 1020, 330) + H(f"Сала<br/>{Y('маманы.')}", 110, 1020, 390)))
SO.append(("Ол сізден әлдеқайда тәжірибелі.",
  CARDCHAR(G(160, 260, 1060, BAR("Сіз", 1, 120, "#ffd21f", 940, "1 ай") + BAR("Маман", 120, 120, "#b28cff", 940, "10 жыл"), pad=64), "ldiag", "r", H(f"Әлдеқайда {Y('тәжірибелі.')}", 64, 160, 760))))
SO.append(("Сөйтіп, өзіңіздің бір айлық еңбегіңізді жоққа шығарасыз.",
  CARDCHAR(G(160, 230, 820, f'<div style="font-size:28px;letter-spacing:.2em;color:var(--muted);font-weight:800;margin-bottom:28px">30 КҮН · ЖАҢА ДАҒДЫ</div><div style="opacity:.35">{GRID(30, set(range(30)), cols=10, size=58)}</div><div class="h" style="position:absolute;left:0;right:0;top:45%;text-align:center;font-size:100px;color:var(--coral);transform:rotate(-8deg)">ЖОҚ?</div>', pad=60, ry=10), "back", "r")))
SO.append(("Тағы бір жағдай.", stage("50%") + CHIP("Тағы бір жағдай", 740, 420) + H(f"{Y('Келбет.')}", 140, center=True, y=530)))
SO.append(("Сіз өз келбетіңізге көңіліңіз толып жүрсіз.",
  stage("50%") + '<div style="position:absolute;left:660px;top:120px;width:600px;height:820px;border-radius:300px 300px 30px 30px;background:linear-gradient(160deg,rgba(255,255,255,.18),rgba(255,255,255,.04));border:6px solid rgba(255,255,255,.3);box-shadow:0 60px 120px rgba(0,0,0,.5);overflow:hidden"><img src="assets/char/face.png" style="position:absolute;left:60px;top:200px;width:480px"/></div>' +
  G(1320, 300, 460, ROW("#3ddc97", "Ұнайды", 44) + ROW("#3ddc97", "Өзіммін", 44), pad=40)))
SO.append(("Бірақ әлеуметтік желіден мінсіз өңделген фотосуреттерді көрген соң, өзіңізден мін іздей бастайсыз.",
  stage("35%") + phone(260, 40, 16, 4, '<div style="padding:90px 30px 0;color:#151830"><div style="height:440px;border-radius:26px;background:linear-gradient(160deg,#ffd6e0,#ffb8c9 50%,#e5a0ff);"></div>' + ''.join(f'<div style="margin-top:30px;font-size:24px;font-weight:800;display:flex;justify-content:space-between"><span>{n}</span><span>{v}</span></div><div style="height:10px;border-radius:5px;background:#e3e5ef;margin-top:10px"><div style="height:100%;width:{v}%;border-radius:5px;background:#ff4d6d"></div></div>' for n, v in [("Тегістеу", 100), ("Сүзгі", 90), ("Пішін", 75)]) + '</div>') +
  K("Өңделген фото", 1020, 330) + H(f"«Мінсіз»<br/>{Y('фильтр.')}", 104, 1020, 390)))
SO.append(("Бұл жерде есте сақтайтын нәрсе бар:", stage("50%") + CHIP("Есте сақтаңыз", 760, 420) + H(f"Ең {Y('маңыздысы:')}", 110, center=True, y=530)))
SO.append(("Сіздің құндылығыңыз басқа адамның жетістігімен өлшенбейді.",
  stage("50%") + '<div style="position:absolute;left:360px;top:300px;width:1200px;height:110px;border-radius:16px;background:linear-gradient(#ffe066,#ffc800);box-shadow:0 30px 60px rgba(0,0,0,.5);transform:rotate(-4deg);background-image:repeating-linear-gradient(90deg,rgba(0,0,0,.5) 0 3px,transparent 3px 60px),linear-gradient(#ffe066,#ffc800)"></div>' +
  '<div style="position:absolute;left:300px;top:340px;width:1320px;height:16px;background:var(--coral);border-radius:8px;transform:rotate(8deg)"></div>' +
  H(f"Құндылығыңыз {Y('өлшенбейді.')}", 84, center=True, y=620)))
for a, b in [("Біреудің әдемілігі", "Сіз ұсқынсыз"), ("Біреудің байлығы", "Сіз кедей"), ("Біреудің жетістігі", "Сіздің шегіңіз")]:
    s = {"Сіз ұсқынсыз": "Біреудің әдемілігі сізді ұсқынсыз етпейді.", "Сіз кедей": "Біреудің байлығы сізді кедей адам ретінде анықтамайды.", "Сіздің шегіңіз": "Біреудің жетістігі сіздің болашағыңызға шек қоймайды."}[b]
    SO.append((s, NEQ(a, b, "Есте сақтаңыз")))

ME = []  # methods
ME.append(("Енді мұны қалай өзгертуге болады?", CHAPTER("03", "Не істеу керек?", "Төрт әдіс")))
ME.append(("Бірінші әдіс — өзіңізді кешегі өзіңізбен салыстырыңыз.",
  stage("72%") + CHIP("1-әдіс", 130, 230) + H(f"Кешегі<br/>{Y('өзіңізбен')}<br/>салыстырыңыз.", 74, 130, 330) +
  char("front", 1060, 330, 680, op=.35) + char("front", 1440, 290, 730) +
  '<div style="position:absolute;left:1080px;top:270px;font-size:30px;font-weight:800;color:var(--muted)">Бір жыл бұрын</div><div style="position:absolute;left:1520px;top:230px;font-size:34px;font-weight:800;color:var(--y)">Бүгін</div>'))
for q, pose, lay in [("Бір жыл бұрын<br/>қандай едіңіз?", "back", 1), ("Қазір нені<br/>үйрендіңіз?", "front", 0), ("Қандай қиындықты<br/>жеңдіңіз?", "rdiag", 0)]:
    ME.append((q.replace("<br/>", " "), QUOTE(q, pose, lay)))
ME.append(("Өзгерісті басқалардан емес, өз өміріңізден іздеңіз.",
  TC("Өзгеріс", f"Басқалардан емес —<br/>{Y('өз өміріңізден.')}", "ldiag", "r", 80)))
ME.append(("Екінші әдіс — әлеуметтік желідегі контентке назар аударыңыз.",
  stage("65%") + phone(1200, 40, -18, 4, APPBAR + post("arman_auto", "#ff6b5b", CAR, "Арман орындалды!", "2 450", 300) + post("biznes.guru", "#3ddc97", MONEY("5 000 000 ₸", "АЙЛЫҚ"), "Мен сияқты бол!", "48 200")) +
  CHIP("2-әдіс", 130, 230) + H(f"Контентке<br/>{Y('назар')}<br/>аударыңыз.", 96, 130, 330)))
ME.append(("Қандай парақшаларды көргеннен кейін өзіңізді нашар сезінесіз?",
  CARDCHAR(G(130, 220, 1080, ''.join(f'<div style="display:flex;align-items:center;justify-content:space-between;margin:18px 0;font-size:38px;font-weight:800"><span style="display:flex;align-items:center;gap:20px"><span style="width:56px;height:56px;border-radius:50%;background:{c};display:inline-block"></span>{n}</span><span style="color:{mc}">{m}</span></div>' for n, c, m, mc in [("biznes.guru", "#3ddc97", "Нашар ▼", "#ff6b5b"), ("arman_auto", "#ff6b5b", "Нашар ▼", "#ff6b5b"), ("kitap.club", "#7cc4ff", "Жақсы ▲", "#3ddc97"), ("sport.daily", "#ffd21f", "Жақсы ▲", "#3ddc97")]), pad=56), "rdiag", "r",
           K("Көргеннен кейінгі көңіл-күй", 130, 160))))
ME.append(("Егер белгілі бір контент сізге үнемі қысым тудырса, оны азайтыңыз немесе жазылымнан шығыңыз.",
  stage("35%") + phone(260, 40, 16, 4, '<div style="padding:120px 34px;color:#151830;text-align:center"><div style="width:180px;height:180px;border-radius:50%;margin:0 auto;background:#3ddc97;box-shadow:0 0 0 6px #fff,0 0 0 10px #ff6b5b"></div><div style="font-family:Unbounded;font-weight:900;font-size:36px;margin-top:30px">biznes.guru</div><div style="font-size:24px;color:#777;margin-top:10px">1,2 млн жазылушы</div><div style="margin-top:60px;padding:24px;border-radius:20px;background:#e9eaf2;font-weight:800;font-size:30px">Жазылымнан шығу</div><div style="margin-top:20px;padding:24px;border-radius:20px;border:3px solid #e3e5ef;font-weight:800;font-size:30px;color:#777">Үнсіз ету</div></div>') +
  K("Қысым болса", 1020, 330) + H(f"Азайтыңыз<br/>немесе<br/>{Y('шығыңыз.')}", 100, 1020, 390)))
ME.append(("Үшінші әдіс — өз жетістіктеріңізді жазып жүріңіз.",
  stage("72%") + CHIP("3-әдіс", 130, 230) + H(f"Жетістіктерді<br/>{Y('жазып')}<br/>жүріңіз.", 92, 130, 330) +
  '<div style="position:absolute;left:1100px;top:200px;perspective:1600px"><div style="width:620px;height:760px;border-radius:24px;transform:rotateY(-16deg) rotate(3deg);background:linear-gradient(#fbf7ee,#efe8d8);box-shadow:-14px 0 0 #c9a45a,0 60px 100px rgba(0,0,0,.55);padding:60px 56px;color:#14172d;background-image:repeating-linear-gradient(transparent 0 58px,rgba(20,23,45,.12) 58px 60px),linear-gradient(#fbf7ee,#efe8d8)"><div style="font-family:Unbounded;font-weight:900;font-size:40px">Жетістіктерім</div>' +
  ''.join(f'<div style="font-size:34px;font-weight:700;margin-top:30px">✓ {t}</div>' for t in ["Ағылшын: 30 сабақ", "Жобаны тапсырдым", "5 км жүгірдім"]) + '</div></div>'))
ME.append(("Кішкентай жетістік болса да, оны елемеңіз.",
  stage("50%") + '<div style="position:absolute;left:870px;top:200px;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff3a0,#ffd21f 45%,#c99a00);box-shadow:0 0 120px rgba(255,210,31,.6);"></div>' +
  H(f"Кішкентай жетістік те —<br/>{Y('жетістік.')}", 84, center=True, y=480)))
CL = ["Жаңа нәрсе үйрендіңіз бе?", "Маңызды жұмысты аяқтадыңыз ба?", "Қиын жағдайдан шықтыңыз ба?"]
for i, q in enumerate(CL):
    rows = ''.join(f'<div style="display:flex;align-items:center;gap:26px;margin:26px 0;font-size:46px;font-weight:800;opacity:{1 if j <= i else .3}"><span style="width:64px;height:64px;border-radius:16px;display:inline-flex;align-items:center;justify-content:center;background:{"#3ddc97" if j <= i else "rgba(255,255,255,.1)"};color:#fff;font-size:40px">{"✓" if j <= i else ""}</span>{t}</div>' for j, t in enumerate(CL))
    ME.append((q, CARDCHAR(G(130, 240, 1120, rows, pad=60, ry=8), ["front", "rdiag", "ldiag"][i], "r")))
ME.append(("Мұның бәрі — сіздің жеке дамуыңыз.",
  stage("50%") + '<svg style="position:absolute;left:160px;top:300px" width="1600" height="600"><path d="M20 560 C 400 540, 700 420, 1000 280 S 1450 60, 1580 30" fill="none" stroke="#3ddc97" stroke-width="20" stroke-linecap="round"/><circle cx="1580" cy="30" r="28" fill="#ffd21f"/></svg>' +
  H(f"Бұл — {Y('жеке дамуыңыз.')}", 84, center=True, y=110)))
ME.append(("Төртінші әдіс — әр адамның өмір жолы әртүрлі екенін қабылдаңыз.",
  stage("72%") + CHIP("4-әдіс", 130, 230) + H(f"Әр жол —<br/>{Y('әртүрлі.')}<br/>Қабылдаңыз.", 92, 130, 330) + char("back", 1380, 300, 730)))
ME.append(("Біреу ерте жетістікке жетеді.",
  stage("50%") + '<div style="position:absolute;left:200px;top:560px;width:1520px;height:8px;background:rgba(255,255,255,.25);border-radius:4px"></div>' +
  G(400, 400, 440, '<div class="h" style="font-size:50px;white-space:nowrap">22 жас ★</div>', pad=34) + '<div style="position:absolute;left:200px;top:600px;font-size:34px;font-weight:800;color:var(--muted)">Біреу</div>' + H(f"Біреу — {Y('ерте.')}", 100, center=True, y=760)))
ME.append(("Біреу кейінірек.",
  stage("50%") + '<div style="position:absolute;left:200px;top:560px;width:1520px;height:8px;background:rgba(255,255,255,.25);border-radius:4px"></div>' +
  G(400, 400, 440, '<div class="h" style="font-size:50px;white-space:nowrap;opacity:.5">22 жас ★</div>', pad=34) + G(1200, 400, 440, '<div class="h x3d" style="font-size:50px;white-space:nowrap">41 жас ★</div>', pad=34) + H(f"Біреу — {Y('кейінірек.')}", 100, center=True, y=760)))
ME.append(("Біреу бір салада мықты болса, екіншісі басқа салада қабілетті.",
  stage("50%") + H(f"Әркім — {Y('өз саласында.')}", 80, center=True, y=110) +
  ''.join(G(130 + (i % 3) * 570, 330 + (i // 3) * 270, 520, f'<div class="h" style="font-size:50px">{t}</div><div style="font-size:30px;font-weight:700;color:{c};margin-top:10px">{d}</div>', pad=44) for i, (t, d, c) in enumerate([("Бизнес", "★★★★★", "#ffd21f"), ("Спорт", "★★☆☆☆", "#7cc4ff"), ("Өнер", "★★★★☆", "#ff6b5b"), ("Ғылым", "★★★☆☆", "#3ddc97"), ("Отбасы", "★★★★★", "#b28cff"), ("Тіл", "★★☆☆☆", "#ffd21f")]))))
ME.append(("Өмір жарыс емес.",
  stage("50%", False) + '<svg style="position:absolute;left:0;top:0" width="1920" height="1080"><path d="M960 1080 C 960 880, 700 760, 480 600" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="130" stroke-linecap="round"/><path d="M960 1080 C 960 880, 1220 760, 1440 600" fill="none" stroke="rgba(255,210,31,.35)" stroke-width="130" stroke-linecap="round"/></svg>' +
  char("back", 900, 520, 520, pool=False) + H(f"Өмір — {Y('жарыс емес.')}", 110, center=True, y=140)))
ME.append(("Сіз міндетті түрде біреуден озып жүруге тиіс емессіз.",
  TC("Есте сақтаңыз", f"Ешкімді<br/>{Y('озу')} міндетті<br/>емес.", "front", "r", 100)))

OU = []  # outro
OU.append(("Сонымен, неге біз өзімізді басқалармен салыстырамыз?", CHAPTER("04", "Қорытынды", "Неге салыстырамыз?")))
OU.append(("Өйткені адам өзін және айналасындағы әлемді түсінуге тырысады.",
  TC("Өйткені", f"Адам әлемді<br/>{Y('түсінгісі')} келеді.", "rdiag", "r", 96)))
OU.append(("Салыстыру кейде бізге бағыт береді.",
  stage("50%") + '<div style="position:absolute;left:810px;top:150px;width:300px;height:300px;border-radius:50%;border:10px solid #3ddc97;box-shadow:0 0 80px rgba(61,220,151,.4)"><div style="position:absolute;left:135px;top:20px;width:20px;height:130px;background:#3ddc97;border-radius:10px;transform-origin:bottom;transform:rotate(35deg)"></div></div>' +
  H(f"Кейде — {Y('бағыт')} береді.", 100, center=True, y=580)))
OU.append(("Бірақ кейде өзіміздің құндылығымызды ұмытуға мәжбүр етеді.",
  stage("50%") + '<div style="position:absolute;left:810px;top:150px;width:300px;height:300px;border-radius:50%;border:10px solid #ff6b5b;box-shadow:0 0 80px rgba(255,107,91,.4)"><div class="h" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:150px;color:#ff6b5b">!</div></div>' +
  H(f"Кейде — {Y('құндылықты')} ұмыттырады.", 68, center=True, y=580)))
OU.append(("Есіңізде болсын:", stage("50%") + CHIP("Есіңізде болсын", 750, 420) + H(Y("Ең бастысы:"), 120, center=True, y=530)))
OU.append(("Сіз әлеуметтік желідегі басқа адамның ең жақсы сәттерін өз өміріңіздің қарапайым күндерімен салыстырып жүрген болуыңыз мүмкін.",
  stage("50%") + K("Олардың ең жақсы сәті", 170, 210) + K("Сіздің қарапайым күніңіз", 1060, 210) +
  f'<div style="position:absolute;left:170px;top:290px;width:700px;height:440px;border-radius:30px;overflow:hidden;container-type:inline-size;box-shadow:0 50px 100px rgba(0,0,0,.6),0 0 0 4px #ffd21f">{BEACH}</div>' +
  G(1060, 290, 700, ROW("#9aa0c3", "07:30 · Ояну", 40) + ROW("#9aa0c3", "09:00 · Жұмыс", 40) + ROW("#9aa0c3", "19:00 · Кептеліс", 40) + ROW("#9aa0c3", "22:00 · Шаршау", 40), pad=60) +
  '<div class="h x3d" style="position:absolute;left:890px;top:420px;font-size:140px">⇄</div>'))
OU.append(("Сондықтан өзгелердің өміріне қарап, өз өміріңізді бағаламаңыз.",
  TC("Сондықтан", f"Өз өміріңізді<br/>{Y('кемсітпеңіз.')}", "front", "r", 100)))
OU.append(("Біреудің жолы — оның жолы.",
  stage("50%", False) + '<svg style="position:absolute;left:0;top:0" width="1920" height="1080"><path d="M960 1080 C 960 880, 700 760, 480 600" fill="none" stroke="rgba(255,255,255,.3)" stroke-width="130" stroke-linecap="round"/><path d="M960 1080 C 960 880, 1220 760, 1440 600" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="130" stroke-linecap="round"/></svg>' +
  CHIP("Біреудің жолы", 330, 470, True) + H("Біреудің жолы — оның жолы.", 80, center=True, y=140)))
OU.append(("Ал сіздің жолыңыз — өзіңіздікі.",
  stage("50%", False) + '<svg style="position:absolute;left:0;top:0" width="1920" height="1080"><path d="M960 1080 C 960 880, 700 760, 480 600" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="130" stroke-linecap="round"/><path d="M960 1080 C 960 880, 1220 760, 1440 600" fill="none" stroke="rgba(255,210,31,.45)" stroke-width="130" stroke-linecap="round"/></svg>' +
  CHIP("Сіздің жолыңыз", 1240, 470) + char("back", 1010, 520, 520, pool=False) + H(f"Сіздің жолыңыз — {Y('өзіңіздікі.')}", 80, center=True, y=140)))
OU.append(("Өзіңізді басқалардан артық көрсетуге емес, кешегі өзіңізден жақсы болуға тырысыңыз.",
  stage("72%") + K("Мақсат", 130, 230) + H(f"Басқалардан емес —<br/>{Y('кешегі өзіңізден')}<br/>жақсы болыңыз.", 60, 130, 300) +
  char("front", 1060, 330, 680, op=.35) + char("front", 1440, 290, 730)))
OU.append(("Егер бұл видео сізге ой салса, пікірге жазыңыз:",
  CARDCHAR(G(130, 300, 1080, '<div style="display:flex;align-items:center;gap:26px"><div style="width:84px;height:84px;border-radius:50%;background:#2b3060;overflow:hidden;position:relative"><img src="assets/char/face.png" style="position:absolute;left:4px;top:6px;width:76px"/></div><div style="font-size:40px;font-weight:700;color:var(--muted)">Пікір қалдырыңыз...</div></div><div style="margin-top:30px;height:4px;background:rgba(255,255,255,.15)"></div><div style="display:flex;justify-content:flex-end;margin-top:26px"><div class="chip">Жіберу</div></div>', pad=56), "rdiag", "r",
           H(f"Пікірге {Y('жазыңыз')}", 90, 130, 140))))
OU.append(("Сіз өзіңізді басқалармен жиі салыстырасыз ба?",
  stage("50%") + H(f"Сіз өзіңізді басқалармен<br/>{Y('жиі салыстырасыз ба?')}", 84, center=True, y=330) + CHIP("Иә", 720, 680, True) + CHIP("Кейде", 860, 680, True) + CHIP("Жоқ", 1060, 680, True)))
OU.append(("ПСИХОКОД арнасына жазылыңыз.",
  stage("50%") + '<div style="position:absolute;left:660px;top:200px;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(255,210,31,.25),transparent 65%)"></div>' +
  '<div style="position:absolute;left:810px;top:220px;width:300px;height:300px;border-radius:50%;background:var(--y);overflow:hidden;box-shadow:0 0 0 8px #fff,0 40px 80px rgba(0,0,0,.5)"><img src="assets/char/face.png" style="position:absolute;left:20px;top:26px;width:260px"/></div>' +
  H("ПСИХОКОД", 110, center=True, y=570, cls="x3d") +
  '<div style="position:absolute;left:760px;top:760px;width:400px;padding:28px;border-radius:24px;background:linear-gradient(180deg,#ff6b5b,#e8453a);text-align:center;font-family:Unbounded;font-weight:900;font-size:44px;color:#fff;box-shadow:inset 0 2px 0 rgba(255,255,255,.4),0 30px 60px rgba(0,0,0,.5)">ЖАЗЫЛУ</div>'))
OU.append(("Біз адам психологиясының қызықты құпияларын бірге зерттейміз.",
  TC("ПСИХОКОД", f"Психологияның<br/>{Y('құпияларын')}<br/>бірге зерттейміз.", "ldiag", "r", 88)))
OU.append(("Келесі кездескенше!",
  stage("50%") + char("front", 830, 260, 760) + H(f"Келесі {Y('кездескенше!')}", 100, center=True, y=100)))

ACTS = [("intro", F_INTRO), ("theory", TH), ("social", SO), ("methods", ME), ("outro", OU)]

# ---------------- layer splitter ----------------
class Splitter(HTMLParser):
    VOID = {"img", "br", "hr", "input", "meta", "link", "source", "polyline", "circle", "rect", "line", "path", "polygon", "ellipse", "stop"}
    def __init__(self, src):
        super().__init__(convert_charrefs=False); self.src = src; self.depth = 0; self.starts = []; self.parts = []
        self.lines = [0]
        for ln in src.split("\n"): self.lines.append(self.lines[-1] + len(ln) + 1)
    def off(self):
        l, c = self.getpos(); return self.lines[l - 1] + c
    def handle_starttag(self, tag, a):
        if self.depth == 0: self.cur = self.off()
        if tag in self.VOID:
            if self.depth == 0: self.parts.append(self.src[self.cur:self.off() + len(self.get_starttag_text())])
            return
        self.depth += 1
    def handle_startendtag(self, tag, a):
        if self.depth == 0: self.parts.append(self.get_starttag_text())
    def handle_endtag(self, tag):
        if tag in self.VOID: return
        self.depth -= 1
        if self.depth == 0:
            end = self.off(); end = self.src.index(">", end) + 1
            self.parts.append(self.src[self.cur:end])

def layers(html):
    sp = Splitter(html); sp.feed(html)
    assert "".join(sp.parts).replace(" ", "") .__len__() > 0
    out = []
    for p in sp.parts:
        if 'class="stage"' in p or 'class="floor"' in p: a = "s"
        elif "assets/char/" in p and 'class="char"' in p: a = "c"
        elif 'class="pool"' in p or 'class="cshadow"' in p: a = "f"
        elif "glass" in p or "phone" in p or "perspective" in p or "chip" in p or "<svg" in p: a = "p"
        else: a = "u"
        out.append(f'<div class="L" data-a="{a}">{p}</div>')
    return "".join(out)

def words(t): return len(re.findall(r"[\wӘәҒғҚқҢңӨөҰұҮүҺһІі]+", t))
import subprocess
VO_LEAD, VO_TAIL = 0.15, 0.45
def vo_len(sid):
    f = f"assets/voice/{sid}.mp3"
    if not os.path.exists(f): return None
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode().strip())
def dur(t, sid=None):
    v = vo_len(sid) if sid else None
    if v: return round(max(2.0, VO_LEAD + v + VO_TAIL), 2)
    return round(max(2.4, words(t) / 2.3 + 0.8), 2)

SCENE_CSS = ".L{position:absolute;inset:0}.cam{position:absolute;inset:0}"
TL_JS = """
const tl = gsap.timeline({ paused: true });
FR.forEach(([id, s, d]) => {
  tl.fromTo('#' + id + ' .cam', { scale: 1 }, { scale: 1.035, duration: d, ease: 'none' }, s);
  let k = 0;
  document.querySelectorAll('#' + id + ' .L').forEach((el) => {
    const t = el.dataset.a; if (t === 's') return;
    const at = s + 0.06 + k * 0.1; k++;
    if (t === 'c') tl.fromTo(el, { opacity: 0, y: 90 }, { opacity: 1, y: 0, duration: 0.75, ease: 'back.out(1.5)' }, at);
    else if (t === 'p') tl.fromTo(el, { opacity: 0, y: 50, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.7, ease: 'power3.out' }, at);
    else if (t === 'f') tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.6, ease: 'none' }, at);
    else tl.fromTo(el, { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out' }, at);
  });
});
"""
import shutil
shutil.rmtree("compositions", ignore_errors=True); os.makedirs("compositions/scenes", exist_ok=True)
hosts, t0, n, plan = "", 0.0, 0, []
for name, frames in ACTS:
    for sent, html in frames:
        n += 1; sid = f"s{n:03d}"; d = dur(sent, sid)
        open(f"compositions/scenes/{sid}.html", "w").write(
            f'<template>\n<style>{CSS.replace("#root{", "#root-unused{")}{SCENE_CSS}#root{{position:absolute;inset:0;font-family:Manrope,sans-serif;color:var(--ivory);background:var(--bg);overflow:hidden}}</style>\n'
            f'<div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080">\n'
            f'<div id="{sid}-frame" class="clip frame" data-start="0" data-duration="{d}" data-track-index="0"><div class="cam">{layers(html)}</div><div class="vig"></div></div>\n</div>\n'
            f'<!-- {sent} -->\n<script>\nconst FR = {json.dumps([[sid + "-frame", 0, d]])};\n{TL_JS}window.__timelines["{sid}"] = tl;\n</script>\n</template>\n')
        hosts += (f'<div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/scenes/{sid}.html" data-start="{t0:.2f}" data-duration="{d}" '
                  f'data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>\n')
        v = vo_len(sid)
        if v:
            hosts += (f'<audio id="vo-{sid}" class="clip" src="assets/voice/{sid}.mp3" data-start="{t0 + VO_LEAD:.2f}" data-duration="{v:.2f}" '
                      f'data-track-index="2" data-volume="1"></audio>\n')
        plan.append({"n": n, "id": sid, "act": name, "start": round(t0, 2), "dur": d, "text": sent, "voice": v})
        t0 = round(t0 + d, 2)

open("index.html", "w").write(f'''<!doctype html>
<html lang="kk">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=1920, height=1080"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1920px;height:1080px;overflow:hidden;background:#14172d}}
#root{{width:100%;height:100%;position:relative}}</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{t0}" data-width="1920" data-height="1080">
{hosts}</div>
<script>window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = gsap.timeline({{ paused: true }});</script>
</body></html>
''')
json.dump(plan, open("boards/plan.json", "w"), ensure_ascii=False, indent=1)
print(n, "frames,", t0, "s")
