import sys
proj = sys.argv[1]
fonts = open(f"{proj}/assets/fonts/fonts.css").read()

CSS = """
:root{--bg:#14172d;--bg2:#1d2142;--y:#ffd21f;--y2:#ffb800;--coral:#ff6b5b;--mint:#3ddc97;--sky:#7cc4ff;--ivory:#f5f1e8;--muted:#9aa0c3}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;background:var(--bg)}
#root{width:100%;height:100%;position:relative;font-family:'Manrope',sans-serif;color:var(--ivory)}
.frame{position:absolute;inset:0;overflow:hidden;background:var(--bg)}
/* one-colour studio: same hue, light only */
.stage{position:absolute;inset:0;background:
 radial-gradient(ellipse 60% 70% at var(--lx,70%) 38%, rgba(98,110,200,.42), transparent 70%),
 linear-gradient(180deg, transparent 0 66%, rgba(0,0,0,.28) 66.2%, rgba(0,0,0,.05) 100%)}
.floor{position:absolute;left:-10%;right:-10%;top:66%;bottom:-20%;transform:perspective(900px) rotateX(62deg);transform-origin:top;
 background-image:linear-gradient(rgba(140,150,255,.10) 2px,transparent 2px),linear-gradient(90deg,rgba(140,150,255,.10) 2px,transparent 2px);background-size:120px 120px;
 -webkit-mask-image:linear-gradient(#000,transparent 75%)}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse 85% 80% at 50% 45%,transparent 55%,rgba(0,0,0,.55));pointer-events:none}
.pool{position:absolute;border-radius:50%;background:radial-gradient(ellipse at center,rgba(255,210,31,.28),rgba(255,210,31,0) 70%)}
.cshadow{position:absolute;border-radius:50%;background:radial-gradient(ellipse at center,rgba(0,0,0,.65),rgba(0,0,0,0) 70%)}
.char{position:absolute;filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))}
.h{font-family:'Unbounded',sans-serif;font-weight:900;letter-spacing:-.02em;line-height:1.05}
.x3d{color:var(--y);text-shadow:0 1px 0 #f0bf00,0 2px 0 #e3b200,0 3px 0 #d6a600,0 4px 0 #c99a00,0 5px 0 #bb8e00,0 6px 0 #ad8200,0 8px 2px rgba(0,0,0,.35),0 24px 40px rgba(0,0,0,.55)}
.w3d{color:#fff;text-shadow:0 1px 0 #d9dcf0,0 2px 0 #c3c7e3,0 3px 0 #aeb3d6,0 4px 0 #989ec9,0 5px 0 #8389bb,0 8px 2px rgba(0,0,0,.35),0 24px 40px rgba(0,0,0,.55)}
.glass{position:absolute;background:linear-gradient(145deg,rgba(255,255,255,.14),rgba(255,255,255,.04));border:1.5px solid rgba(255,255,255,.18);border-radius:32px;
 box-shadow:inset 0 1px 0 rgba(255,255,255,.25),0 40px 80px rgba(0,0,0,.45);backdrop-filter:blur(18px)}
.chip{display:inline-flex;align-items:center;gap:14px;padding:14px 28px;border-radius:999px;font-weight:800;font-size:30px;letter-spacing:.06em;text-transform:uppercase;
 background:linear-gradient(180deg,#ffe066,#ffc800);color:#1a1a1a;box-shadow:inset 0 2px 0 rgba(255,255,255,.6),inset 0 -4px 0 rgba(0,0,0,.18),0 18px 30px rgba(0,0,0,.4)}
.chip.dark{background:linear-gradient(180deg,#2b3060,#1f2347);color:var(--ivory);box-shadow:inset 0 1px 0 rgba(255,255,255,.2),0 18px 30px rgba(0,0,0,.4)}
.cap{position:absolute;left:120px;bottom:110px}
.cap .k{font-size:28px;font-weight:800;letter-spacing:.18em;color:var(--muted);text-transform:uppercase;margin-bottom:18px}
/* 3D phone */
.p3d{position:absolute;perspective:2200px}
.phone{width:500px;height:1000px;border-radius:70px;padding:18px;background:linear-gradient(135deg,#3b4170,#14172d 40%,#2a2f58);
 box-shadow:inset 0 0 0 3px rgba(255,255,255,.18),18px 0 0 #0b0d1c,0 60px 120px rgba(0,0,0,.6),0 0 160px rgba(124,196,255,.25)}
.scr{width:100%;height:100%;border-radius:54px;overflow:hidden;position:relative;background:#f4f5fb}
.scr::after{content:'';position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.35),rgba(255,255,255,0) 35%);pointer-events:none}
.notch{position:absolute;left:50%;top:16px;width:130px;height:36px;margin-left:-65px;background:#0b0d1c;border-radius:20px;z-index:3}
.post{margin:16px;border-radius:26px;background:#fff;box-shadow:0 10px 24px rgba(20,23,45,.12);overflow:hidden;color:#151830}
.post .top{display:flex;align-items:center;gap:14px;padding:14px 18px;font-weight:800;font-size:24px}
.av{width:46px;height:46px;border-radius:50%;box-shadow:0 0 0 3px #fff,0 0 0 6px #ff6b5b}
.pic{position:relative;overflow:hidden}
.post .cp{padding:12px 18px 18px;font-size:23px;font-weight:700}
.heart{color:#ff4d6d}
.badge{position:absolute;padding:16px 26px;border-radius:24px;font-weight:800;font-size:34px;background:#fff;color:#151830;box-shadow:0 24px 50px rgba(0,0,0,.45)}
.coin{position:absolute;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff4b0,#ffd21f 35%,#d99a00 75%,#a26f00);box-shadow:0 10px 0 #8a5d00,0 30px 40px rgba(0,0,0,.45);
 display:flex;align-items:center;justify-content:center;font-family:Unbounded;font-weight:900;color:#9a6a00}
.q{position:absolute;font-family:Unbounded;font-weight:900}
"""

# ---------- reusable illustrations (pseudo-3D SVG) ----------
CAR = """<svg viewBox="0 0 600 300" width="100%" height="100%"><defs>
<linearGradient id="sky1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fd3ff"/><stop offset="1" stop-color="#eaf5ff"/></linearGradient>
<linearGradient id="body1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff8a7a"/><stop offset=".45" stop-color="#ff4d3d"/><stop offset="1" stop-color="#a51d14"/></linearGradient>
<linearGradient id="glass1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e8f6ff"/><stop offset="1" stop-color="#5b7fa8"/></linearGradient>
<radialGradient id="tyre"><stop offset=".45" stop-color="#d9dde8"/><stop offset=".55" stop-color="#2a2a2e"/><stop offset="1" stop-color="#0d0d10"/></radialGradient></defs>
<rect width="600" height="300" fill="url(#sky1)"/><rect y="230" width="600" height="70" fill="#c9cfdc"/>
<ellipse cx="300" cy="248" rx="250" ry="18" fill="rgba(0,0,0,.35)"/>
<path d="M60 220 Q55 175 95 165 L170 155 Q215 105 290 100 L380 100 Q440 104 485 150 L530 160 Q560 168 560 205 L556 222 Z" fill="url(#body1)"/>
<path d="M190 155 Q225 118 290 114 L300 114 L300 155 Z M315 114 L375 114 Q420 118 455 152 L315 155 Z" fill="url(#glass1)"/>
<path d="M80 180 L540 178" stroke="rgba(255,255,255,.55)" stroke-width="5"/>
<circle cx="160" cy="222" r="38" fill="url(#tyre)"/><circle cx="460" cy="222" r="38" fill="url(#tyre)"/>
<rect x="520" y="170" width="30" height="12" rx="6" fill="#fff7c2"/></svg>"""

BEACH = """<svg viewBox="0 0 600 300" width="100%" height="100%"><defs>
<linearGradient id="bs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff9a6b"/><stop offset=".55" stop-color="#ffd59a"/><stop offset="1" stop-color="#ffe9c4"/></linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1fb5d6"/><stop offset="1" stop-color="#0a6f9e"/></linearGradient>
<radialGradient id="sun"><stop offset="0" stop-color="#fff6c8"/><stop offset=".5" stop-color="#ffd21f"/><stop offset="1" stop-color="rgba(255,210,31,0)"/></radialGradient></defs>
<rect width="600" height="300" fill="url(#bs)"/><circle cx="420" cy="150" r="110" fill="url(#sun)"/>
<rect y="170" width="600" height="80" fill="url(#sea)"/><path d="M0 250 Q300 225 600 250 L600 300 L0 300Z" fill="#f3dca8"/>
<path d="M120 300 Q125 210 165 140" stroke="#5a3a1c" stroke-width="14" fill="none"/>
<g fill="#1f8f55"><path d="M165 140 Q110 115 60 140 Q115 128 165 146Z"/><path d="M165 140 Q215 100 270 118 Q215 120 168 146Z"/><path d="M165 140 Q140 85 95 78 Q145 100 162 146Z"/><path d="M165 140 Q215 145 240 190 Q205 158 163 146Z"/></g></svg>"""

HOUSE = """<svg viewBox="0 0 600 300" width="100%" height="100%"><defs>
<linearGradient id="hs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a8d8ff"/><stop offset="1" stop-color="#f0f8ff"/></linearGradient></defs>
<rect width="600" height="300" fill="url(#hs)"/><rect y="235" width="600" height="65" fill="#7cc77a"/>
<ellipse cx="300" cy="250" rx="220" ry="16" fill="rgba(0,0,0,.25)"/>
<polygon points="150,140 300,90 300,245 150,245" fill="#f5efe4"/><polygon points="300,90 450,140 450,245 300,245" fill="#d9cdb8"/>
<polygon points="130,145 300,60 310,95 150,150" fill="#3b4170"/><polygon points="300,60 470,145 450,150 300,95" fill="#262a52"/>
<rect x="190" y="160" width="60" height="50" rx="4" fill="#ffd77a"/><rect x="340" y="160" width="60" height="50" rx="4" fill="#e9b94f"/>
<rect x="265" y="185" width="34" height="60" fill="#8a5a2b"/></svg>"""

def stage(lx="70%", grid=True):
    return f'<div class="stage" style="--lx:{lx}"></div>' + ('<div class="floor"></div>' if grid else '')

def char(src, x, y, h, flip=False, pool=True, op=1):
    w = int(h * 0.36)
    s = ''
    if pool:
        s += f'<div class="pool" style="left:{x-w*0.9:.0f}px;top:{y+h-80}px;width:{w*2.8:.0f}px;height:160px"></div>'
        s += f'<div class="cshadow" style="left:{x-w*0.25:.0f}px;top:{y+h-30}px;width:{w*1.5:.0f}px;height:50px"></div>'
    tr = 'transform:scaleX(-1);' if flip else ''
    s += f'<img class="char" src="assets/char/{src}.png" style="left:{x}px;top:{y}px;height:{h}px;opacity:{op};{tr}"/>'
    return s

def phone(x, y, ry, rx, inner, scale=1):
    return f'''<div class="p3d" style="left:{x}px;top:{y}px"><div style="transform:rotateY({ry}deg) rotateX({rx}deg) scale({scale});transform-style:preserve-3d">
<div class="phone"><div class="scr"><div class="notch"></div>{inner}</div></div></div></div>'''

def post(user, color, pic, caption, likes, ph=300):
    return f'''<div class="post"><div class="top"><div class="av" style="background:{color}"></div>{user}</div>
<div class="pic" style="height:{ph}px">{pic}</div><div class="cp">{caption} <span class="heart">♥ {likes}</span></div></div>'''

def cap(kicker, html, size=96, cls="w3d"):
    return f'<div class="cap"><div class="k">{kicker}</div><div class="h {cls}" style="font-size:{size}px">{html}</div></div>'

APPBAR = '<div style="padding:66px 26px 6px;display:flex;justify-content:space-between;align-items:center;color:#151830"><b style="font-family:Unbounded;font-size:30px">лента</b><span style="font-size:26px">♡ ✉</span></div>'

F = []
# 01
F.append(("Елестетіп көріңіз...", stage("62%", False) +
  '<div class="pool" style="left:820px;top:120px;width:900px;height:900px;background:radial-gradient(circle,rgba(124,196,255,.25),transparent 65%)"></div>' +
  '<img class="char" src="assets/char/face.png" style="left:1020px;top:250px;height:830px"/>' +
  '<div style="position:absolute;left:120px;top:330px"><div class="chip dark" style="margin-bottom:40px">ПСИХОКОД</div><div class="h w3d" style="font-size:120px">Елестетіп<br/><span class="x3d">көріңіз...</span></div></div>'))
# 02
F.append(("Сіз кешке үйде отырсыз.", stage("68%") +
  '<div class="glass" style="left:1180px;top:110px;width:520px;height:400px;border-radius:24px;background:linear-gradient(160deg,#28306a,#10132a);overflow:hidden"><div style="position:absolute;left:300px;top:70px;width:130px;height:130px;border-radius:50%;background:#fff3c4;box-shadow:0 0 90px rgba(255,243,196,.6)"></div><div style="position:absolute;left:340px;top:50px;width:130px;height:130px;border-radius:50%;background:#1a1f48"></div><div style="position:absolute;left:258px;top:0;width:6px;height:400px;background:rgba(255,255,255,.2)"></div><div style="position:absolute;left:0;top:198px;width:520px;height:6px;background:rgba(255,255,255,.2)"></div></div>' +
  '<div style="position:absolute;left:880px;top:180px;width:16px;height:520px;background:linear-gradient(90deg,#2a2f58,#4a5190)"></div><div style="position:absolute;left:800px;top:110px;width:180px;height:110px;border-radius:90px 90px 10px 10px;background:linear-gradient(#ffe7a0,#ffc94a);box-shadow:0 0 140px 50px rgba(255,200,80,.35)"></div>' +
  char("front", 1330, 330, 700) +
  cap("21:00 · үй", 'Кеш.<br/><span class="x3d">Үйдесіз.</span>', 120)))
# 03
day = ''.join(f'<div style="display:flex;align-items:center;gap:22px;margin:18px 0"><div style="width:22px;height:22px;border-radius:50%;background:{c};box-shadow:0 0 18px {c}"></div><div style="font-size:34px;font-weight:700;width:120px;color:var(--muted)">{t}</div><div style="font-size:38px;font-weight:800">{l}</div></div>' for t,l,c in [("09:00","Жұмыс","#7cc4ff"),("13:00","Түскі ас","#3ddc97"),("18:00","Жол","#ff6b5b"),("20:30","Үй","#ffd21f")])
F.append(("Күніңіз әдеттегідей өтті.", stage("72%") +
  f'<div style="position:absolute;left:150px;top:150px;perspective:1800px"><div class="glass" style="position:relative;width:720px;padding:50px 60px;transform:rotateY(14deg) rotateX(4deg)"><div class="k" style="font-size:26px;letter-spacing:.18em;color:var(--muted);font-weight:800">БҮГІН</div>{day}</div></div>' +
  char("ldiag", 1250, 300, 720) +
  '<div class="h w3d" style="position:absolute;left:150px;top:840px;font-size:84px">Әдеттегі <span class="x3d">күн.</span></div>'))
# 04
apps = ''.join(f'<div style="width:96px;height:96px;border-radius:26px;background:{c};box-shadow:0 10px 18px rgba(0,0,0,.18)"></div>' for c in ["linear-gradient(135deg,#ff6b5b,#ff2f7a)","linear-gradient(135deg,#7cc4ff,#4a6cff)","linear-gradient(135deg,#3ddc97,#0fae6c)","linear-gradient(135deg,#ffd21f,#ff9d00)","linear-gradient(135deg,#b28cff,#6a4cff)","linear-gradient(135deg,#ff9a6b,#ff5a4e)","linear-gradient(135deg,#5ee1ff,#00a3c4)","linear-gradient(135deg,#ffe066,#f2b800)"])
F.append(("Телефоныңызды алып, әлеуметтік желіні ашасыз.", stage("55%") +
  phone(700, 40, -22, 6, f'<div style="padding:150px 40px;display:grid;grid-template-columns:repeat(3,96px);gap:46px;justify-content:center">{apps}</div><div style="position:absolute;left:50%;top:150px;margin-left:-160px;width:96px;height:96px;border-radius:26px;box-shadow:0 0 0 8px #ffd21f,0 0 60px #ffd21f"></div>') +
  '<img class="char" src="assets/char/face.png" style="left:120px;top:420px;height:660px;transform:scaleX(-1)"/>' +
  '<div style="position:absolute;left:1250px;top:330px"><div class="chip" style="margin-bottom:30px">21:03</div><div class="h w3d" style="font-size:84px">Әлеуметтік<br/><span class="x3d">желі.</span></div></div>'))
# 05-08 feed, one post each
def feedframe(title_html, kicker, user, color, pic, caption, likes, badges, lx="35%"):
    return stage(lx) + phone(260, 40, 16, 4, APPBAR + post(user, color, pic, caption, likes, 420) + '<div class="post" style="height:300px;opacity:.6"></div>') + badges + \
      f'<div style="position:absolute;left:1020px;top:300px"><div class="k" style="font-size:28px;letter-spacing:.18em;color:var(--muted);font-weight:800;margin-bottom:24px">{kicker}</div><div class="h w3d" style="font-size:104px">{title_html}</div></div>'
F.append(("Бірінші адамның жаңа көлік алғанын көресіз.", feedframe('Жаңа<br/><span class="x3d">көлік.</span>', "1-пост", "arman_auto", "#ff6b5b", CAR, "Арман орындалды!", "2 450",
  '<div class="badge" style="left:720px;top:620px;transform:rotate(6deg)"><span class="heart">♥</span> +2 450</div>')))
F.append(("Екіншісі шетелде демалып жүр.", feedframe('Шетелде<br/><span class="x3d">демалыс.</span>', "2-пост", "aru.travels", "#7cc4ff", BEACH, "Мальдив, 7-күн", "5 120",
  '<div class="badge" style="left:700px;top:170px;transform:rotate(-6deg)">✈ Мальдив</div>')))
F.append(("Үшіншісі әдемі үй сатып алған.", feedframe('Әдемі<br/><span class="x3d">үй.</span>', "3-пост", "dana.home", "#3ddc97", HOUSE, "Өз үйіміз!", "8 900",
  '<div class="badge" style="left:730px;top:640px;transform:rotate(5deg)">🔑 Кілт</div>'.replace('🔑 ',''))))
coins = ''.join(f'<div class="coin" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;font-size:{s//3}px;transform:rotate({r}deg)">₸</div>' for x,y,s,r in [(820,180,150,-14),(880,700,120,12),(1700,180,110,8),(1740,760,170,-10),(1480,860,90,20)])
F.append(("Ал тағы біреуі небәрі 25 жасында миллионер болыпты.", stage("50%", False) +
  phone(260, 40, 16, 4, APPBAR + '<div class="post"><div class="top"><div class="av" style="background:#ffd21f"></div>dauren_25</div><div style="height:420px;background:linear-gradient(160deg,#1d2142,#3b4170);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff"><div style="font-family:Unbounded;font-weight:900;font-size:120px;color:#ffd21f">25</div><div style="font-family:Unbounded;font-weight:700;font-size:34px">жас · миллионер</div></div><div class="cp">Бәрі мүмкін! <span class="heart">♥ 21 300</span></div></div>') + coins +
  '<div style="position:absolute;left:1020px;top:330px"><div class="k" style="font-size:28px;letter-spacing:.18em;color:var(--muted);font-weight:800;margin-bottom:24px">4-пост</div><div class="h w3d" style="font-size:104px"><span class="x3d">25</span> жаста<br/>миллионер.</div></div>'))
# 09 strange feeling
F.append(("Сіз олардың суреттерін қарап отырып, біртүрлі сезімге бөленесіз.", stage("50%", False) +
  ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{int(w*0.62)}px;border-radius:24px;overflow:hidden;opacity:{o};filter:blur({b}px);transform:rotate({r}deg);box-shadow:0 30px 60px rgba(0,0,0,.5)">{p}</div>' for x,y,w,o,b,r,p in [(120,130,460,.85,0,-8,CAR),(1380,110,420,.8,2,7,BEACH),(140,640,380,.6,4,6,HOUSE),(1420,640,400,.6,3,-6,CAR)]) +
  '<div class="pool" style="left:560px;top:150px;width:800px;height:800px;background:radial-gradient(circle,rgba(124,196,255,.22),transparent 65%)"></div>' +
  '<img class="char" src="assets/char/face.png" style="left:720px;top:290px;height:790px"/>' +
  '<div class="h w3d" style="position:absolute;left:0;right:0;top:110px;text-align:center;font-size:76px">Біртүрлі <span class="x3d">сезім...</span></div>'))
# 10-12 thoughts
def thought(q, pose, layout):
    if layout == 0:
        return stage("75%") + char(pose, 1330, 250, 780) + f'<div class="glass" style="left:130px;top:250px;width:1080px;padding:60px 70px"><div class="q x3d" style="position:relative;font-size:150px;line-height:1;height:90px;margin-top:-20px">“</div><div class="h" style="font-size:78px;font-weight:700">{q}</div></div>'
    if layout == 1:
        return stage("28%") + char(pose, 280, 250, 780, flip=True) + f'<div class="glass" style="left:760px;top:220px;width:1030px;padding:60px 70px"><div class="q x3d" style="position:relative;font-size:150px;line-height:1;height:90px;margin-top:-20px">“</div><div class="h" style="font-size:78px;font-weight:700">{q}</div></div>'
    return stage("50%", False) + '<img class="char" src="assets/char/face.png" style="left:1180px;top:330px;height:750px"/>' + f'<div class="glass" style="left:130px;top:200px;width:1050px;padding:60px 70px;background:linear-gradient(145deg,rgba(255,210,31,.95),rgba(255,184,0,.9));color:#1a1a1a"><div class="q" style="position:relative;font-size:150px;line-height:1;height:90px;margin-top:-20px;color:#1a1a1a">“</div><div class="h" style="font-size:74px;font-weight:700">{q}</div></div>'
F.append(("«Мен неге әлі осындай жетістікке жетпедім?»", thought("Мен неге әлі осындай жетістікке <span style='color:var(--y)'>жетпедім?</span>", "rdiag", 0)))
F.append(("«Менің өмірім неге басқалардікіндей емес?»", thought("Менің өмірім неге <span style='color:var(--y)'>басқалардікіндей</span> емес?", "ldiag", 1)))
F.append(("«Мүмкін, мен бір нәрсені дұрыс істемей жүрген шығармын?»", thought("Мүмкін, мен бір нәрсені дұрыс істемей жүрген шығармын?", "face", 2)))
# 13-14 mood clock
def clock(t, label, col, mood):
    return f'<div style="position:absolute;left:140px;top:200px;perspective:1800px"><div class="glass" style="position:relative;width:760px;padding:56px 64px;transform:rotateY(12deg)"><div class="h" style="font-size:170px;color:#fff">{t}</div><div style="display:flex;align-items:center;gap:20px;margin-top:26px"><div style="width:26px;height:26px;border-radius:50%;background:{col};box-shadow:0 0 24px {col}"></div><div style="font-size:44px;font-weight:800">{label}</div></div><div style="margin-top:40px;height:22px;border-radius:11px;background:rgba(255,255,255,.1);overflow:hidden"><div style="width:{mood}%;height:100%;background:linear-gradient(90deg,{col},{col}aa);border-radius:11px"></div></div><div style="font-size:26px;color:var(--muted);font-weight:700;margin-top:14px;letter-spacing:.14em">КӨҢІЛ-КҮЙ</div></div></div>'
F.append(("Бірнеше минут бұрын бәрі жақсы еді.", stage("72%") + clock("21:00", "Бәрі жақсы", "#3ddc97", 86) + char("front", 1300, 320, 710)))
F.append(("Бірақ енді өз өміріңіз көңіліңізден шықпай қалғандай.", stage("72%") + clock("21:07", "Көңіл толмайды", "#ff6b5b", 24) + char("back", 1300, 320, 710)))
# 15-16 strangers
def strangers(locked):
    s = ''
    for i,(x,r,c,n) in enumerate([(170,-6,"#ff6b5b","arman_auto"),(700,0,"#7cc4ff","aru.travels"),(1230,6,"#ffd21f","dauren_25")]):
        body = ('<div style="font-size:120px;line-height:1">🔒</div>'.replace('🔒','<svg width="110" height="130" viewBox="0 0 110 130"><path d="M25 60 V40 a30 30 0 0 1 60 0 V60" stroke="#ffd21f" stroke-width="12" fill="none"/><rect x="10" y="58" width="90" height="68" rx="16" fill="#ffd21f"/><circle cx="55" cy="90" r="10" fill="#14172d"/></svg>')
                if locked else f'<div style="width:170px;height:170px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#5a6199,#262b55);display:flex;align-items:center;justify-content:center;font-family:Unbounded;font-weight:900;font-size:90px;color:{c};box-shadow:0 0 0 6px {c}">?</div>')
        sub = 'Шынайы өмірі жабық' if locked else 'Таныс емес'
        s += f'<div style="position:absolute;left:{x}px;top:200px;perspective:1600px"><div class="glass" style="position:relative;width:500px;height:520px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;transform:rotateY({-r*2}deg) rotate({r/2}deg)">{body}<div style="font-size:38px;font-weight:800">{n}</div><div style="font-size:28px;color:var(--muted);font-weight:700">{sub}</div></div></div>'
    return s
F.append(("Бір қызығы, сіз ол адамдарды мүлде танымайсыз.", stage("50%") + strangers(False) + '<div class="h w3d" style="position:absolute;left:0;right:0;top:820px;text-align:center;font-size:86px">Мүлде <span class="x3d">танымайсыз.</span></div>'))
F.append(("Олардың қалай өмір сүретінін де білмейсіз.", stage("50%") + strangers(True) + '<div class="h w3d" style="position:absolute;left:0;right:0;top:820px;text-align:center;font-size:74px">Қалай өмір сүретінін <span class="x3d">білмейсіз.</span></div>'))
# 17 why
F.append(("Сонда неге олардың өмірі сіздің өзіңізге деген көзқарасыңызды өзгерте алады?", stage("50%") +
  ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:300px;height:186px;border-radius:20px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.5);transform:rotate({r}deg)">{p}</div>' for x,y,r,p in [(170,170,-8,CAR),(170,560,6,BEACH),(1450,170,8,HOUSE),(1450,560,-6,CAR)]) +
  '<svg style="position:absolute;left:0;top:0" width="1920" height="1080"><g stroke="#ffd21f" stroke-width="5" stroke-dasharray="4 16" stroke-linecap="round" fill="none" opacity=".8"><path d="M470 260 Q700 300 840 480"/><path d="M470 650 Q650 640 840 600"/><path d="M1450 260 Q1220 300 1080 480"/><path d="M1450 650 Q1270 640 1080 600"/></g></svg>' +
  char("front", 830, 300, 690) +
  '<div class="q x3d" style="left:1030px;top:150px;font-size:220px">?</div>' +
  '<div class="h w3d" style="position:absolute;left:0;right:0;top:60px;text-align:center;font-size:64px">Неге <span class="x3d">олардың</span> өмірі сізді өзгертеді?</div>'))
# 18 title
F.append(("Бүгін біз ... әлеуметтік салыстыру туралы сөйлесеміз.", stage("72%") +
  '<div style="position:absolute;left:130px;top:220px"><div class="chip" style="margin-bottom:46px">ПСИХОКОД · Бүгінгі тақырып</div><div class="h w3d" style="font-size:134px">Әлеуметтік</div><div class="h x3d" style="font-size:134px">салыстыру</div><div style="margin-top:46px;font-size:40px;font-weight:700;color:var(--muted)">Неге біз өзімізді басқалармен салыстырамыз?</div></div>' +
  char("front", 1400, 260, 760)))

D = 3
body = ''
for i, (txt, html) in enumerate(F):
    body += f'<div id="f{i+1:02d}" class="clip frame" data-start="{i*D}" data-duration="{D}" data-track-index="0">{html}<div class="vig"></div></div>\n'
doc = f'''<!doctype html><html lang="kk"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1920, height=1080"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>{fonts}{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{len(F)*D}" data-width="1920" data-height="1080">
{body}</div>
<script>const tl=gsap.timeline({{paused:true}});window.__timelines["main"]=tl;</script></body></html>'''
open(f"{proj}/index.html", "w").write(doc)
import json
json.dump([t for t,_ in F], open(f"{proj}/boards/sentences.json", "w"), ensure_ascii=False)
print(len(F), "frames")
