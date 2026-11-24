#!/usr/bin/env python3
"""Builds FILM.md for «Бір нөмірден басталған махаббат».

Identity, wardrobe and location strings live in one place below and are pasted
verbatim into every prompt, so a change here (e.g. swapping which reference image
is Qarakat and which is Arai) propagates to all 45 clips. Run:  python3 build_film.py
"""
import os

ASPECT = "16:9"

# ---------------------------------------------------------------- characters
CHAR = {
    "ZH": dict(
        kk="Жандос", ref=1,
        short="ZHANDOS (man, ref image 1): twenties, tall and lean, thick messy jet-black hair, calm dark eyes, small moles on his cheeks; keep his exact face from the reference.",
        id='''ZHANDOS (CHARACTER_A): a young Kazakh man in his twenties with East Asian features; tall, lean build, upright relaxed posture; long oval face; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead (not swept back, not short and neat on top); straight thick dark eyebrows, narrow calm dark-brown eyes, straight nose, natural light skin with a few small dark moles on his cheeks; clean-shaven. Use supplied reference image 1 (his character sheet) as the identity reference and preserve his exact face and features.''',
    ),
    "QA": dict(
        kk="Қарақат", ref=2,
        short="QARAKAT (woman, ref image 2): twenties, slim, jet-black hair in a high round bun, large thin silver hoop earrings, calm almond eyes; keep her exact face from the reference.",
        id='''QARAKAT (CHARACTER_B): a young Kazakh woman in her twenties with East Asian features; slim build, a little shorter than Zhandos; jet-black hair pulled back smoothly from the face into a high round bun at the back of the crown; straight dark brows, almond-shaped dark-brown eyes, calm composed expression at rest, natural light skin, soft coral-pink lips. Signature details, keep in every frame: the high round bun and large thin silver hoop earrings. Use supplied reference image 2 (her character sheet) as the identity reference and preserve her exact face and features.''',
    ),
    "AR": dict(
        kk="Арай", ref=3,
        short="ARAI (woman, ref image 3): twenties, freckles, long curly chestnut-brown hair in a high ponytail; keep her exact face from the reference.",
        id='''ARAI (CHARACTER_C): a young Kazakh woman in her twenties with East Asian features; soft rounded face with a warm smile and light freckles across her nose and cheeks, defined dark brows, dark-brown almond eyes; long voluminous curly chestnut-brown hair tied in a high curly ponytail tied with a black hair tie, loose curly strands framing her face. Signature details, keep in every frame: the freckles and the curly chestnut ponytail. Use supplied reference image 3 (her character sheet) as the identity reference and preserve her exact face and features.''',
    ),
}

WARD = {
    "ZH_SPORT": ("Zhandos", '''black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes — exactly as in reference image 1, unchanged.''',
                "Референстегі қара adidas худи мен шалбар (ақ үш жолақ), ақ кроссовка — өзгеріссіз"),
    "ZH_DATE": ("Zhandos", '''black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes — exactly as in reference image 1, unchanged.''',
                "Референстегі қара adidas худи мен шалбар (ақ үш жолақ), ақ кроссовка — өзгеріссіз"),
    "ZH_SEA": ("Zhandos", '''black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes — exactly as in reference image 1, unchanged.''',
                "Референстегі қара adidas худи мен шалбар (ақ үш жолақ), ақ кроссовка — өзгеріссіз"),
    "ZH_SUIT": ("Zhandos", '''classic black two-piece suit, crisp white shirt, slim black tie, polished black leather shoes.''',
                "Қара костюм, ақ көйлек, қара галстук, қара туфли"),
    "QA_SPORT": ("Qarakat", '''oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers, the large thin silver hoop earrings — exactly as in reference image 2, unchanged; she carries no bag or backpack.''',
                "Референстегі қою көк худи, күміс жетон-кулон, ашық сұр шалбар, ақ кроссовка, күміс сырға — өзгеріссіз"),
    "QA_DATE": ("Qarakat", '''oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose light heather-grey jogger sweatpants with elastic cuffs, plain white low-top sneakers, the large thin silver hoop earrings — exactly as in reference image 2, unchanged.''',
                "Референстегі қою көк худи, күміс жетон-кулон, ашық сұр шалбар, ақ кроссовка, күміс сырға — өзгеріссіз"),
    "QA_SEA": ("Qarakat", '''oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose light heather-grey jogger sweatpants with elastic cuffs, plain white low-top sneakers, the large thin silver hoop earrings — exactly as in reference image 2, unchanged.''',
                "Референстегі қою көк худи, күміс жетон-кулон, ашық сұр шалбар, ақ кроссовка, күміс сырға — өзгеріссіз"),
    "QA_BRIDE": ("Qarakat", '''white wedding gown with a fitted lace bodice and a long full skirt, a sheer veil pinned beneath her high bun, the silver hoop earrings, the engagement ring on her ring finger.''',
                 "Ақ той көйлегі, шаршы (фата), сырға, сақина"),
    "AR_DAY": ("Arai", '''oversized cream-ivory hoodie with pale-pink drawstrings and a small pale-pink heart on the left chest, black track pants with two white side stripes, pink-and-white low-top sneakers — exactly as in reference image 3, unchanged.''',
                "Референстегі ақшыл худи (қызғылт бау, жүрекше), ақ жолақты қара шалбар, қызғылт-ақ кроссовка — өзгеріссіз"),
}

GROUP = {
    "ZHF": '''ZHANDOS'S TWO FRIENDS (supporting, generic faces, never in close-up, no jewellery or necklaces): FRIEND 1 — buzz-cut black hair, plain grey pullover hoodie, black joggers; FRIEND 2 — black baseball cap, dark-green zip-up track jacket, black joggers.''',
    "QAF": '''QARAKAT'S TEAMMATE — exactly ONE girl: white T-shirt, black leggings, white sneakers, long straight black hair in a low ponytail; no hoodie, no bun, no curls, no hoop earrings.''',
    "FAM": '''RELATIVES AND GUESTS of both families (supporting, generic faces) in festive clothes.''',
    "HELP": '''A HELPER: only her hands and forearms are visible; her face is never shown.''',
    "STAFF": '''Two banquet-hall staff members in black uniforms, soft in the background.''',
}

# ---------------------------------------------------------------- locations
LOC = {
    "HALL": ('''Indoor volleyball gym, evening; keep this layout identical in every shot of the film. A honey-coloured wooden court with white lines. The volleyball NET stretches ACROSS the middle of the court, from the left side wall toward the right side wall, on two padded poles at the sidelines, dividing the court into a near half and a far half — it never hangs in front of the bleachers. Wooden bench bleachers run along the RIGHT side wall. A grey double exit door with a green exit sign is in the LEFT side wall, in the near half. Pale beige walls, tall dark windows high up, square white LED ceiling panels. Background life: in the far half, beyond the net, five or six other students in coloured sports T-shirts (red, blue, green, yellow) with shorts casually practise, passing their own ball over the net; three or four more sit on the bleachers chatting. All background people stay small, soft-focus and anonymous, never look at the camera, never wear white T-shirts with black leggings, and none wears a navy, black three-stripe or cream hoodie, a high bun, a curly ponytail or hoop earrings. Zhandos and his friends sit on the lowest bench at the near end of the bleachers (screen-right); the exit is screen-left.''',
             '''Even overhead LED panels, neutral white with a warm bounce from the wooden floor; natural skin tones with visible skin texture.'''),
    "HALL_NIGHT": ('''Outside the sports complex at night: wide concrete entrance steps and glass doors glowing from inside at screen-right, a quiet city street running left–right in front, parked cars.''',
                   '''Warm sodium street lamps, cool blue night ambience, red taxi tail lights; natural skin tones.'''),
    "HALL_DAY": ('''Outside the same sports complex in the late afternoon: wide concrete entrance steps, glass doors, a pale concrete facade, young trees, the sidewalk running left–right.''',
                 '''Low warm late-afternoon sun from screen-left, soft golden rim light, natural skin tones.'''),
    "CAFE": ('''A small modern café on a quiet city street in daylight: a large glass front, a glass door with a brass handle, two small outdoor tables, potted plants, a tree-lined sidewalk running left–right, light pedestrian traffic, mild weather.''',
             '''Soft overcast daylight, neutral natural colours, realistic skin tones.'''),
    "PARK": ('''A tree-lined park alley in daytime: a paved path, wooden benches, mature leafy trees, a few distant passers-by.''',
             '''Dappled sunlight through the leaves, warm-green palette, natural skin tones.'''),
    "ZH_ROOM": ('''Zhandos's small bedroom: a single bed with dark-grey bedding against the left wall, a wooden desk with a desk lamp under the window, a shelf with a few books and a volleyball, the window showing the city.''',
                '''Night: a warm desk lamp as the key, the cool glow of the phone on his face, city lights soft through the window.'''),
    "QA_ROOM": ('''Qarakat's bedroom: a bed with white bedding, a warm bedside lamp, a tall free-standing mirror, sheer curtains on the window, a small shelf with plants.''',
                '''Night: a warm bedside lamp from screen-left, the cool phone glow on her face.'''),
    "CINEMA_EXT": ('''A city square in front of a cinema at early evening: a lit cinema facade with blank, unreadable signage, warm street lamps just switching on, a few passers-by.''',
                   '''Blue-hour sky mixed with warm street lamps and the warm glow of the cinema facade; city lights in soft bokeh.'''),
    "CINEMA": ('''A dark cinema auditorium: rows of deep-red seats; the screen is off-frame in front of the audience.''',
               '''Only the cool, softly flickering light of the off-frame projection on their faces; deep shadows around them.'''),
    "CAFE2": ('''A cosy café interior in the evening: a small wooden table, two cups of tea, plants, a few soft-focus patrons in the background.''',
              '''Warm pendant lights overhead, cosy amber tones, natural skin.'''),
    "BOOK": ('''A warm bookstore aisle: tall wooden shelves filled with books whose covers and spines are plain and unreadable.''',
             '''Warm pendant lights, wooden tones, soft shadows.'''),
    "QA_EXT": ('''The entrance of Qarakat's apartment building at night: a lit glass entrance door at the top of three steps, a short path, one street lamp, a quiet residential street.''',
               '''Night: one warm street lamp from screen-left and the warm light of the glass entrance door.'''),
    "STEPPE": ('''Open golden steppe grassland on a clear day, gentle hills on the horizon, a big blue sky.''',
               '''Bright warm afternoon sun from behind the camera, golden grass, blue sky.'''),
    "LIVING": ('''A cosy living room at night: a soft grey sofa with a knitted blanket, a bowl of popcorn; the TV is off-frame in front of the sofa.''',
               '''The shifting cool-warm light of the off-frame TV on their faces, a warm lamp far behind them.'''),
    "CAFE3": ('''A bright café by a large sunny window in daytime: a marble-top table with two cups of coffee and a slice of cake.''',
              '''Bright daylight through the window, warm and airy, natural skin tones.'''),
    "STREET": ('''A city street at night: lit shop windows with blank, unreadable signage, warm street lamps, light foot traffic, clean dry pavement.''',
               '''Night: warm street lamps and soft shop-window glow, bokeh lights behind them.'''),
    "BEACH": ('''A quiet sandy seashore at sunset: a calm sea with gentle waves, the sun low over the horizon, a golden-pink sky. A romantic picnic on the sand: a low wooden table on a cream blanket with cushions, a vase of white and blush flowers, plates of sweets, glass-jar candles and small lanterns glowing. The couple sits side by side facing the sea — Zhandos on the left, Qarakat on the right. No other people on the beach.''',
              '''Warm low sun on the horizon backlighting them, golden-pink sky, warm candle fill on their faces; natural skin tones, no lens flares.'''),
    "BRIDE_ROOM": ('''A bright bridal room on the wedding day: a tall window with sheer curtains, a full-length mirror, white flowers.''',
                   '''Bright soft window light through sheer curtains, white and warm-gold tones.'''),
    "GROOM_ROOM": ('''A calm hotel room on the wedding day with a large mirror.''',
                   '''Soft daylight from a window, neutral warm tones.'''),
    "TABLE": ('''A white table by a window on the wedding day.''',
              '''Soft window light, warm gold reflections, no artificial sparkle.'''),
    "HALL_W": ('''A grand wedding banquet hall: crystal chandeliers, round tables with white tablecloths and gold accents, white and blush floral arrangements, a wide aisle leading to tall double doors.''',
               '''Warm chandelier light mixed with daylight, a white and gold palette, natural skin tones.'''),
}

VISUAL = '''High-end photorealistic live-action cinema, natural human anatomy, realistic skin texture with visible pores, believable physics and weight, coherent natural real-time motion at 24fps, detailed environment, controlled depth of field, cinematic composition, one continuous take with no dissolves or double exposure. Characters never look into the camera lens; their eyes go to the person or place the action describes.'''

AVOID = '''Face identity drift, altered facial features, changed hairstyles, wardrobe changes, extra fingers or limbs, distorted hands, duplicate people, floating objects, warped backgrounds, unnatural body movement, slow motion, exaggerated acting, waxy or plastic skin, cartoon or 3D-render look, random text, subtitles, logos or brand marks beyond the reference outfits, watermarks, cuts within the shot, unrequested visual effects'''

# ---------------------------------------------------------------- clips
# gen = seconds to generate; edit = seconds used in the final cut (0 = runs in a split screen with the previous clip)
CLIPS = []


def C(**k):
    CLIPS.append(k)


# ===== SCENE 1 =====
C(n=1, scene=1, en="The Game Ends", kk="Ойын аяқталды", gen=10, edit=8,
  cast=[("QA", "QA_SPORT"), ("AR", "AR_DAY"), ("ZH", "ZH_SPORT")], groups=["QAF", "ZHF"], loc="HALL",
  shot="Жалпы план, еден деңгейінен; солға баяу трекинг",
  ctx='''The opening of the film: a women's volleyball game has just ended and the players are leaving the gym. This is the evening Zhandos first sees Qarakat.''',
  act='''Opening frame: low angle near the floor — a volleyball already lying on the polished wooden floor in the foreground bounces twice, low, and rolls out of frame screen-left — nobody throws it. Behind it the women's team is collecting their bags after the game. Qarakat, setting off from the middle of the court near the net, far from the bleachers, carrying nothing, walks from right to left across the frame, side-on to the camera, toward the exit doors with Arai beside her and one teammate on the far side, laughing at something Arai says. In the soft background at screen-right, Zhandos sits with his two friends on the lowest bench of the bleachers, small in frame. As the girls pass, Zhandos turns his head to look at Qarakat. Final frame: Qarakat and her teammates walking out of frame screen-left; Zhandos, small and soft in the background at screen-right, looking after her.''',
  cam='''Wide shot starting low near the floor, rising gently to eye level as it tracks slowly left with the girls; 35mm natural perspective; focus pulls from the bouncing ball to Qarakat; Zhandos stays soft in the background.''',
  perf='''Relaxed post-game energy: real, unforced laughter, a little tiredness in the shoulders. Qarakat's smile is small and genuine. Zhandos's head turn is subtle and unhurried.''',
  audio='''Two hollow ball bounces echoing in the gym, sneakers squeaking, the teammates' happy chatter kept low and indistinct (no clear words), gym reverb. No music yet.''',
  cont='''Evening. Qarakat moves right-to-left toward the exit (screen-left); Zhandos and his friends stay by the bleachers at screen-right. The next shot is Zhandos noticing her.''',
  avoid="a crowd of extra players, a second woman with a high bun and silver hoop earrings, readable signs on the walls",
  note="Монтажда: фильм 1,5 с қара экранмен басталады, доптың соғылған дыбысы қараңғыда естіледі, сосын кадр ашылады.",
  first="Еденде секірген доп; артта сөмкесін алып жатқан қыздар.",
  last="Қыздар кадрдан солға шығып барады; артта, оң жақта Жандос оған қарап тұр.",
  tr=dict(tech="Көзқарас бойынша монтаж (eye match) + қимыл үстіндегі монтаж",
          why="Жандос басын бұрған сәтте кесеміз — көрермен оның не көргенін бірден түсінеді.",
          mech="A клипте Жандос басын солға бұрады → B клип оның жүзінен басталады, көзі солға қарап тұр.",
          match="Қарақат — экранның сол жағында, Жандостың көзқарасы — солға; зал жарығы бірдей.",
          sound="Қыздардың күлкісі мен кроссовка сықыры B клипке созылады (L-cut).",
          where="Монтажда"))

C(n=2, scene=1, en="He Sees Her", kk="Ол оны көрді", gen=10, edit=8,
  cast=[("ZH", "ZH_SPORT")], groups=["ZHF"], loc="HALL",
  shot="Орта план → ірі план, баяу жақындау (push-in)",
  ctx='''Zhandos notices Qarakat for the first time — the moment the love story begins.''',
  act='''Opening frame: medium shot of Zhandos sitting on the lowest bench of the bleachers, laughing at a friend's joke; his two friends' shoulders are at the frame edges. His eyes drift screen-left and find her: the laugh stops mid-breath; a tiny double take — his eyes flick away and snap back; they widen a fraction and brighten, catching the light; lips part, he forgets to breathe, then a slow, astonished smile spreads as his gaze follows someone moving further screen-left (Qarakat walking to the exit, off-screen). The camera pushes in slowly from a medium shot to a close-up of his face. In the last two seconds he taps his friend's arm, glances at him, looks back toward her and asks in an excited half-whisper in Kazakh: "Анау қыз кім өзі?" Final frame: close-up of Zhandos, eyes fixed screen-left, a faint hopeful curiosity on his face.''',
  cam='''Starts as a 50mm medium shot at eye level and pushes in slowly on a dolly to an 85mm-feel close-up; shallow depth of field, the gym lights behind him melting into soft bokeh; composed slightly right of centre, leaving looking room on the left.''',
  light='''Overhead LED panels with a soft edge light from the gym lights behind him; natural skin tones with visible skin texture.''',
  perf='''Romantic-lead acting, readable but never exaggerated: love at first sight told through the eyes — widening, brightening, a held breath, a disbelieving smile — then boyish excitement as he taps his friend and glances friend–girl–friend.''',
  audio='''The gym noise and the friends' chatter gradually muffle as the camera moves in; a soft single piano note enters around the midpoint. Kazakh dialogue, spoken in Kazakh with these exact words — ZHANDOS (quiet, almost to himself, curious, slow and clearly articulated — four separate words, never merged): "Анау қыз... кім өзі?"''',
  cont='''Same evening gym. Eyeline always screen-left, toward the exit where Qarakat walks. The next shot is his friends answering.''',
  first="Жандос достарымен күліп тұр; көзі солға ауады.",
  last="Жандостың ірі планы, көзі солға қадалған.",
  tr=dict(tech="Дыбыс көпірі (J-cut) + реакциялық монтаж",
          why="Достың жауабы сұраққа бірден жалғасып, диалог табиғи ағады.",
          mech="1-достың «Қайсы?» деген сөзі A клиптің соңғы жарты секундында алдын ала естіледі, сосын үш адамдық кадрға кесеміз.",
          match="Жандос сол орында, көзқарасы әлі солға; жарық сол.",
          sound="Фортепиано ноталары екі клипке ортақ.",
          where="Монтажда"))

C(n=3, scene=1, en="Does Anyone Have Her Number?", kk="«Нөмірі бар ма?»", gen=10, edit=9,
  cast=[("ZH", "ZH_SPORT")], groups=["ZHF"], loc="HALL",
  shot="Үш адамдық орта план, жеңіл қолмен түсіру",
  ctx='''Zhandos's friends tell him the girl is Qarakat, an acquaintance of theirs — but nobody has her number.''',
  act='''Opening frame: a medium three-shot of the three young men sitting side by side on the lowest bench of the bleachers — FRIEND 1 (buzz-cut, grey hoodie) at screen-left, Zhandos centre-right, FRIEND 2 (black cap, dark-green track jacket) at screen-right. Friend 1 follows Zhandos's gaze screen-left and answers casually. Zhandos turns to him quickly and asks, eager. Friend 2 shrugs and shakes his head as he answers. Zhandos glances back toward the exit, makes a decision, jumps up from the bench and takes a first quick step screen-left. Final frame: Zhandos stepping out of frame screen-left; the two friends exchange an amused look.''',
  cam='''Medium three-shot at eye level, 40mm, gentle handheld breathing; at the end a small pan left following Zhandos's first step.''',
  perf='''Friend 1 relaxed and matter-of-fact; Zhandos animated, hopeful, slightly impatient; Friend 2 an easy shrug. Natural comic timing, nothing exaggerated.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — FRIEND 1 (casual): "Қайсы? Қарақат па? Ол біздің танысымыз ғой." ZHANDOS (eager): "Қарақат дейсің бе? Нөмірі бар ма?" FRIEND 2 (shrugging): "Жоқ, нөмірі бізде жоқ." Low gym echo; the soft piano continues quietly.''',
  cont='''Zhandos exits screen-left, toward the exit; in the next shot he comes out of the building still moving screen-left.''',
  first="Үш адамдық кадр: 1-дос сол жақта, Жандос ортада, 2-дос оң жақта.",
  last="Жандос кадрдан солға шығып кетеді; достары бір-біріне күле қарайды.",
  tr=dict(tech="Есік арқылы өту + қозғалыс бағытын сақтау (motion match)",
          why="Жандостың асығысы үзілмей, залдан көшеге жалғасады.",
          mech="A клипте Жандос солға қадам басады → B клипте шыны есік ашылып, ол дәл сол бағытта (солға) жүгіріп шығады.",
          match="Қозғалыс бағыты — солға; киімі бірдей; кеш.",
          sound="Есіктің итерілген дыбысы кесуден 0,3 с бұрын басталады; фортепиано жалғасады.",
          where="Монтажда"))

C(n=4, scene=1, en="Too Late", kk="Кешікті", gen=10, edit=6,
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT"), ("AR", "AR_DAY")], groups=["QAF"], loc="HALL_NIGHT",
  shot="Жалпы план, статикалық; соңында баяу жақындау",
  ctx='''Zhandos runs out after Qarakat, but she has already left in a taxi with her friends.''',
  act='''Opening frame: wide shot from across the street. A white sedan taxi with a lit roof sign waits at the curb in front of the steps; Arai (cream hoodie, curly ponytail) and Qarakat's teammate are getting in. Qarakat — navy hoodie, high bun, silver hoops — gets into the back seat last and the door closes. The taxi pulls away and drives off screen-left down the street. At the same moment the glass doors at screen-right swing open and Zhandos hurries down the steps, slows at the curb and stops, watching the red tail lights shrink into the distance. He exhales and gives a small rueful smile to himself. Final frame: Zhandos alone at the curb in a three-quarter back view, looking screen-left after the distant tail lights.''',
  cam='''Wide, locked-off at eye level from across the street, 35mm; in the final three seconds a very slow push-in toward Zhandos.''',
  perf='''Disappointed but not dramatic — a slight drop of the shoulders, a breath out, a small self-aware smile.''',
  audio='''A car door closing, the engine pulling away, a quiet evening street, his quick footsteps on the steps. The piano phrase stops unresolved.''',
  cont='''Night. Everything moves screen-left (the taxi and Zhandos), continuing the direction from inside the gym.''',
  avoid="readable licence plates, readable taxi branding",
  first="Такси жиекте; қыздар отырып жатыр, Қарақат соңғы болып отырады.",
  last="Жандос жиекте жалғыз, алыстаған қызыл шамдарға қарап тұр.",
  tr=dict(tech="Уақыт бойынша қатаң кесу + дыбыс көпірі",
          why="Түннен күндізгі жарыққа кенет ауысу «келесі күн» екенін түсіндірмей-ақ көрсетеді.",
          mech="Қызыл шамдардан кейін бірден күндізгі кафе есігіне кесеміз.",
          match="Келесі кадр да солдан оңға оқылатын көше; Жандостың киімі бірдей.",
          sound="Кафе есігінің қоңырауы кесуден 0,3 с бұрын естіледі; ойнақы пиццикато басталады.",
          where="Монтажда"))

# ===== SCENE 2 =====
C(n=5, scene=2, en="Arai Comes Out Alone", kk="Арай жалғыз шығады", gen=10, edit=6,
  cast=[("QA", "QA_SPORT"), ("AR", "AR_DAY"), ("ZH", "ZH_SPORT")], groups=["QAF"], loc="CAFE",
  shot="Жалпы-орта план, тротуардың арғы бетінен",
  ctx='''The next day: Qarakat and a friend leave a café; a moment later Arai comes out alone — and Zhandos sees his chance.''',
  act='''Opening frame: the café's glass door in the centre of the frame. Qarakat and one teammate step out laughing and walk away along the sidewalk screen-right, leaving frame. The door swings shut. A few seconds later it opens again and Arai steps out alone, pushing up the sleeves of her cream hoodie and glancing at her phone. Zhandos enters from the left foreground (seen from behind and the side), walking toward her and raising a hand to get her attention. Final frame: Arai looks up at him, mildly surprised; Zhandos is two steps away from her.''',
  cam='''Wide-medium shot from across the sidewalk, 35mm, static, with a slight pan right as Zhandos walks in.''',
  perf='''Arai relaxed and self-possessed; Zhandos polite and a little nervous.''',
  audio='''A small doorbell chime each time the door opens, street ambience, footsteps. A light, playful pizzicato tune begins softly.''',
  cont='''Daytime, the next day. Qarakat exits screen-right. Arai and Qarakat must look clearly different: curly chestnut ponytail and cream hoodie versus high black bun and navy hoodie.''',
  avoid="readable café name or menu text",
  first="Кафенің шыны есігі; Қарақат құрбысымен шығып, оңға кетеді.",
  last="Арай басын көтереді; Жандос одан екі қадам жерде.",
  tr=dict(tech="Қимыл үстіндегі монтаж (action cut)",
          why="Жандостың жақындауы үзілмей, бірден әңгімеге ұласады.",
          mech="Жандостың соңғы қадамында кесеміз → B клип оның Арайдың алдына тоқтаған сәтінен басталады.",
          match="Жандос — сол жақта, Арай — оң жақта; қозғалыс солдан оңға.",
          sound="Көше шуы мен пиццикато үзілмейді.",
          where="Монтажда"))

C(n=6, scene=2, en="You're Arai, Right?", kk="«Сен Арайсың ғой?»", gen=10, edit=9,
  cast=[("ZH", "ZH_SPORT"), ("AR", "AR_DAY")], loc="CAFE",
  shot="Екі адамдық орта план, профильден",
  ctx='''Zhandos introduces himself to Arai and asks whether she knows Qarakat.''',
  act='''Opening frame: a medium two-shot in profile on the sidewalk in front of the café — Zhandos at screen-left facing right, Arai at screen-right facing left. Zhandos, a bit nervous, rubs the back of his neck and greets her. Arai, hands in her hoodie pocket, answers. Zhandos asks his question. At Qarakat's name Arai raises one eyebrow and tilts her head as she answers. Final frame: Arai looking at him with a sceptical half-smile, waiting for his answer.''',
  cam='''Medium two-shot at eye level, 50mm, static with subtle handheld breathing; both faces clearly readable.''',
  perf='''Zhandos polite, slightly awkward, hopeful. Arai guarded but curious; the eyebrow lift is small and natural.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ZHANDOS (friendly, a little nervous): "Сәлем! Сен Арайсың ғой?" ARAI (neutral): "Иә, не болды?" ZHANDOS: "Бір нәрсе сұрайын деп едім. Қарақат деген қызды танисың ба?" ARAI (curious, cautious): "Иә, танимын. Неге?" Quiet street ambience under the voices; the pizzicato very low.''',
  cont='''Zhandos always screen-left, Arai screen-right. Daylight, the café front behind them.''',
  first="Профильдегі екі адамдық кадр: Жандос солда, Арай оңда.",
  last="Арай күмәнмен жымиып, жауап күтіп тұр.",
  tr=dict(tech="Иық үстінен кадрға кесу (кадр / кері кадр)",
          why="Шешуші сұрақ келе жатыр — Арайдың реакциясын жақыннан көру керек.",
          mech="Арайдың «Неге?» деген сөзінен кейінгі кідірісте Жандостың иығы үстінен түсірілген кадрға кесеміз.",
          match="180° сызығы сақталады: Жандос солда, Арай оңда; көзқарастар сәйкес.",
          sound="Көше шуы үздіксіз.",
          where="Монтажда"))

C(n=7, scene=2, en="Not Without Her Permission", kk="«Рұқсатынсыз бере алмаймын»", gen=10, edit=9,
  cast=[("ZH", "ZH_SPORT"), ("AR", "AR_DAY")], loc="CAFE",
  shot="Жандостың иығы үстінен Арайға, орта-ірі план",
  ctx='''Zhandos asks Arai for Qarakat's number; she refuses until she has asked Qarakat herself.''',
  act='''Opening frame: over-the-shoulder shot — the back of Zhandos's head and his left shoulder (black hoodie with white sleeve stripes) soft in the left foreground, Arai sharp at screen-right facing him. Zhandos asks for the number. Arai considers him for a moment, then shakes her head politely but firmly as she answers. She gives a small nod, turns and walks away screen-right along the sidewalk. Final frame: Arai walking out of frame screen-right; Zhandos's shoulder still in the left foreground.''',
  cam='''Over-the-shoulder medium close-up on Arai, 50mm, shallow depth of field, static; focus stays on Arai until she exits.''',
  perf='''Arai is loyal and principled, not rude: calm, firm, with a polite small smile. Zhandos stays still, slightly deflated.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ZHANDOS (hopeful): "Сол қызбен танысқым келіп жүр. Нөмірін бере аласың ба?" ARAI (polite, firm): "Жоқ, рұқсатынсыз бере алмаймын. Алдымен өзінен сұрайын." Her footsteps fading, street ambience.''',
  cont='''Arai exits screen-right; in the next shot she keeps the same direction as she walks up to Qarakat.''',
  first="Жандостың иығы алдыңғы планда, Арай оң жақта, анық.",
  last="Арай кадрдан оңға шығып барады.",
  tr=dict(tech="Қозғалыс сәйкестігі (motion match) + дыбыс көпірі",
          why="Арай тура Қарақатқа барады — ой жүрісі көрнекі түрде жалғасады.",
          mech="Арай A клипте оңға шығады → B клипте сол жақтан кадрға кіріп, Қарақаттың жанына тоқтайды.",
          match="Қозғалыс бағыты солдан оңға; Арайдың киімі бірдей.",
          sound="Пиццикато жалғасады; B клиптің құс үні жарты секунд бұрын кіреді.",
          where="Генерацияда (Арайдың кадрға кіруі) + монтажда"))

C(n=8, scene=2, en="I Don't Even Know Him", kk="«Танымаймын ғой»", gen=10, edit=8,
  cast=[("AR", "AR_DAY"), ("QA", "QA_SPORT")], loc="PARK",
  shot="Екі адамдық орта план",
  ctx='''Later that day Arai tells Qarakat that a guy named Zhandos wants her number; Qarakat declines.''',
  act='''Opening frame: Qarakat standing by a bench on the park path at screen-right, scrolling her phone. Arai walks into frame from screen-left and stops beside her, facing her. Leaning in with a playful, conspiratorial smile, Arai tells her about Zhandos. Qarakat lowers her phone; her eyebrows lift in surprise, then she shakes her head with a shy, dismissive half-smile as she answers. She looks down and tucks her hands into her hoodie pocket. Final frame: Qarakat looking down with a faint smile she is trying to hide; Arai shrugging.''',
  cam='''Medium two-shot at eye level, 50mm, static with gentle handheld breathing; Arai at screen-left, Qarakat at screen-right.''',
  perf='''Arai teasing and warm. Qarakat surprised, then shy and a little flattered under the refusal — the hidden smile is the subtext.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ARAI (playful, conspiratorial): "Қарақат, саған бір жігіт қызығып жүр. Аты Жандос. Нөміріңді сұрап жатыр." QARAKAT (shy, dismissive): "Жоқ, бермей-ақ қойшы. Танымаймын ғой." Birdsong, rustling leaves, the distant city.''',
  cont='''Daytime, the same day. The two women must stay clearly different: Qarakat — high black bun, silver hoops, navy hoodie; Arai — curly chestnut ponytail, freckles, cream hoodie.''',
  first="Қарақат орындық жанында; Арай сол жақтан кадрға кіреді.",
  last="Қарақат төмен қарап, жымиюын жасырады; Арай иығын көтереді.",
  tr=dict(tech="Есік арқылы өту (уақыт секірісі)",
          why="Үшінші күнге өтудің ең таза жолы — жаңа есіктің ашылуы.",
          mech="Қарақаттың төмен қараған сәтінен кейін спорт кешенінің шыны есігі ашылып, Жандос пен достары шыққан кадрға кесеміз.",
          match="Жандостың киімі бірдей; күн жарығы алтын реңкке ауысады.",
          sound="Ойнақы әуен екі клипке ортақ (музыкалық көпір).",
          where="Монтажда"))

# ===== SCENE 3 =====
C(n=9, scene=3, en="Did She Say No?", kk="«Нөмірін бермеді ме?»", gen=10, edit=7,
  cast=[("ZH", "ZH_SPORT"), ("AR", "AR_DAY")], groups=["ZHF"], loc="HALL_DAY",
  shot="Орта-жалпы план → екі адамдық орта план, қолмен ілесу",
  ctx='''The third day: Zhandos comes out of the volleyball hall, spots Arai and asks what Qarakat said.''',
  act='''Opening frame: the glass doors of the sports complex swing open and Zhandos comes down the steps with his two friends, sports bags on their shoulders. He spots Arai walking along the sidewalk from screen-right, jogs over and stops in front of her — Zhandos screen-left, Arai screen-right; his friends hang back behind him. Zhandos asks, hopeful. Arai shakes her head as she answers. Zhandos's shoulders drop slightly. Final frame: medium two-shot, Zhandos disappointed, Arai sympathetic.''',
  cam='''Starts wide-medium on the steps and follows Zhandos with a smooth handheld move, settling into a medium two-shot, 35mm.''',
  perf='''Zhandos hopeful, then visibly deflated; Arai sympathetic but matter-of-fact.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ZHANDOS (hopeful): "Арай, Қарақат не деді? Нөмірін бермеді ме?" ARAI (shaking her head): "Жоқ, келіспеді." Footsteps on concrete, light street ambience, playful music low.''',
  cont='''Third day, late afternoon. Zhandos screen-left, Arai screen-right — the same sides as at the café.''',
  first="Шыны есік ашылып, Жандос достарымен баспалдақтан түседі.",
  last="Екі адамдық кадр: Жандостың көңілі түсіп тұр, Арай жанашыр.",
  tr=dict(tech="Тұрақты кадрға кесу (комедиялық пауза)",
          why="Комедия қозғалмайтын кадрды жақсы көреді — «сауда» сахнасы сондай кадрда ойналады.",
          mech="Жандос ернін жымқырып ойланған сәтте кесеміз → B клип сол ойланудан, қозғалмайтын кадрда басталады.",
          match="Позициялар бірдей; күн жарығы сол жақтан.",
          sound="Музыка бір сәтке тынады — комедиялық кідіріс.",
          where="Монтажда"))

C(n=10, scene=3, en="Can We Make a Deal?", kk="«Мынаған келісе алмаймыз ба?»", gen=10, edit=9,
  cast=[("ZH", "ZH_SPORT"), ("AR", "AR_DAY")], groups=["ZHF"], loc="HALL_DAY",
  shot="Қозғалмайтын екі адамдық орта план (комедиялық кадр)",
  ctx='''Zhandos tries to buy Qarakat's number from Arai with money; Arai plays hard to get.''',
  act='''Opening frame: locked-off medium two-shot — Zhandos at screen-left, Arai at screen-right, his friends soft in the background. Zhandos thinks for a beat, lips pressed, then pulls a few folded banknotes out of his hoodie pocket and holds them out to Arai with a hopeful, slightly sly smile as he speaks. Arai looks down at the money, then up at him, narrows her eyes and theatrically weighs it, says her first line slowly, pauses, then delivers her second line deadpan and holds out her open palm. Final frame: Arai with her palm open and eyebrows raised; Zhandos frozen mid-smile, caught out.''',
  cam='''Locked-off medium two-shot at eye level, 40mm, no camera movement at all — the stillness lets the comedy play.''',
  perf='''Deadpan comedy, understated. Zhandos sly and hopeful; Arai savouring her leverage while keeping a straight face.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ZHANDOS (sly, hopeful): "Мынаған келісе алмаймыз ба?" ARAI (slowly, pretending to think): "Ойланып көрейін..." — a short pause — ARAI (deadpan, firm): "Үстінен қос!" Light street ambience; the music stops for the pause and returns on her last line.''',
  cont='''Same positions as the previous shot. The banknotes are plain folded paper money in his right hand. The next shot starts with Arai's palm still open.''',
  avoid="close-up readable or fake-looking banknote designs",
  first="Қозғалмайтын кадр: Жандос ойланып тұр, Арай оң жақта.",
  last="Арай алақанын жайып, қасын көтерген; Жандостың күлкісі қатып қалған.",
  tr=dict(tech="Соңғы кадр → бастапқы кадр (first/last frame) + қимыл үстіндегі монтаж",
          why="Шешуші қимыл — ақша қосу — үзілмей жалғасуы керек.",
          mech="A клиптің соңғы кадрын B клиптің бастапқы суреті ретінде береміз: Арайдың ашық алақаны екі клипке ортақ.",
          match="Алақан, ақша, позициялар, жарық дәл сәйкес.",
          sound="Ойнақы әуеннің бір акценті кесуге дәл түседі.",
          where="Екеуінде де: генерацияда (бастапқы кадр) және монтажда"))

C(n=11, scene=3, en="But Don't Tell Her It Was Me", kk="«Мә, бірақ мен бергенімді айтпа!»", gen=10, edit=9,
  cast=[("ZH", "ZH_SPORT"), ("AR", "AR_DAY")], loc="HALL_DAY",
  shot="Екі адамдық орта план, баяу жақындау",
  ctx='''Zhandos adds more money; Arai takes it and gives him Qarakat's number, making him promise not to tell.''',
  act='''Opening frame: medium two-shot — Arai at screen-right with her palm open, Zhandos at screen-left. Zhandos sighs with a laugh and places more folded banknotes into her palm. Arai tucks the money into her hoodie pocket, takes out her phone and holds its screen toward him (the screen faces him, away from the camera) and says her line in a low, conspiratorial voice. Zhandos quickly types the number into his own phone. Arai pockets her phone, gives him a knowing look and walks off screen-right. Final frame: Zhandos alone in the frame, looking down at his phone with a growing smile.''',
  cam='''Medium two-shot at eye level, 40mm, a very slow push-in toward Zhandos across the shot.''',
  perf='''Arai secretive and amused; Zhandos relieved and quietly excited, trying not to grin too early.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ARAI (low, conspiratorial): "Мә, бірақ мен бергенімді айтпа!" Soft taps on a phone screen; the playful music resumes.''',
  cont='''Arai exits screen-right. Late-afternoon golden light from screen-left. Phone screens are never readable.''',
  avoid="readable phone screens or numbers",
  first="Арайдың ашық алақаны; Жандос тағы ақша қосады.",
  last="Жандос жалғыз, телефонына қарап жымия бастайды.",
  tr=dict(tech="Көзқарас бойынша детальға кесу (insert)",
          why="Көрермен Жандоспен бірге телефонға қарайды — жеңіс сәті.",
          mech="Жандос телефонға төмен қараған сәтте кесеміз → B клип оның қолындағы телефоннан басталып, жүзіне көтеріледі.",
          match="Телефон оң қолында; алтын жарық бірдей.",
          sound="Экранға түрту дыбысы кесуге дәл түседі.",
          where="Монтажда"))

C(n=12, scene=3, en="Saved", kk="Нөмір сақталды", gen=5, edit=4,
  cast=[("ZH", "ZH_SPORT")], loc="HALL_DAY",
  shot="Ірі план; қолдан жүзге қарай тік көтерілу (tilt up)",
  ctx='''Zhandos finally has Qarakat's number.''',
  act='''Opening frame: close-up of Zhandos's hands holding his phone at chest height, the screen glowing but unreadable. His thumb taps once to save the contact. The camera tilts up to his face as he looks up from the phone and breaks into a wide, boyish grin, then gives a small, quick fist pump. Final frame: close-up of Zhandos grinning, golden light on his face.''',
  cam='''Close-up, 85mm portrait feel, one smooth tilt up from his hands to his face; shallow depth of field.''',
  light='''Warm low golden-hour sun from screen-left, a soft rim light on his hair, natural skin texture.''',
  perf='''Pure, unguarded joy, a little boyish; the fist pump is small and private, not showy.''',
  audio='''A soft tap on the screen; the playful music lands on one bright final note.''',
  cont='''Same late afternoon. The phone stays in his right hand.''',
  avoid="readable phone screen",
  first="Жандостың қолындағы телефон; бас бармағы «сақтау» батырмасын басады.",
  last="Жандостың кең күлкісі, жүзінде алтын жарық.",
  tr=dict(tech="Затқа негізделген сәйкестік (object match — телефон)",
          why="Телефон — оқиғаның басты заты; ол бізді уақыт бойынша кешке алып өтеді.",
          mech="A клипте телефон кадрдың төменгі бөлігінде → B клип дәл сол жерде, кешкі бөлмеде телефонмен басталады.",
          match="Телефон бір қолда, кадрдың бір орнында; күн жарығынан шамның жылы жарығына.",
          sound="Экранға түрту → пернетақта дыбысы.",
          where="Монтажда"))

# ===== SCENE 4 =====
C(n=13, scene=4, en="First Messages", kk="Алғашқы хабарламалар", gen=10, edit=5,
  cast=[("ZH", "ZH_SPORT")], loc="ZH_ROOM",
  shot="Орта план, бүйірден, статикалық",
  ctx='''That evening Zhandos writes to Qarakat for the first time.''',
  act='''Opening frame: medium shot of Zhandos sitting on the edge of his bed, leaning forward with his phone in both hands. He types, stops, deletes, types again, takes a small breath and taps send. He waits a second, then quickly types and sends a second message, then a third. Final frame: Zhandos holding the phone, staring at the screen, waiting.''',
  cam='''Medium shot from slightly to the side at eye level, 50mm, static, shallow depth of field.''',
  perf='''Nervous hope: small hesitations, biting his lip, a short exhale before each send.''',
  audio='''Soft screen taps, a gentle message-sent sound three times, a quiet room. A few sparse piano notes.''',
  cont='''Same day, evening. The phone screen faces him and is never readable — the messages are added as graphics in editing.''',
  avoid="readable phone screen or on-screen text",
  note="Монтажда хабарлама көпіршіктерін қосыңыз: «Сәлем, Қарақат!» → «Қалайсың?» → «Таныссақ бола ма?»",
  first="Жандос төсек шетінде, телефонды екі қолымен ұстап отыр.",
  last="Жандос экранға қарап, жауап күтіп отыр.",
  tr=dict(tech="Параллель монтаж + дыбыс көпірі (себеп → салдар)",
          why="Хабарлама «ұшып барып» Қарақаттың телефонына жетеді — екі бөлмені бір дыбыс жалғайды.",
          mech="«Жіберілді» дыбысы A клиптің соңында; B клип Қарақаттың телефонының жарқ етіп дірілдеуінен басталады.",
          match="Екеуі де кешкі бөлмеде, телефон жарығы жүздерінде.",
          sound="Жіберу дыбысы → хабарлама келу дыбысы.",
          where="Монтажда"))

C(n=14, scene=4, en="Read, No Reply", kk="Оқыды, бірақ…", gen=5, edit=4,
  cast=[("QA", "QA_SPORT")], loc="QA_ROOM",
  shot="Орта-ірі план, сәл жоғарыдан",
  ctx='''Qarakat receives Zhandos's messages, reads them, and does not reply.''',
  act='''Opening frame: Qarakat lying on her stomach on her bed, propped on her elbows; her phone on the bedspread lights up and buzzes. She picks it up and reads; a tiny surprised smile flickers at the corner of her mouth, she bites her lip, then places the phone face-down on the bed beside her and looks away toward the window, thoughtful. Final frame: the phone face-down, Qarakat looking away.''',
  cam='''Medium close-up from slightly above, 50mm, static, shallow depth of field.''',
  perf='''Intrigued but cautious; the smile is barely there and quickly hidden.''',
  audio='''A phone vibrating on the bedspread, a soft message tone, a quiet room.''',
  cont='''Evening. The phone screen is never readable.''',
  avoid="readable phone screen",
  first="Қарақат төсекте етпетінен жатыр; телефоны жарқ етеді.",
  last="Телефон төңкеріліп жатыр; Қарақат терезеге қарап ойланып қалған.",
  tr=dict(tech="Затқа негізделген сәйкестік + уақыт өткенін білдіретін қысқа dissolve (12 кадр)",
          why="Төңкерілген телефоннан Жандостың үстеліндегі телефонға өту «бірнеше күн өтті» дегенді сөзсіз айтады.",
          mech="Төңкерілген телефон кадрдың төменгі бөлігінде → B клип үстел үстінде жатқан телефоннан басталады.",
          match="Телефон кадрдың бір бөлігінде; түнгі жарықтан күндізгі терезе жарығына.",
          sound="Бөлменің тыныштығы; қаласаңыз сағаттың тықылы.",
          where="Монтажда"))

C(n=15, scene=4, en="Days of Silence", kk="Жауапсыз күндер", gen=5, edit=4,
  cast=[("ZH", "ZH_SPORT")], loc="ZH_ROOM",
  shot="Орта план, статикалық",
  ctx='''Several days pass with no reply; Zhandos keeps checking his phone.''',
  act='''Opening frame: Zhandos sitting at his desk by the window in daylight, his phone lying on the desk. He picks it up and checks it — nothing — types one short message with his thumb and sends it, then puts the phone down and leans back with a sigh, running a hand through his hair. Final frame: Zhandos leaning back in his chair, looking at the silent phone.''',
  cam='''Medium shot at eye level, 50mm, static.''',
  light='''Daytime: soft daylight from the window behind the desk, neutral and a little flat — the colour of waiting.''',
  perf='''Mild frustration and patience; no melodrama.''',
  audio='''A screen tap, a message-sent sound, the sigh, a quiet daytime room with distant traffic.''',
  cont='''Several days later, daytime. The phone screen is never readable.''',
  avoid="readable phone screen",
  note="Монтажда хабарлама көпіршігі: «Неге жауап бермейсің?»",
  first="Күндіз; телефон үстел үстінде жатыр.",
  last="Жандос орындыққа шалқайып, үнсіз телефонға қарап отыр.",
  tr=dict(tech="Дыбыс көпірі (J-cut)",
          why="Арайдың кеңесі Жандостың күрсінісіне жауап сияқты естіледі.",
          mech="Арайдың «Қарақат, бір сөйлесіп көрсеңші…» деген даусы A клиптің соңғы секундында естіліп, саябақ кадрына кесеміз.",
          match="Күндізгі жарық екі клипте де.",
          sound="Күрсініс → құстардың үні мен Арайдың даусы.",
          where="Монтажда"))

C(n=16, scene=4, en="Give Him a Chance", kk="«Мүмкіндік беріп көр»", gen=10, edit=7,
  cast=[("AR", "AR_DAY"), ("QA", "QA_SPORT")], loc="PARK",
  shot="Алдынан шегіне ілесу (leading track), екі адамдық орта план",
  ctx='''Some days later, Arai encourages Qarakat to give Zhandos a chance.''',
  act='''Opening frame: Arai (screen-left) and Qarakat (screen-right) walk side by side toward the camera along the park path. Arai gently bumps Qarakat's shoulder with hers and speaks warmly. Qarakat slows down and looks at the path in front of her, thinking, a small undecided smile appearing. Final frame: Qarakat walking more slowly, lost in thought; Arai watching her with a knowing smile.''',
  cam='''The camera leads them, moving backward at walking pace; medium two-shot, 35mm, smooth and steady.''',
  perf='''Arai sincere and supportive, not pushy. Qarakat genuinely considering it — the decision is visible in her eyes.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ARAI (warm, encouraging): "Қарақат, бір сөйлесіп көрсеңші. Жігіт жаман емес сияқты. Мүмкіндік беріп көр." Footsteps on the path, birdsong, leaves.''',
  cont='''The same park alley as before, another day. Arai screen-left, Qarakat screen-right; the two women stay clearly different.''',
  first="Арай мен Қарақат камераға қарай қатар келе жатыр.",
  last="Қарақат баяулап, ойға батқан; Арай оған жымия қарайды.",
  tr=dict(tech="Графикалық сәйкестік (жүздің орны) + уақыт бойынша кесу",
          why="Қарақаттың ойы күндізден кешке дейін созылады — бір ойдың жалғасы.",
          mech="A клипте Қарақаттың ойлы жүзі кадрдың оң жақ бөлігінде → B клипте де жүзі сол орында, енді кешкі бөлмеде.",
          match="Жүздің кадрдағы орны мен көзқарас бағыты бірдей.",
          sound="Құс үні сөніп, бөлменің тыныштығы басталады.",
          where="Монтажда"))

C(n=17, scene=4, en="The Reply", kk="Жауап", gen=5, edit=4,
  cast=[("QA", "QA_SPORT")], loc="QA_ROOM",
  shot="Ірі план",
  ctx='''That evening Qarakat finally replies to Zhandos.''',
  act='''Opening frame: close-up of Qarakat sitting cross-legged on her bed, holding her phone, hesitating. She takes a breath, types a short reply with both thumbs and taps send, then pulls her knees up and hides a shy smile behind them. Final frame: Qarakat hugging her knees, smiling shyly, the phone in her hand.''',
  cam='''Close-up, 85mm portrait feel, static, shallow depth of field.''',
  perf='''A small brave decision followed by shyness; restrained and sweet.''',
  audio='''Soft screen taps, a message-sent sound, a quiet room.''',
  cont='''The same evening as the park walk. The phone screen is never readable.''',
  avoid="readable phone screen",
  first="Қарақат төсекте малдас құрып, телефонын ұстап ойланып отыр.",
  last="Қарақат тізесін құшақтап, ұялып жымияды.",
  tr=dict(tech="Дыбыс көпірі: «жіберілді» → «келді» (себеп → салдар)",
          why="13→14 өтуінің айнасы: енді хабарлама кері бағытта ұшады — бұрылыс сәт.",
          mech="Қарақаттың жіберу дыбысынан кейін бірден Жандостың кеудесінде дірілдеген телефонға кесеміз.",
          match="Екеуі де кешкі бөлмеде; жарық логикасы бірдей.",
          sound="Жіберу дыбысы → діріл мен хабарлама дыбысы; музыка қайта оралады.",
          where="Монтажда"))

C(n=18, scene=4, en="She Answered!", kk="Ол жауап берді!", gen=5, edit=4,
  cast=[("ZH", "ZH_SPORT")], loc="ZH_ROOM",
  shot="Орта план, жоғарыдан; ол отырғанда камера көтеріледі",
  ctx='''Zhandos receives Qarakat's reply and immediately writes back to invite her out.''',
  act='''Opening frame: Zhandos lying on his back on his bed in the dim room, staring at the ceiling, his phone resting on his chest. The phone lights up and buzzes. He grabs it, reads, and sits bolt upright, a huge grin spreading across his face, and immediately starts typing back with both thumbs. Final frame: Zhandos sitting up on the bed, grinning, typing fast.''',
  cam='''Medium shot from slightly above the bed, 35mm; the camera rises gently as he sits up.''',
  light='''Night: a dim warm desk lamp, the phone's cool glow lighting his face.''',
  perf='''Explosive but natural joy — a second of disbelief, then the grin.''',
  audio='''A phone vibration and message tone, bedsprings as he sits up, quick screen taps. Warm music returns.''',
  cont='''Evening. The phone screen is never readable. His typing here is the invitation to a first date.''',
  avoid="readable phone screen",
  first="Жандос шалқасынан жатыр, телефон кеудесінде.",
  last="Жандос төсекте отырып, күліп, тез жазып жатыр.",
  tr=dict(tech="Музыкалық соққыға кесу + энергия сәйкестігі",
          why="Шақыру → дайындық: Жандостың қуанышы Қарақаттың толқуына ауысады.",
          mech="Жандос «жіберу» батырмасын басқанда гитара тақырыбы басталады; бірінші соққыда Қарақаттың айна алдындағы кадрына кесеміз.",
          match="Кештен келесі күнге; жарық жылырақ.",
          sound="Акустикалық гитара — фильмнің махаббат тақырыбы — осы жерден басталады.",
          where="Монтажда"))

# ===== SCENE 5 =====
C(n=19, scene=5, en="In Front of the Mirror", kk="Айна алдында", gen=10, edit=4,
  cast=[("QA", "QA_DATE")], loc="QA_ROOM",
  shot="Иық үстінен айнаға, баяу жақындау",
  ctx='''Qarakat has agreed to a date and nervously gets ready.''',
  act='''Opening frame: over Qarakat's shoulder into the tall mirror — she is in her navy hoodie with the silver dog-tag pendant; behind her on the bed lie two other outfits she decided against. She smooths the hoodie, re-pins a strand into her high bun, adjusts one silver hoop earring, takes a nervous breath and gives her reflection a small, determined smile. Final frame: her reflection smiling in the mirror.''',
  cam='''Over-the-shoulder into the mirror, 50mm, slow subtle push-in, focus on her reflection.''',
  light='''Late-afternoon window light, soft and warm from screen-left.''',
  perf='''Nervous excitement: small fidgets, a breath, then quiet confidence.''',
  audio='''Fabric rustle, a hairpin click, the warm acoustic guitar theme.''',
  cont='''Date day. Her reflection must match her exactly; keep her face as in the reference.''',
  avoid="mismatched mirror reflection, a second person in the room",
  first="Айнадағы Қарақат; артында, төсекте таңдалмай қалған киімдер.",
  last="Айнадағы бейнесі жымияды.",
  tr=dict(tech="Параллель қимыл сәйкестігі (action match)",
          why="Екеуі де бір-бірі үшін дайындалып жатыр — бір қимыл оларды байланыстырады.",
          mech="Қарақат сырғасын түзеген қимылдан Жандостың жағасын түзеген қимылына кесеміз.",
          match="Қолдың қимылы мен кадр өлшемі ұқсас.",
          sound="Гитара тақырыбы үздіксіз.",
          where="Монтажда"))

C(n=20, scene=5, en="He Waits", kk="Ол күтіп тұр", gen=5, edit=3,
  cast=[("ZH", "ZH_DATE")], loc="CINEMA_EXT",
  shot="Орта план, статикалық",
  ctx='''Zhandos waits for Qarakat in front of the cinema for their first date.''',
  act='''Opening frame: medium shot of Zhandos standing in front of the lit cinema, straightening his black three-stripe hoodie and smoothing his hair. He checks the time on his phone, puts it in his pocket, then looks up to screen-right — and his face lights up with a nervous smile as he sees her approaching. Final frame: Zhandos smiling toward screen-right.''',
  cam='''Medium shot at eye level, 50mm, static, shallow depth of field.''',
  perf='''Nervous anticipation melting into a shy smile.''',
  audio='''Evening city ambience, distant traffic; the guitar theme continues.''',
  cont='''First-date evening. Eyeline screen-right — Qarakat arrives from screen-right in the next shot.''',
  avoid="readable cinema signage or film posters",
  first="Жандос кинотеатр алдында жағасын түзеп тұр.",
  last="Жандос оң жаққа қарап жымияды.",
  tr=dict(tech="Көзқарас бойынша монтаж (eye match)",
          why="Біз Қарақатты Жандостың көзімен көреміз.",
          mech="Жандостың оңға қараған көзқарасынан Қарақат оң жақтан келе жатқан кадрға кесеміз.",
          match="Көзқарас — оңға; Қарақат оң жақтан кіреді.",
          sound="Гитара тақырыбы, көше шуы.",
          where="Монтажда"))

C(n=21, scene=5, en="The First Meeting", kk="Кездесу", gen=10, edit=4,
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], loc="CINEMA_EXT",
  shot="Екі адамдық орта-жалпы план, баяу жақындау",
  ctx='''Zhandos and Qarakat meet for their first date; both are shy.''',
  act='''Opening frame: Zhandos at screen-left; Qarakat walks in from screen-right and stops in front of him. A shy pause; they both smile, look down, then up at each other. He gives a small awkward wave, she laughs softly and tucks her hands into her sleeves. He gestures toward the cinema entrance and they turn and walk together screen-left toward it. Final frame: the two of them walking side by side toward the glowing entrance, seen in a three-quarter back view.''',
  cam='''Medium-wide two-shot at eye level, 35mm, a slow push-in during the greeting, then holding as they walk away.''',
  perf='''First-date shyness: small smiles, quick glances, an awkward but sweet laugh. No dialogue — everything is in the looks.''',
  audio='''City evening ambience, their soft laughter (no clear words), the guitar theme.''',
  cont='''From this shot to the end of the film Zhandos is always screen-left and Qarakat screen-right whenever they are together.''',
  avoid="readable signage, film posters",
  first="Жандос солда; Қарақат оң жақтан келіп тоқтайды.",
  last="Екеуі кинотеатрға қарай қатар кетіп барады.",
  tr=dict(tech="Жарық арқылы өту (light transition)",
          why="Көшенің жылы шамдарынан кинозалдың жыпылықтаған жарығына — орын да, уақыт та ауысады.",
          mech="Олар кіреберістің жарығына енген сәтте кесеміз → B клип қараңғы залда, экран жарығы жүздерінде жыпылықтап басталады.",
          match="Жандос солда, Қарақат оңда — орындары сақталады.",
          sound="Көше шуы кесіледі; залдың тыныш күңгірі.",
          where="Монтажда"))

C(n=22, scene=5, en="At the Cinema", kk="Кинода", gen=5, edit=3,
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], loc="CINEMA",
  shot="Екі адамдық орта план, алдынан",
  ctx='''On their first date they watch a film together.''',
  act='''Opening frame: Zhandos (screen-left) and Qarakat (screen-right) sitting side by side in the dark, lit by the flickering light of the screen in front of them. Qarakat steals a sideways glance at him; he notices and turns his head; their eyes meet for a second, both smile and look back at the screen. Final frame: both looking forward, smiling.''',
  cam='''Medium two-shot from the front, as if from below the screen, 50mm, static.''',
  perf='''A tiny, sweet moment of mutual awareness; restrained.''',
  audio='''The muffled, indistinct sound of a film playing (no recognisable music or dialogue), a quiet audience.''',
  cont='''Date evening. Zhandos screen-left, Qarakat screen-right.''',
  avoid="the cinema screen or any film footage visible in frame",
  first="Қараңғы зал; экран жарығы екеуінің жүзінде.",
  last="Екеуі экранға қарап жымиып отыр.",
  tr=dict(tech="Ырғақпен кесу (музыка соққысына)",
          why="Кездесудің үш орны — бір әуеннің үш тактысы.",
          mech="Олардың жымиған сәтінде, гитара соққысына кафе кадрына кесеміз.",
          match="Жандос солда, Қарақат оңда; жылы жарыққа ауысу.",
          sound="Гитара тақырыбы.",
          where="Монтажда"))

C(n=23, scene=5, en="At the Café", kk="Кафеде", gen=5, edit=3,
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], loc="CAFE2",
  shot="Екі адамдық орта план, бүйірден",
  ctx='''After the film they talk in a café.''',
  act='''Opening frame: a side view of a small wooden table; Zhandos (screen-left) tells a story animatedly with his hands; Qarakat (screen-right) laughs, covering her mouth with her hand, then leans forward to listen. Final frame: Qarakat leaning forward, still smiling, eyes on him.''',
  cam='''Medium two-shot from the side, 50mm, static, warm bokeh behind.''',
  perf='''Relaxed and natural; the ice has broken.''',
  audio='''Soft café murmur, cups, their laughter (no clear words), the guitar theme.''',
  cont='''Same date evening. Zhandos screen-left, Qarakat screen-right.''',
  first="Кафе үстелі: Жандос бір нәрсе айтып отыр, Қарақат күледі.",
  last="Қарақат алға еңкейіп, оған қарап тыңдап отыр.",
  tr=dict(tech="Алдыңғы планмен жабу (foreground occlusion)",
          why="Сөре кадрды жауып өтіп, бір орыннан екіншісіне үзіліссіз әкеледі.",
          mech="B клип кітап сөресінің шеті кадрды жауып өтуінен басталады (камера сөре бойымен жылжиды) — A клиптің соңына тікелей жалғанады.",
          match="Жылы жарық; Жандос солда, Қарақат оңда.",
          sound="Кафе шуы → кітап парақтарының сыбдыры.",
          where="Генерацияда (сөренің жабуы) + монтажда"))

C(n=24, scene=5, en="At the Bookstore", kk="Кітап дүкенінде", gen=5, edit=3,
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], loc="BOOK",
  shot="Орта план, сөре бойымен бүйірден жылжу",
  ctx='''They wander through a bookstore together.''',
  act='''Opening frame: the end of a wooden bookshelf passes across the lens, revealing Zhandos (screen-left) and Qarakat (screen-right) in the aisle. Qarakat pulls a book from the shelf and shows him the cover; he leans in close to look; their shoulders touch and they share a smile. Final frame: the two standing shoulder to shoulder, smiling over the book.''',
  cam='''Medium shot, a slow lateral track to the right along the shelves, 50mm, starting with the shelf as a foreground wipe.''',
  perf='''Growing closeness; the shoulder touch is natural and unforced.''',
  audio='''A quiet bookstore, pages rustling, the guitar theme.''',
  cont='''Same date evening. Book covers and spines are plain and unreadable.''',
  avoid="readable book titles or text",
  first="Сөренің шеті кадрды жауып өтіп, екеуі көрінеді.",
  last="Екеуі иық тірестіріп, кітапқа қарап жымиып тұр.",
  tr=dict(tech="Біртіндеп ауысу (cross dissolve) — уақыттың өтуі",
          why="Кеш батып, түн түскенін жұмсақ ауысу жақсы береді.",
          mech="1 секундтық dissolve: дүкеннің жылы жарығы түнгі көше шамына ұласады.",
          match="Жандос солда, Қарақат оңда.",
          sound="Гитара тақырыбы баяулап, түнгі тыныштыққа ауысады.",
          where="Монтажда"))

C(n=25, scene=5, en="The Goodbye Hug", kk="Қоштасу", gen=10, edit=6,
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], loc="QA_EXT",
  shot="Екі адамдық орта-жалпы план, статикалық",
  ctx='''Zhandos walks Qarakat home; at the door she shyly hugs him and goes inside.''',
  act='''Opening frame: Zhandos (screen-left) and Qarakat (screen-right) walk up the short path and stop at the foot of the steps to her building entrance. A shy, silent pause; they look at each other, then away. Suddenly Qarakat steps in and gives him a quick hug, then turns, runs up the three steps and goes inside; the glass door closes behind her. Final frame: Zhandos alone at the foot of the steps, facing the closed, lit door, surprised.''',
  cam='''Medium-wide two-shot at eye level, 35mm, static.''',
  perf='''Tender awkwardness, then her brave, quick hug — she is shy and fast; he is frozen in happy surprise.''',
  audio='''A quiet night street, footsteps, the door closing with a soft click; the guitar theme pauses.''',
  cont='''Night, the end of the first date. Zhandos screen-left, Qarakat screen-right.''',
  first="Олар есік алдына келіп тоқтайды.",
  last="Жандос жабылған есік алдында жалғыз, таңданып тұр.",
  tr=dict(tech="Реакциялық монтаж",
          why="Бұл сәттің ең маңыздысы — оның реакциясы.",
          mech="Есік сырт етіп жабылған сәтте Жандостың ірі планына кесеміз.",
          match="Шам жарығы — сол жақтан; түн.",
          sound="Есіктің сырт еткені → тыныштық → оның ақырын күлкісі.",
          where="Монтажда"))

C(n=26, scene=5, en="He Can't Stop Smiling", kk="Күлімсіреп қалды", gen=5, edit=3,
  cast=[("ZH", "ZH_DATE")], loc="QA_EXT",
  shot="Ірі план, статикалық",
  ctx='''Zhandos stands outside her door, overwhelmed with happiness.''',
  act='''Opening frame: close-up of Zhandos under the street lamp, still surprised, looking at the closed door. The surprise slowly melts into a wide, quiet smile; he looks down and shakes his head with a soft laugh. Final frame: Zhandos smiling to himself, eyes lowered.''',
  cam='''Close-up, 85mm portrait feel, static, shallow depth of field.''',
  perf='''Disbelief turning into happiness; the laugh is small and private.''',
  audio='''Night quiet, his soft laugh; the guitar theme returns and swells into the montage song.''',
  cont='''Same night.''',
  first="Жандостың ірі планы, жабық есікке қарап тұр.",
  last="Жандос өзіне-өзі жымиып, төмен қарайды.",
  tr=dict(tech="Жүз сәйкестігі (match cut)",
          why="Сол бір күлкі монтажға ұласады: «содан бері ол жиі осылай жымиды».",
          mech="Жандостың күлкісінің ірі планынан түнгі қоңырау кезіндегі оның жымиған ірі планына кесеміз (басы кадрдың бір орнында).",
          match="Жүздің орны, өлшемі, күлкі.",
          sound="Монтаждың әні толық басталады.",
          where="Монтажда"))

# ===== SCENE 6 (montage) =====
C(n=27, scene=6, en="Midnight Call — Zhandos", kk="Түнгі қоңырау — Жандос", gen=5, edit=4,
  cast=[("ZH", "ZH_SPORT")], loc="ZH_ROOM",
  shot="Ірі план, жастық деңгейінде (бөлінген экранның сол жағы)",
  ctx='''Montage of their happy days: talking on the phone until midnight.''',
  act='''Opening frame: Zhandos lying on his side on his bed in the dark, facing screen-right, his phone held to his ear. He listens, laughs quietly, closes his eyes for a moment and smiles. Final frame: Zhandos lying still, eyes closed, smiling, the phone at his ear.''',
  cam='''Close-up at pillow level, 50mm, static. Compose him in the left half of the frame (it will sit in a split screen).''',
  light='''Night: cool blue moonlight from the window plus a very faint warm lamp; soft low-key look.''',
  perf='''Sleepy, tender happiness.''',
  audio='''No dialogue — only soft breathing and a quiet laugh; the montage song plays over it in editing.''',
  cont='''Night. He faces screen-right, mirrored by Qarakat facing screen-left in the paired shot.''',
  first="Жандос қараңғыда бүйірінен жатып, телефонмен сөйлесіп жатыр.",
  last="Жандос көзін жұмып, жымиып жатыр.",
  tr=dict(tech="Экранды екіге бөлу (split screen)",
          why="Екеуі бір уақытта, бөлек төсекте — бірақ бір әңгімеде; «сағыну» сезімі кадрдың өзінде.",
          mech="27-клип экранның сол жартысында, 28-клип оң жартысында қатар жүреді — бір-біріне қарап жатқандай.",
          match="Ол оңға, ол солға қарап жатыр; жарық бірдей.",
          sound="Ән үздіксіз.",
          where="Монтажда"))

C(n=28, scene=6, en="Midnight Call — Qarakat", kk="Түнгі қоңырау — Қарақат", gen=5, edit=0,
  cast=[("QA", "QA_SPORT")], loc="QA_ROOM",
  shot="Ірі план, жастық деңгейінде (бөлінген экранның оң жағы)",
  ctx='''Montage of their happy days: talking on the phone until midnight, missing each other.''',
  act='''Opening frame: Qarakat lying on her side on her bed in the dark, facing screen-left, her phone at her ear, hugging a pillow to her chest. She laughs quietly into the pillow, then gazes ahead, smiling, missing him. Final frame: Qarakat hugging the pillow, smiling, eyes half-closed.''',
  cam='''Close-up at pillow level, 50mm, static. Compose her in the right half of the frame (it will sit in a split screen).''',
  light='''Night: cool blue moonlight from the window plus a very faint warm lamp; soft low-key look.''',
  perf='''Tender, a little longing.''',
  audio='''No dialogue — only soft breathing and a quiet laugh.''',
  cont='''Night. She faces screen-left, mirroring Zhandos.''',
  first="Қарақат жастықты құшақтап, телефонмен сөйлесіп жатыр.",
  last="Қарақат жастықты құшақтап, жымиып жатыр.",
  tr=dict(tech="Жарық арқылы өту (түннен күн жарығына)",
          why="Түнгі сағыныштан — бірге өткен жарқын күнге.",
          mech="Бөлінген экран жабылып, ашық далаға тікелей кесеміз; жарықтың кенет өзгерісі әннің соққысына түседі.",
          match="Екеуі енді бір кадрда — бірге.",
          sound="Әннің қайырмасы осы жерден басталады.",
          where="Монтажда"))

C(n=29, scene=6, en="Horseback Riding", kk="Атқа міну", gen=5, edit=3,
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT")], loc="STEPPE",
  shot="Жалпы-орта план, бүйірден қатар ілесу",
  ctx='''Montage: they go horseback riding together.''',
  act='''Opening frame: Zhandos (screen-left, further from camera) and Qarakat (screen-right, nearer) ride two calm brown horses side by side at a slow walk, moving left to right across golden steppe grass. Qarakat laughs and looks over at him; he grins back and points ahead at the horizon. Final frame: both riding side by side, smiling.''',
  cam='''Wide-to-medium tracking shot alongside them, moving left to right at their pace, 35mm, smooth.''',
  perf='''Carefree and playful.''',
  audio='''Hooves on dry grass, wind, horses snorting softly; the montage song.''',
  cont='''Daytime. The horses walk calmly with a realistic gait.''',
  avoid="unnatural horse legs or gait, extra riders",
  first="Екеуі далада аттармен қатар келе жатыр.",
  last="Екеуі жымиып, қатар серуендеп барады.",
  tr=dict(tech="Ырғақпен кесу",
          why="Монтаж әннің ырғағымен жүреді — бір соққы, бір естелік.",
          mech="Келесі соққыда диван кадрына кесеміз.",
          match="Жандос солда, Қарақат оңда (бүкіл монтажда сақталады).",
          sound="Ән.",
          where="Монтажда"))

C(n=30, scene=6, en="Movie Night", kk="Үйдегі кино кеші", gen=5, edit=3,
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT")], loc="LIVING",
  shot="Екі адамдық орта план, алдынан",
  ctx='''Montage: they watch a film together at home (the film itself is never shown).''',
  act='''Opening frame: Zhandos (screen-left) and Qarakat (screen-right) sitting close together on a grey sofa under a knitted blanket, a bowl of popcorn between them, watching the TV that is off-frame in front of them; its changing light plays across their faces. Qarakat slowly rests her head on his shoulder; he smiles and leans his head gently against hers. Final frame: her head on his shoulder, both watching.''',
  cam='''Medium two-shot from the front (from the TV's position), 50mm, static.''',
  perf='''Comfortable, intimate, unhurried.''',
  audio='''Indistinct TV sound (no recognisable film audio), popcorn crunch; the montage song.''',
  cont='''Night. The TV screen is never visible.''',
  avoid="the TV screen or any film footage in frame, recognisable film characters or logos",
  note="Сценарийде бұл — «Гарри Поттер» кеші. Авторлық құқыққа байланысты фильмнің өзі кадрда көрсетілмейді.",
  first="Диванда көрпе астында қатар отыр, теледидар жарығы жүздерінде.",
  last="Қарақаттың басы Жандостың иығында.",
  tr=dict(tech="Ырғақпен кесу + қимыл сәйкестігі",
          why="Бір-біріне еңкейген қимыл келесі кадрда жалғасады.",
          mech="Қарақат басын иығына қойған қимылдан — кафеде оған қарай еңкейген сәтке кесеміз.",
          match="Жандос солда, Қарақат оңда.",
          sound="Ән.",
          where="Монтажда"))

C(n=31, scene=6, en="Another Café", kk="Тағы бір кафе", gen=5, edit=3,
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], loc="CAFE3",
  shot="Екі адамдық орта план, бүйірден",
  ctx='''Montage: one of the many cafés they visit together.''',
  act='''Opening frame: Zhandos (screen-left) and Qarakat (screen-right) at a marble table by a sunny window, two cups of coffee and a slice of cake between them. They lean toward each other, clink their coffee cups and both laugh. Final frame: both laughing, leaning toward each other.''',
  cam='''Medium two-shot from the side, 50mm, static.''',
  perf='''Easy, playful, in love.''',
  audio='''Café murmur, the clink of cups; the montage song.''',
  cont='''Daytime.''',
  first="Күн сәулелі терезе жанында кофе мен торт.",
  last="Екеуі күліп, бір-біріне қарай еңкейген.",
  tr=dict(tech="Ырғақпен кесу + жарықтың ауысуы (күн → түн)",
          why="Күндізгі кафеден түнгі көшеге — бір махаббаттың көп күні.",
          mech="Келесі соққыда түнгі көшеде камераға қарай келе жатқан кадрға кесеміз.",
          match="Жандос солда, Қарақат оңда.",
          sound="Ән.",
          where="Монтажда"))

C(n=32, scene=6, en="Night Walk", kk="Түнгі серуен", gen=5, edit=3,
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], loc="STREET",
  shot="Екі адамдық орта план, алдынан шегіне ілесу",
  ctx='''Montage: walking the city streets hand in hand.''',
  act='''Opening frame: Zhandos (screen-left) and Qarakat (screen-right) walk hand in hand toward the camera along a night street, swinging their joined hands, laughing and looking at each other. Final frame: still walking, she leans her head toward his shoulder.''',
  cam='''Medium two-shot, the camera moving backward ahead of them at walking pace, 35mm, steady.''',
  perf='''Light, happy, completely at ease together.''',
  audio='''Night street ambience, footsteps; the montage song reaches its end.''',
  cont='''Night. Their hands are joined between them (his left hand, her right hand).''',
  avoid="readable shop signs",
  first="Олар түнгі көшеде қол ұстасып, камераға қарай келе жатыр.",
  last="Қарақат басын оның иығына қарай иеді.",
  tr=dict(tech="Біртіндеп ауысу (cross dissolve) — уақыттың ұзақ өтуі",
          why="Монтаж аяқталып, шарықтау шегіне — ұсыныс күніне өтеміз.",
          mech="1,5 секундтық dissolve: түнгі көше шамдары теңіздегі күн батудың алтын жарығына ұласады.",
          match="Жандос солда, Қарақат оңда — ұсыныс сахнасында да солай.",
          sound="Монтаж әні сөніп, толқын дыбысы мен ішекті аспаптардың баяу әуені кіреді.",
          where="Монтажда"))

# ===== SCENE 7 =====
C(n=33, scene=7, en="The Seaside Picnic", kk="Теңіз жағасы", gen=10, edit=5,
  cast=[("ZH", "ZH_SEA"), ("QA", "QA_SEA")], loc="BEACH",
  shot="Артынан жалпы план → баяу жақындау",
  ctx='''The proposal day: Zhandos has prepared a picnic on the seashore at sunset.''',
  act='''Opening frame: a wide shot from behind the couple — Zhandos (screen-left) and Qarakat (screen-right) sitting side by side on cushions at the low picnic table on the sand, facing the calm sea and the low sun; the flowers, sweets and glowing candle jars are on the table. They talk quietly; Qarakat laughs and leans her shoulder against his. Final frame: closer — the two of them silhouetted against the golden sea, her shoulder against his.''',
  cam='''Wide shot from behind at seated eye level, 35mm, one slow steady push-in toward them across the whole shot.''',
  perf='''Calm, warm, intimate; she has no idea what is coming; he is quietly nervous.''',
  audio='''Gentle waves, a light sea breeze, soft indistinct talk and her laugh; slow strings begin.''',
  cont='''Sunset. Zhandos always screen-left, Qarakat always screen-right. The sea is in front of them.''',
  avoid="other people on the beach, lens flares, oversaturated sky",
  first="Артынан жалпы план: екеуі теңізге қарап, пикник үстелінің жанында отыр.",
  last="Жақынырақ: алтын теңіз аясында екеуінің силуэті.",
  tr=dict(tech="Камераның табиғи қозғалысы (push-in жалғасы)",
          why="Камера оларға жақындай береді — көрермен де сол сәтке жақындайды.",
          mech="A клиптің баяу жақындауы B клипте Қарақаттың иығы үстінен Жандосқа түсірілген жақын кадрмен жалғасады.",
          match="Жандос солда, Қарақат оңда; күн артқы фонда.",
          sound="Толқын мен ішекті аспаптар үздіксіз.",
          where="Монтажда"))

C(n=34, scene=7, en="The Day I First Saw You", kk="«Сені алғаш көрген күнім…»", gen=10, edit=10,
  cast=[("ZH", "ZH_SEA"), ("QA", "QA_SEA")], loc="BEACH",
  shot="Қарақаттың иығы үстінен Жандосқа, орта-ірі план",
  ctx='''Zhandos takes Qarakat's hand and begins to speak from the heart.''',
  act='''Opening frame: over Qarakat's right shoulder (soft in the right foreground: her high bun and a silver hoop earring) onto Zhandos, who has turned toward her. He takes her hand in both of his, looks into her eyes and speaks slowly and sincerely. Final frame: Zhandos holding her hand, looking into her eyes, swallowing nervously.''',
  cam='''Over-the-shoulder medium close-up on Zhandos, 85mm portrait feel, shallow depth of field, static with a barely perceptible drift; the sunset sea softly blurred behind him.''',
  light='''Warm low sun as a rim light on his hair and shoulders, soft warm candle fill on his face, natural skin texture.''',
  perf='''Sincere, a little nervous, steady eye contact; no theatrical emotion — the words carry it.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ZHANDOS (slow, sincere, warm): "Білесің бе, сені алғаш көрген күнім әлі есімде. Сол кезде сенің бір күнің менің бүкіл өмірімді өзгертетінін білмеппін." Gentle waves; the strings drop very low under his voice.''',
  cont='''Sunset, same picnic. Zhandos screen-left facing right; Qarakat screen-right facing left (her shoulder in the foreground).''',
  first="Қарақаттың иығы үстінен Жандос; ол оның қолын алады.",
  last="Жандос оның қолын ұстап, көзіне қарап тұр.",
  tr=dict(tech="Кадр / кері кадр + L-cut (дыбыс созылады)",
          why="Сөздің екінші жартысында маңыздысы — оны тыңдап отырған Қарақаттың жүзі.",
          mech="Жандостың даусы үзілмей, Қарақаттың ірі планына кесеміз; оның сөзі кадр сыртынан жалғасады.",
          match="180° сызығы: Жандос солда, Қарақат оңда; күн жарығы бір жақтан.",
          sound="Жандостың даусы мен толқын екі клипке ортақ.",
          where="Монтажда"))

C(n=35, scene=7, en="A Step Into the Future", kk="«Болашаққа қадам басқым келеді…»", gen=10, edit=9,
  cast=[("QA", "QA_SEA"), ("ZH", "ZH_SEA")], loc="BEACH",
  shot="Жандостың иығы үстінен Қарақатқа, ірі план",
  ctx='''Qarakat listens as Zhandos continues; she remembers how hard he tried.''',
  act='''Opening frame: over Zhandos's left shoulder (soft in the left foreground, black hoodie with white sleeve stripes) onto Qarakat, who is listening, her hand in his. Zhandos, seen from behind, keeps speaking. When he mentions how hard he tried, Qarakat lets out a small laugh, remembering; then her face grows serious and her eyes begin to glisten. Final frame: close-up of Qarakat, eyes shining, lips slightly parted, waiting.''',
  cam='''Over-the-shoulder close-up on Qarakat, 85mm portrait feel, shallow depth of field, static.''',
  light='''Warm sunset light on her face, soft candle fill, a gentle rim on her hair; realistic skin texture.''',
  perf='''Listening is the performance: a small laugh of recognition, then deep emotion held back — real, not melodramatic.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words by ZHANDOS, whose back is to the camera (no lip-sync needed): "Басында сенімен танысу үшін қанша тырысқанымды өзің де білесің. Бүгін сенімен бірге болашаққа қадам басқым келеді..." Waves; the strings slowly rising.''',
  cont='''Sunset, same picnic. Qarakat screen-right facing left.''',
  first="Жандостың иығы үстінен Қарақат; ол тыңдап отыр.",
  last="Қарақаттың көзі жасаурап, күтіп отыр.",
  tr=dict(tech="Қимыл үстіндегі монтаж (қол қалтаға)",
          why="Сөз аяқталды — енді әрекет.",
          mech="B клип Жандостың қалтасынан сақина қорабын шығарған қимылынан басталады.",
          match="Позициялар мен жарық сақталады.",
          sound="Ішекті аспаптар көтеріліп, кенет тынады — сұрақтың алдындағы тыныштық.",
          where="Монтажда"))

C(n=36, scene=7, en="Will You?", kk="«Келісесің бе?»", gen=10, edit=7,
  cast=[("ZH", "ZH_SEA"), ("QA", "QA_SEA")], loc="BEACH",
  shot="Екі адамдық орта план, профильден",
  ctx='''Zhandos takes out the ring and asks Qarakat to be his partner for life.''',
  act='''Opening frame: a medium two-shot in profile — Zhandos (screen-left) facing Qarakat (screen-right), the sunset sea behind them. Zhandos takes a small dark ring box from his pocket and opens it toward her, revealing a simple, elegant ring, and asks his question. Qarakat's hand rises to her mouth. Final frame: Zhandos holding the open ring box; Qarakat with her hand over her mouth, eyes filling with tears.''',
  cam='''Medium two-shot in profile, 50mm, static, the sun low on the horizon between them.''',
  light='''Golden backlight from the low sun, faces gently lit by the candles, natural skin.''',
  perf='''His voice slightly unsteady; her reaction is real surprise and emotion, not exaggerated.''',
  audio='''Kazakh dialogue, spoken in Kazakh with these exact words — ZHANDOS (quiet, nervous, hopeful): "Қарақат, менің өмірлік серігім болуға келісесің бе?" Then near-silence: only the waves.''',
  cont='''Sunset. The ring is a simple gold band with a small stone.''',
  avoid="an oversized or glowing ring, magical sparkles",
  first="Профильдегі екі адамдық кадр; Жандос қорапты шығарады.",
  last="Жандос ашық қорапты ұстап тұр; Қарақат аузын жауып, көзіне жас алған.",
  tr=dict(tech="Соңғы кадр → бастапқы кадр (first/last frame) + қимыл үстіндегі монтаж",
          why="Жауап сәті үзілмеуі керек — қол, қорап, жарық бәрі сәйкес болсын.",
          mech="A клиптің соңғы кадры B клиптің бастапқы суреті ретінде беріледі.",
          match="Қорап, қолдар, жарық дәл сәйкес.",
          sound="Толқын; ол басын изеген сәтте музыка толқып көтеріледі.",
          where="Екеуінде де: генерацияда және монтажда"))

C(n=37, scene=7, en="Yes", kk="«Иә»", gen=10, edit=7,
  cast=[("QA", "QA_SEA"), ("ZH", "ZH_SEA")], loc="BEACH",
  shot="Жақын екі адамдық кадр, өте баяу жақындау",
  ctx='''Qarakat says yes with a nod, and Zhandos puts the ring on her finger.''',
  act='''Opening frame: a close two-shot — Zhandos (screen-left) holding the open ring box, Qarakat (screen-right) with her hand over her mouth and tears in her eyes. She lowers her hand, smiles through her tears and nods several times. Zhandos, beaming, takes the ring out and gently slides it onto her ring finger. They both look down at the ring, then up into each other's eyes. Final frame: their faces close together, both smiling, her hand with the ring held in his.''',
  cam='''Close two-shot, 85mm portrait feel, static with a very slow push-in, shallow depth of field.''',
  light='''Golden sunset rim light, warm candle fill, natural skin texture, real tears.''',
  perf='''The emotional climax: genuine, restrained joy — tears and a smile together, a relieved exhale from him.''',
  audio='''No words. Waves; the strings swell warmly as she nods.''',
  cont='''Sunset. From now on the ring stays on her ring finger.''',
  avoid="distorted fingers, the ring changing shape, extra hands",
  first="Қарақат аузын жауып отыр; Жандоста ашық қорап.",
  last="Жүздері жақын, екеуі жымиып тұр; оның сақиналы қолы Жандостың қолында.",
  tr=dict(tech="Қимыл сәйкестігі (құшаққа ұмтылу)",
          why="Олардың бір-біріне жақындауы құшақпен жалғасады.",
          mech="Олар бір-біріне еңкейе бастаған сәтте кесеміз → B клип құшақтасқан сәттен басталады.",
          match="Позициялар мен жарық сақталады.",
          sound="Ішекті аспаптар шарықтау шегінде.",
          where="Монтажда"))

C(n=38, scene=7, en="Embrace and Sunset", kk="Құшақ және күн батуы", gen=10, edit=7,
  cast=[("ZH", "ZH_SEA"), ("QA", "QA_SEA")], loc="BEACH",
  shot="Орта план → жоғары көтерілген жалпы план (шегіну)",
  ctx='''They embrace; the camera pulls away to reveal the sea and the setting sun.''',
  act='''Opening frame: medium shot of Zhandos and Qarakat embracing beside the picnic table, her chin on his shoulder, eyes closed, smiling. The camera slowly pulls back and rises, revealing the glowing candles and flowers of the picnic, then the wide empty beach, the calm sea and the sun touching the horizon. Final frame: a wide shot — the small embracing couple beside their glowing picnic on the shore, the sun on the horizon.''',
  cam='''One smooth, slow pull-back and rise like a crane move, from medium to wide; 35mm; stable and graceful, no spinning.''',
  light='''The sun touching the horizon, a golden-pink sky, the candles glowing warmer as the light fades.''',
  perf='''Stillness and relief; they hold each other without moving much.''',
  audio='''Waves, the strings resolving into a warm chord.''',
  cont='''Sunset. The ring on her finger. Zhandos on the left, Qarakat on the right.''',
  avoid="lens flares, other people on the beach, a drone circling them",
  first="Олар құшақтасып тұр; Қарақаттың иегі оның иығында.",
  last="Жалпы план: теңіз жағасындағы кішкентай жұп, күн көкжиекте.",
  tr=dict(tech="Біртіндеп ауысу (cross dissolve) — уақыттың өтуі",
          why="Ұсыныстан тойға — фильмдегі ең маңызды уақыт секірісі, ол жұмсақ болуы керек.",
          mech="1,5 с dissolve: күн батудың алтын жарығы қалыңдық бөлмесінің ақ терезе жарығына ұласады.",
          match="Жылы жарықтан ақ-алтын реңкке.",
          sound="Ішекті аккорд салтанатты той әуеніне ұласады.",
          where="Монтажда"))

# ===== SCENE 8 =====
C(n=39, scene=8, en="The Wedding Dress", kk="Той көйлегі", gen=5, edit=3,
  cast=[("QA", "QA_BRIDE")], groups=["HELP"], loc="BRIDE_ROOM",
  shot="Иық үстінен айнаға, орта план",
  ctx='''Wedding preparations: Qarakat in her wedding gown.''',
  act='''Opening frame: Qarakat in her white wedding gown stands in front of a full-length mirror; a helper's hands (face not shown) fasten the last buttons at the back of the gown. Qarakat smooths the skirt with both hands, looks at her reflection and takes an emotional breath, smiling. Final frame: her reflection in the mirror, smiling, the veil falling from her high bun.''',
  cam='''Medium shot over her shoulder into the mirror, 50mm, slow subtle push-in.''',
  perf='''Emotional, quiet happiness.''',
  audio='''Fabric rustle; the celebratory wedding music.''',
  cont='''Wedding day. She faces screen-right in the mirror composition.''',
  avoid="mismatched mirror reflection, the helper's face",
  first="Қарақат ақ көйлекпен айна алдында; біреудің қолдары артынан түйме салып жатыр.",
  last="Айнадағы бейнесі жымияды.",
  tr=dict(tech="Параллель қимыл (айналық композиция)",
          why="Екеуі бір мезетте дайындалып жатыр.",
          mech="Ол оңға қараған айна кадрынан сол жаққа қараған Жандостың айна кадрына кесеміз.",
          match="Айналық симметрия.",
          sound="Той әуені.",
          where="Монтажда"))

C(n=40, scene=8, en="The Suit", kk="Костюм", gen=5, edit=3,
  cast=[("ZH", "ZH_SUIT")], loc="GROOM_ROOM",
  shot="Айнаға қараған орта план, статикалық",
  ctx='''Wedding preparations: Zhandos puts on his suit.''',
  act='''Opening frame: Zhandos in his black suit stands in front of a mirror, buttoning his jacket, then straightening his black tie; he meets his own eyes in the mirror and takes a confident breath with a small smile. Final frame: Zhandos looking at himself, ready.''',
  cam='''Medium shot into the mirror, 50mm, static.''',
  perf='''Calm, proud, a little nervous underneath.''',
  audio='''Fabric rustle; the wedding music.''',
  cont='''Wedding day. He faces screen-left in the mirror composition, mirroring Qarakat's shot.''',
  avoid="mismatched mirror reflection",
  first="Жандос айна алдында костюмінің түймесін салып тұр.",
  last="Жандос айнаға қарап тұр — дайын.",
  tr=dict(tech="Пішін сәйкестігі (shape match)",
          why="Дөңгелек пішін — сақина — тойдың символы.",
          mech="Костюм түймесінің дөңгелек пішінінен сақиналардың дөңгелегіне кесеміз.",
          match="Дөңгелек пішін кадрдың ортасында.",
          sound="Той әуені.",
          where="Монтажда"))

C(n=41, scene=8, en="The Rings", kk="Сақиналар", gen=5, edit=2,
  cast=[], loc="TABLE",
  shot="Детальды ірі план (макро), бүйірге баяу жылжу",
  ctx='''Wedding preparations: the wedding rings.''',
  act='''Opening frame: an extreme close-up of two simple gold wedding bands resting in an open white velvet ring box on the white table. The camera glides slowly to the side; window light catches the gold. Final frame: the two rings side by side with a soft focus fall-off.''',
  cam='''Macro extreme close-up, a slow lateral slide, very shallow depth of field.''',
  audio='''The wedding music.''',
  cont='''Wedding day. Two plain gold bands.''',
  avoid="people, hands, text on the box, glowing or magical sparkles",
  first="Ақ барқыт қораптағы екі алтын сақина.",
  last="Сақиналар қатар, жұмсақ фокуста.",
  tr=dict(tech="Фокус арқылы өту (rack focus, монтажда)",
          why="Жұмсақ фокус келесі кадрдың жұмсақ фокусына ұласады.",
          mech="Сақиналар фокустан шығады → гүл шоғы фокусқа кіреді.",
          match="Ақ-алтын реңк.",
          sound="Той әуені.",
          where="Монтажда"))

C(n=42, scene=8, en="The Bouquet", kk="Гүл шоғы", gen=5, edit=2,
  cast=[("QA", "QA_BRIDE")], loc="BRIDE_ROOM",
  shot="Ірі план, фокустың ауысуы",
  ctx='''Wedding preparations: the bride's bouquet.''',
  act='''Opening frame: close-up of Qarakat's hands holding a bridal bouquet of white roses and eucalyptus at waist height against her white gown, the engagement ring on her finger; the image starts softly out of focus and comes into sharp focus as she lifts the bouquet slightly and turns it. Final frame: the bouquet sharp, her gown and the edge of her veil soft behind.''',
  cam='''Close-up, 85mm, a rack focus from soft to sharp, static.''',
  audio='''The wedding music.''',
  cont='''Wedding day. Only her hands, the bouquet and the gown are in frame.''',
  avoid="distorted fingers",
  first="Қалыңдықтың қолындағы ақ раушан гүл шоғы (фокус жұмсақ).",
  last="Гүл шоғы анық, артында көйлек.",
  tr=dict(tech="Камераның табиғи қозғалысы (алға жылжу)",
          why="Камера алға жылжып, бізді той залына «кіргізеді».",
          mech="B клиптегі камераның алға жылжуы музыка ырғағымен басталады.",
          match="Ақ-алтын реңк, жылы жарық.",
          sound="Той әуені үдей түседі.",
          where="Монтажда"))

C(n=43, scene=8, en="The Banquet Hall", kk="Той залы", gen=5, edit=3,
  cast=[], groups=["STAFF"], loc="HALL_W",
  shot="Жалпы план, алға баяу жылжу (dolly)",
  ctx='''Wedding preparations: the banquet hall is being decorated.''',
  act='''Opening frame: a wide shot of the grand banquet hall; the camera glides slowly forward along the aisle between round tables with white tablecloths and gold accents, crystal chandeliers glowing overhead; two staff members in the soft background place the last flower arrangements on a table. Final frame: the camera moving toward the tall double doors at the end of the aisle.''',
  cam='''Wide, a slow steady dolly forward, 24–35mm rectilinear, straight lines kept straight.''',
  audio='''The wedding music building.''',
  cont='''Wedding day.''',
  avoid="fisheye distortion, warped tables or chandeliers, text",
  note="Ұсыныс: залдың безендіруіне қазақы ою-өрнек немесе домбыра сарыны қосылса — фильмге ұлттық нақыш береді (міндетті емес).",
  first="Той залы: дөңгелек үстелдер, люстралар; камера алға жылжиды.",
  last="Камера залдың соңындағы биік есіктерге қарай жылжып барады.",
  tr=dict(tech="Камераның табиғи қозғалысы жалғасады",
          why="Залдан адамдарға — тойдың жүрегіне.",
          mech="Алға жылжу B клипте қонақтарға қарай жалғасады.",
          match="Қозғалыс бағыты — алға.",
          sound="Музыка; қонақтардың күлкісі кіре бастайды.",
          where="Монтажда"))

C(n=44, scene=8, en="Joyful Faces", kk="Қуанышты жүздер", gen=5, edit=3,
  cast=[], groups=["FAM"], loc="HALL_W",
  shot="Орта план, бүйірге баяу жылжу",
  ctx='''The happy faces of both families on the wedding day.''',
  act='''Opening frame: a medium shot of a group of relatives from both families in festive clothes standing near the tables, smiling, hugging each other and applauding toward the doors (off-screen). The camera drifts slowly past them. Final frame: an older woman wiping away a happy tear, a man beside her clapping.''',
  cam='''Medium, a slow lateral drift, 50mm, shallow depth of field.''',
  perf='''Warm, genuine joy; natural, varied reactions.''',
  audio='''Applause, joyful voices (no clear words), the wedding music.''',
  cont='''Wedding day. Zhandos and Qarakat are not in this shot. Everyone looks toward the doors.''',
  avoid="duplicate faces, distorted hands, text",
  note="Нақты той болса, бұл кадрды нағыз туыстардың бейнежазбасымен ауыстырған әлдеқайда жақсы — генератор бөтен адамдардың жүзін ойлап табады.",
  first="Екі жақтың туыстары қол шапалақтап, жымиып тұр.",
  last="Қуаныштан көзіне жас алған апа, жанында қол шапалақтаған кісі.",
  tr=dict(tech="Есік арқылы өту (doorway)",
          why="Барлығы есікке қарап тұр — сол есіктен күйеу мен қалыңдық кіреді.",
          mech="Қонақтардың есікке қарай қол шапалақтауынан ашылған есіктен кіріп келе жатқан жұпқа кесеміз.",
          match="Қонақтардың көзқарасы есікке бағытталған.",
          sound="Қол шапалақ пен музыка шарықтайды.",
          where="Монтажда"))

C(n=45, scene=8, en="Together, Forward", kk="Бірге алға", gen=10, edit=6,
  cast=[("ZH", "ZH_SUIT"), ("QA", "QA_BRIDE")], loc="HALL_W",
  shot="Алдынан шегіне ілесу, жалпы → орта план",
  ctx='''The final shot: Zhandos and Qarakat walk hand in hand toward the camera.''',
  act='''Opening frame: the tall double doors of the banquet hall are open, warm light behind them; Zhandos (screen-left) and Qarakat (screen-right, holding her bouquet in her other hand) walk hand in hand through the doors and down the aisle toward the camera. They glance at each other and smile, then look ahead, radiant. Final frame: a medium shot as they come close to the camera, smiling; warm light fills the frame.''',
  cam='''The camera moves slowly backward ahead of them, from wide to medium, 35mm, steady and graceful.''',
  light='''Warm backlight from the doorway and the chandeliers, white and gold, natural skin texture.''',
  perf='''Joyful, proud, calm; a shared glance and a smile.''',
  audio='''Applause from guests off-screen; the wedding music at its peak.''',
  cont='''Wedding day. Zhandos screen-left, Qarakat screen-right — the same sides as through the whole second half of the film.''',
  avoid="an extra bride or groom, distorted hands, text",
  first="Биік есіктер ашық; Жандос пен Қарақат қол ұстасып кіреді.",
  last="Олар камераға жақын, жымиып тұр; жылы жарық кадрды толтырады.",
  tr=dict(tech="Қараңғыға ауысу (fade to black)",
          why="Фильмнің соңы — финалдық жазуларға тыныш, салтанатты өту.",
          mech="Жарық кадрды толтырған сәттен кейін 1 секундта қараңғыға ауысып, ақ жазулар пайда болады.",
          match="—",
          sound="Той әуенінің соңғы аккорды финалдық жазуларға созылады.",
          where="Монтажда"))

FINAL_CARD = 7  # seconds of end titles, made in editing

SCENE_NAMES = {
    1: "Алғашқы көзқарас", 2: "Араймен танысу", 3: "Нөмір үшін келіссөз",
    4: "Жауапсыз хабарламалар", 5: "Алғашқы кездесу", 6: "Бірге өткен бақытты күндер",
    7: "Теңіз жағасындағы ұсыныс", 8: "Тойға дайындық",
}


# ---------------------------------------------------------------- helpers
def tc(s):
    s = int(round(s))
    return f"{s // 60:02d}:{s % 60:02d}"


def timeline():
    t, out = 0, {}
    for c in CLIPS:
        if c["edit"] == 0:  # split screen with previous clip
            out[c["n"]] = out[c["n"] - 1]
            continue
        out[c["n"]] = (t, t + c["edit"])
        t += c["edit"]
    return out, t


def prompt(c):
    L = [f"Create a photorealistic live-action cinematic shot. Duration: {c['gen']} seconds. Aspect ratio: {ASPECT} (landscape).", ""]
    L += ["STORY CONTEXT:", c["ctx"], ""]
    if c["cast"] or c.get("groups"):
        L.append("CHARACTER IDENTITY:")
        for key, _ in c["cast"]:
            L.append("- " + CHAR[key]["id"])
        for g in c.get("groups", []):
            L.append("- " + GROUP[g])
        L.append("")
    if c["cast"]:
        L.append("WARDROBE & PROPS:")
        for _, w in c["cast"]:
            who, desc, _ = WARD[w]
            L.append(f"- {who}: {desc}")
        L.append("")
    loc_desc, loc_light = LOC[c["loc"]]
    L += ["LOCATION & ENVIRONMENT:", loc_desc, ""]
    L += ["ACTION — ONE CONTINUOUS TAKE:", c["act"], ""]
    L += ["CAMERA:", c["cam"], ""]
    L += ["LIGHTING & COLOR:", c.get("light", loc_light), ""]
    if c.get("perf"):
        L += ["PERFORMANCE & EMOTION:", c["perf"], ""]
    L += ["AUDIO:", c["audio"], ""]
    cont = c["cont"]
    if c["cast"]:
        anchors = []
        for key, w in c["cast"]:
            who = WARD[w][0]
            if key == "QA":
                anchors.append(f"{who} keeps her exact face, the high round bun and the silver hoop earrings")
            elif key == "AR":
                anchors.append(f"{who} keeps her exact face, freckles and the curly chestnut ponytail")
            else:
                anchors.append(f"{who} keeps his exact face and hair")
        cont += " Identity anchors: " + "; ".join(anchors) + "; outfits exactly as listed above."
    L += ["CONTINUITY:", cont, ""]
    L += ["VISUAL QUALITY:", VISUAL, ""]
    avoid = AVOID + (", " + c["avoid"] if c.get("avoid") else "") + "."
    L += ["AVOID:", avoid]
    return "\n".join(L)


# ---------------------------------------------------------------- static Kazakh sections
def bible():
    rows = [
        "| ID | Кейіпкер | Референс сурет | Кесіп алатын бөліктер | Әр кадрда тексерілетін белгі |",
        "|---|---|---|---|---|",
        "| CHARACTER_A | **Жандос** | 1-сурет (`1000098369.jpg`) — ер адам, қара худи | жоғарғы сол жақтағы бет (алдынан) + төменгі ортадағы толық бой | қалың қара шаш, бетіндегі кішкентай меңдер |",
        "| CHARACTER_B | **Қарақат** | 2-сурет (`1000098361.jpg`) — түйілген шаш, күміс сырға | жоғарғы қатардағы бет (алдынан) + төменгі сол жақтағы толық бой + профиль | жоғары түйілген қара шаш, үлкен жұқа күміс сырғалар |",
        "| CHARACTER_C | **Арай** | 3-сурет (`1000098562.jpg`) — бұйра каштан шаш, ақшыл худи | жоғарғы ортадағы бет + төменгі сол жақтағы толық бой | сепкіл, бұйра каштан «құйрық» шаш, ақшыл худи |",
    ]
    ward_rows = ["| Кейіпкер | Сценалар | Киім |", "|---|---|---|"]
    plan = [
        ("Жандос", "1–7", "ZH_SPORT"),
        ("Жандос", "8 — той (сценарий бойынша)", "ZH_SUIT"),
        ("Қарақат", "1–7", "QA_SPORT"),
        ("Қарақат", "8 — той (сценарий бойынша)", "QA_BRIDE"),
        ("Арай", "2–4", "AR_DAY"),
    ]
    for who, sc, w in plan:
        ward_rows.append(f"| {who} | {sc} | {WARD[w][2]} |")
    loc_rows = ["| ID | Орын | Сцена | Жарық / кеңістік |", "|---|---|---|---|",
                "| HALL | Волейбол залы, кеш | 1 | Шығатын есік — әрқашан экранның сол жағында, трибуна — оң жағында |",
                "| HALL_NIGHT / HALL_DAY | Спорт кешенінің алды | 1 (түн), 3 (кешкі алтын шақ) | Есік — оң жақта; көше солдан оңға созылады |",
                "| CAFE | Кафе алды, күндіз | 2 | Бұлтты жұмсақ күн жарығы |",
                "| PARK | Саябақ аллеясы | 2, 4 | Жапырақ арасынан түскен күн |",
                "| ZH_ROOM / QA_ROOM | Екеуінің бөлмелері | 4, 5, 6 | Кеште — үстел шамы мен телефон жарығы |",
                "| CINEMA_EXT, CINEMA, CAFE2, BOOK, QA_EXT | Алғашқы кездесу орындары | 5 | Көкшіл кеш → жылы шамдар |",
                "| STEPPE, LIVING, CAFE3, STREET | Монтаж орындары | 6 | Әрқайсысының өз жарығы |",
                "| BEACH | Теңіз жағасы, күн бату | 7 | Жандос — сол жақта, Қарақат — оң жақта; теңіз алдарында |",
                "| BRIDE_ROOM, GROOM_ROOM, TABLE, HALL_W | Той күні | 8 | Ақ пен алтын |"]
    ids = "\n\n".join(CHAR[k]["id"] for k in ("ZH", "QA", "AR"))
    shorts = "\n".join(CHAR[k]["short"] for k in ("ZH", "QA", "AR"))
    return f"""## 3. Кейіпкерлер мен үздіксіздік кітабы

### Референс суреттер

{chr(10).join(rows)}

**Маңызды:** үш парақты толық жүктеуге болады — промпттарда олардың бір адамның бірнеше көрінісі бар «кейіпкер парағы» екені айтылған. Генератор кадрға тор немесе бір адамның бірнеше көшірмесін шығарса, әр парақтан бет пен толық бойды бөлек кесіп алыңыз.

### Тұрақты сипаттамалар (әр промптқа сөзбе-сөз енгізілген)

```text
{ids}
```

**Қысқа нұсқасы** — таңба шегі бар генераторларға (9-бөлім, 7-кеңес):

```text
{shorts}
```

### Киім кестесі

{chr(10).join(ward_rows)}

Киімдер барлық сценада **референстегідей, өзгеріссіз**. Жалғыз ерекшелік — той (8-сцена): сценарийде Қарақат той көйлегін, Жандос костюмін киеді. Екі қыз киімі арқылы оңай ажыратылады: Қарақат — қою көк худи, Арай — ақшыл худи.

### Мінез, дауыс, қимыл

- **Жандос** — жылы, сәл толқыған, бірақ табанды. Ойланғанда ернін жымқырады, қуанғанда баладай кең күледі. Дауысы жұмсақ баритон.
- **Қарақат** — сабырлы, ұялшақ, күлкісін жасыруға тырысады. Шешім қабылдар алдында терең дем алады. Дауысы жайлы, ақырын.
- **Арай** — ойнақы, сенімді, сәл айлакер. Бір қасын көтеріп қарайды. Дауысы шапшаң, көңілді.

### Өзгермейтін ережелер

1. Қарақаттың шашы бүкіл фильмде **жоғары түйілген**; күміс сырғалары — әр кадрда.
2. Арай мен Қарақат бір кадрда ешқашан бірдей киінбейді.
3. 21-клиптен (алғашқы кездесу) бастап фильмнің соңына дейін, екеуі бірге болғанда **Жандос — экранның сол жағында, Қарақат — оң жағында**. Басында (1–4) олар экранның қарама-қарсы шеттерінде — бұл әдейі: әлі таныс емес.
4. Сақина 37-клиптен бастап Қарақаттың саусағында.
5. Телефон экрандары ешқашан оқылмайды; барлық мәтін монтажда қосылады.

### Локациялар

{chr(10).join(loc_rows)}
"""


SCREENPLAY = """## 4. Толық сценарий

# БІР НӨМІРДЕН БАСТАЛҒАН МАХАББАТ

**Жанры / көңіл күйі:** романтикалық драма, жеңіл юмормен
**Ұзақтығы:** ≈ 4:00 (монтаждан кейін)
**Пропорция:** 16:9
**Визуалды шешім:** табиғи, шынайы романтикалық кино; себепсіз қозғалмайтын камера; ұстамды актерлік ойын; түс бірінші бөлімнің салқын кешкі реңкінен күн батудың алтын түсіне және тойдың ақ-алтын реңкіне қарай жылиды.
**Логлайн:** Волейбол залында бір қызды көріп қалған жігіт оның нөмірін алу үшін бәрін істейді — тіпті құрбысына «ақы төлейді», — ал сол бір нөмір екеуін теңіз жағасындағы ұсынысқа, одан тойға дейін жеткізеді.

### Оқиғаның қысқаша мазмұны

Жандос волейбол залында Қарақатты көріп қалады. Достарында оның нөмірі жоқ, ал Қарақат таксиге отырып кетіп қалады. Келесі күні Жандос Қарақаттың құрбысы Арайдан нөмір сұрайды, бірақ Арай рұқсатсыз бермейді, ал Қарақат бас тартады. Үшінші күні Жандос Арайға ақша ұсынады; Арай «үстінен қос» деп, ақыры нөмірді береді. Жандос жазады — Қарақат бірнеше күн жауап бермейді. Арайдың кеңесінен кейін Қарақат жауап жазады. Алғашқы кездесу — кино, кафе, кітап дүкені, есік алдындағы ұялған құшақ. Содан кейін бірге өткен бақытты күндер. Теңіз жағасында, күн батарда Жандос ұсыныс жасайды, Қарақат келіседі. Фильм тойға дайындықпен және екеуінің қол ұстасып бірге жүруімен аяқталады.

---

### 1-СЦЕНА. АЛҒАШҚЫ КӨЗҚАРАС
**ИНТ. ВОЛЕЙБОЛ ЗАЛЫ — КЕШ / НАТ. СПОРТ КЕШЕНІНІҢ АЛДЫ — ТҮН** · ~31 с · 1–4-клиптер

Қара экран. Доптың еденге екі рет соғылған жаңғырықты дыбысы.

Волейбол залы. Ойын жаңа ғана аяқталды. Доп еденде секіріп, кадрдан домалап шығады. Қыздар сөмкелерін иықтарына іліп, есікке қарай беттейді. Олардың арасында — ҚАРАҚАТ: шашы жоғары түйілген, құлағында жұқа күміс сырғалар. Құрбыларымен күліп келеді.

Залдың арғы шетінде, трибуна жанында ЖАНДОС достарымен әзілдесіп тұр. Кенет көзі Қарақатқа түседі. Күлкісі баяу сөнеді.

Камера Жандостың жүзіне баяу жақындайды. Залдың шуы бәсеңдеп, алыстағандай болады. Фортепианоның жалғыз ақырын нотасы.

> **ЖАНДОС** *(ақырын, көзін алмай)*
> Анау қыз кім өзі?

> **1-ДОСЫ**
> Қайсы? Қарақат па? Ол біздің танысымыз ғой.

> **ЖАНДОС** *(жалт бұрылып)*
> Қарақат дейсің бе? Нөмірі бар ма?

> **2-ДОСЫ** *(иығын көтеріп)*
> Жоқ, нөмірі бізде жоқ.

Жандос есікке қарай ұмтылады.

Көше. Шыны есік ашылып, Жандос баспалдақтан жүгіріп түседі. Бірақ кеш: Қарақат құрбыларымен таксиге отырып, есік жабылады. Такси орнынан қозғалып, көшемен алыстап кетеді.

Жандос жиекте тоқтап, таксидің қызыл шамдарының артынан қарап қалады. Ауыр дем алып, өзіне-өзі күлімсірейді.

*Дыбыс:* көшенің кешкі шуы; фортепиано әуені аяқталмай үзіледі.
*Өту:* түннен күндізге — кафе есігінің қоңырауы.

---

### 2-СЦЕНА. АРАЙМЕН ТАНЫСУ
**НАТ. КАФЕ АЛДЫ — КЕЛЕСІ КҮН, КҮНДІЗ / НАТ. САЯБАҚ АЛЛЕЯСЫ — СОЛ КҮНІ** · ~32 с · 5–8-клиптер

Кафенің шыны есігінен Қарақат құрбысымен күліп шығып, тротуармен кетеді. Есік жабылады. Бір сәттен соң есік қайта ашылып, АРАЙ жалғыз шығады — иығында кенеп сөмке, бұйра шашы жоғары байланған.

Жандос оны байқап, жанына келеді.

> **ЖАНДОС** *(сәл толқып)*
> Сәлем! Сен Арайсың ғой?

> **АРАЙ**
> Иә, не болды?

> **ЖАНДОС**
> Бір нәрсе сұрайын деп едім. Қарақат деген қызды танисың ба?

> **АРАЙ** *(қасын көтеріп)*
> Иә, танимын. Неге?

> **ЖАНДОС**
> Сол қызбен танысқым келіп жүр. Нөмірін бере аласың ба?

> **АРАЙ** *(сыпайы, бірақ нық)*
> Жоқ, рұқсатынсыз бере алмаймын. Алдымен өзінен сұрайын.

Арай басын изеп, кетіп қалады. Жандос орнында қалады.

Саябақ аллеясы. Қарақат орындық жанында телефонына қарап тұр. Арай келіп, жанына тоқтайды.

> **АРАЙ** *(ойнақы, сыбырлағандай)*
> Қарақат, саған бір жігіт қызығып жүр. Аты Жандос. Нөміріңді сұрап жатыр.

Қарақат таңғалып қасын көтереді, сосын ұялып басын шайқайды.

> **ҚАРАҚАТ**
> Жоқ, бермей-ақ қойшы. Танымаймын ғой.

Ол төмен қарап, сөмкесінің бауын түзейді — бірақ ернінің ұшында жасырын күлкі бар.

*Дыбыс:* көше шуы, құстардың үні; ойнақы пиццикато әуені.
*Өту:* үшінші күнге — спорт кешенінің есігі ашылады.

---

### 3-СЦЕНА. НӨМІР ҮШІН КЕЛІССӨЗ
**НАТ. ВОЛЕЙБОЛ ЗАЛЫНЫҢ АЛДЫ — ҮШІНШІ КҮН, КЕШКІ АЛТЫН ШАҚ** · ~29 с · 9–12-клиптер

Жандос достарымен залдан шығып келе жатыр. Арайды көріп, жанына жүгіріп барады.

> **ЖАНДОС**
> Арай, Қарақат не деді? Нөмірін бермеді ме?

> **АРАЙ** *(басын шайқап)*
> Жоқ, келіспеді.

Жандостың иығы түсіп кетеді. Ол ернін жымқырып ойланады... да, қалтасынан бірнеше бүктелген банкнот шығарады.

> **ЖАНДОС** *(айлакер үмітпен)*
> Мынаған келісе алмаймыз ба?

Арай ақшаға, сосын Жандосқа қарайды. Көзін қысып, ойланған кейіп танытады.

> **АРАЙ** *(асықпай)*
> Ойланып көрейін...
> *(кідіріс; мүлдем салқын)*
> Үстінен қос!

Ол алақанын жаяды. Жандос күрсініп, күліп, тағы ақша қосады. Арай ақшаны қалтасына салып, телефонын шығарады да, экранын Жандосқа бұрады.

> **АРАЙ** *(ақырын, құпия)*
> Мә, бірақ мен бергенімді айтпа!

Жандос нөмірді тез өз телефонына теріп алады. Арай кетеді. Жандос «сақтау» батырмасын басып, басын көтереді — жүзінде баладай кең күлкі.

*Дыбыс:* қозғалмайтын камера, комедиялық кідірістер; ойнақы әуен жарқын бір нотамен аяқталады.
*Өту:* телефон — бір кадрдан екіншісіне, кешкі бөлмеге.

---

### 4-СЦЕНА. ЖАУАПСЫЗ ХАБАРЛАМАЛАР
**ИНТ. ЖАНДОСТЫҢ БӨЛМЕСІ — КЕШ / ИНТ. ҚАРАҚАТТЫҢ БӨЛМЕСІ — КЕШ / НАТ. САЯБАҚ — КҮНДІЗ** · ~28 с · 13–18-клиптер

Жандос төсектің шетінде отырып, телефонға жазады, өшіреді, қайта жазады. Жібереді.

*Экранда (монтажда қосылады):* «Сәлем, Қарақат!» — «Қалайсың?» — «Таныссақ бола ма?»

Қарақаттың бөлмесі. Телефон жарқ етеді. Ол оқиды, ернінің ұшымен жымияды — да, телефонды төңкеріп қояды. Жауап жоқ.

Бірнеше күн өтеді. Күндізгі бөлме. Жандос телефонын тағы алады. Жауап жоқ. Тағы бір хабарлама жібереді.

*Экранда:* «Неге жауап бермейсің?»

Ол телефонды үстелге қойып, орындыққа шалқаяды.

Саябақ аллеясы. Арай мен Қарақат қатар келе жатыр.

> **АРАЙ** *(жылы)*
> Қарақат, бір сөйлесіп көрсеңші. Жігіт жаман емес сияқты. Мүмкіндік беріп көр.

Қарақат қадамын баяулатып, ойланып қалады.

Кеш. Қарақат төсекте малдас құрып отыр. Терең дем алып, жауап жазады да, жібереді. Тізесін құшақтап, ұялып жымияды.

Жандостың бөлмесі. Шалқасынан жатқан Жандостың кеудесіндегі телефон дірілдейді. Ол оқиды — атып тұрып, қуанышын жасыра алмай, бірден жауап жаза бастайды.

*Дыбыс:* бөлменің тыныштығы, жалғыз фортепиано ноталары; хабарламаның келген дыбысы — бұрылыс сәт; музыка қайта оралады.
*Өту:* гитара тақырыбының бірінші соққысы — айна алдындағы Қарақат.

---

### 5-СЦЕНА. АЛҒАШҚЫ КЕЗДЕСУ
**ИНТ. ҚАРАҚАТТЫҢ БӨЛМЕСІ — КҮНДІЗ / НАТ. КИНОТЕАТР АЛДЫ — КЕШ / ИНТ. КИНОЗАЛ / ИНТ. КАФЕ / ИНТ. КІТАП ДҮКЕНІ / НАТ. ҚАРАҚАТТЫҢ ҮЙІНІҢ АЛДЫ — ТҮН** · ~29 с · 19–26-клиптер

Жандос Қарақатты кездесуге шақырды — ол келісті.

Қарақат айна алдында. Төсекте таңдалмай қалған киімдер жатыр. Ол кофтасын түзеп, шашын қайта бекітеді, сырғасын реттейді. Терең дем алып, айнадағы өзіне жымияды.

Жандос кинотеатр алдында күтіп тұр. Жағасын түзейді. Басын көтереді — ол келе жатыр.

Екеуі кездеседі. Ұялып, бір-біріне күлімсірейді, төмен қарайды, қайта қарайды. Бірге кинотеатрға беттейді.

Кинозалда қатар отыр. Қарақат оған ұрлана қарайды. Жандос байқап қалады. Екеуі экранға қайта бұрылып, жымияды.

Кафеде Жандос бір нәрсені қызу айтып отыр. Қарақат аузын жауып күледі.

Кітап дүкенінде Қарақат сөреден кітап алып, мұқабасын көрсетеді. Иықтары бір-біріне тиіп тұр.

Түн. Қарақаттың үйінің кіреберісі. Олар есік алдына келіп тоқтайды. Үнсіз бір сәт. Қарақат кенет Жандосты құшақтап алады да, үйіне жүгіріп кіріп кетеді.

Жандос шам астында жалғыз қалады. Таңданысы баяу кең күлкіге айналады.

*Дыбыс:* жылы акустикалық гитара — фильмнің махаббат тақырыбы. Сөз жоқ — бәрі көзқараста.
*Өту:* сол бір күлкі — түнгі қоңыраудағы күлкіге.

---

### 6-СЦЕНА. БІРГЕ ӨТКЕН БАҚЫТТЫ КҮНДЕР (монтаж)
**ӘРТҮРЛІ ОРЫНДАР** · ~16 с · 27–32-клиптер

Романтикалық ән. Жылдам, әдемі монтаж:

- Түн ортасы. Экран екіге бөлінген: Жандос пен Қарақат әрқайсысы өз төсегінде, телефонмен сөйлесіп, ақырын күледі. Қарақат жастықты құшақтап жатыр — сағынып.
- Алтын далада атқа мініп, қатар серуендейді.
- Үйде көрпе астында «Гарри Поттер» фильмін көреді — экран кадрда көрінбейді, тек оның жарығы жүздерінде ойнайды. Қарақат басын Жандостың иығына сүйейді.
- Тағы бір кафе — кесе соғыстырып, күледі.
- Түнгі қала көшесі — қол ұстасып, бір-біріне қарап, күліп келе жатыр.

*Дыбыс:* романтикалық ән; әр кадр ырғаққа түседі.
*Өту:* түнгі көше шамдары біртіндеп күн батудың алтын жарығына ұласады.

---

### 7-СЦЕНА. ТЕҢІЗ ЖАҒАСЫНДАҒЫ ҰСЫНЫС
**НАТ. ТЕҢІЗ ЖАҒАСЫ — КҮН БАТУ** · ~45 с · 33–38-клиптер

Кеш. Теңіз жағасында әдемі безендірілген пикник: аласа үстелде гүлдер, тәттілер, шыны ыдыстағы шамдар. Жандос пен Қарақат қатар отырып, теңізге қарап әңгімелеседі. Қарақат күліп, иығын оған сүйейді.

Жандос Қарақаттың қолын ұстап, көзіне қарайды.

> **ЖАНДОС** *(баяу, шын жүректен)*
> Білесің бе, сені алғаш көрген күнім әлі есімде. Сол кезде сенің бір күнің менің бүкіл өмірімді өзгертетінін білмеппін.

Қарақат тыңдап отыр. Жандостың даусы жалғасады:

> **ЖАНДОС** *(кадр сыртынан)*
> Басында сенімен танысу үшін қанша тырысқанымды өзің де білесің. Бүгін сенімен бірге болашаққа қадам басқым келеді...

«Қанша тырысқанымды» дегенде Қарақат ақырын күліп жібереді — есіне түсті. Сосын жүзі байыпты тартып, көзі жасаурайды.

Жандос сақина қорабын шығарып, ашады.

> **ЖАНДОС** *(ақырын, толқып)*
> Қарақат, менің өмірлік серігім болуға келісесің бе?

Қарақат аузын қолымен жабады. Көзіне жас келеді. Ол күлімсіреп, басын изейді. Жандос сақинаны саусағына тағады. Екеуі құшақтасады.

Камера баяу алыстап, жоғары көтеріледі: жарқыраған шамдар, бос жағалау, теңіз және көкжиекке тиген күн.

*Дыбыс:* толқын; сөз кезінде ішекті аспаптар басылады; «иә» деген изеуде әуен толқып көтеріледі; жылы аккордпен аяқталады.
*Өту:* күн батудың алтын жарығы біртіндеп той күнінің ақ жарығына ұласады.

---

### 8-СЦЕНА. ТОЙҒА ДАЙЫНДЫҚ
**ИНТ. ҚАЛЫҢДЫҚТЫҢ БӨЛМЕСІ / КҮЙЕУ ЖІГІТТІҢ БӨЛМЕСІ / ТОЙ ЗАЛЫ — ТОЙ КҮНІ** · ~22 с · 39–45-клиптер

Көтеріңкі, салтанатты әуен. Кадрлар бірінен соң бірі ауысады:

- Қарақат той көйлегін киіп, айнаға қарайды.
- Жандос костюмінің түймесін салып, галстугін түзейді.
- Екі алтын сақина — жақын кадр.
- Қалыңдықтың ақ раушан гүл шоғы.
- Той залы безендірілуде.
- Екі жақтың туыстарының қуанышты жүздері.

Биік есіктер ашылады. Жандос пен Қарақат қол ұстасып, камераға қарай бірге жүреді. Кадрды жылы жарық толтырады.

*Дыбыс:* той әуені шарықтау шегінде, қол шапалақ. *(Ұсыныс: домбыра сарыны қосылса — қазақы нақыш береді.)*

---

### ФИНАЛ
**Қара экран** · ~7 с · монтажда жасалады

Ақ әріптер баяу пайда болады:

> **ЖАНДОС ❤️ ҚАРАҚАТ**
> Бір кездейсоқ көзқарастан басталған махаббат...
> Бүгін мәңгілікке жалғасты.
> Енді олар бір-бірінің өмірлік серігі!
> **Бақытты болыңыздар!**

*Дыбыс:* той әуенінің соңғы аккорды үнсіздікке ұласады.
"""

HEAD = """# «БІР НӨМІРДЕН БАСТАЛҒАН МАХАББАТ» — фильм пакеті

Жандос ❤️ Қарақат · 16:9 · ≈ 4 минут · 45 клип + финалдық жазу

> **Референстер:** **1-сурет — Жандос, 2-сурет (түйілген шаш, күміс сырға, қою көк худи) — Қарақат, 3-сурет (бұйра каштан шаш, ақшыл худи) — Арай.** Киімдер мен беттер барлық клипте референстегідей; тек тойда — ақ көйлек пен костюм.

**Мазмұны:** 1. Шығармашылық бағыт · 2. Оқиға құлпы · 3. Кейіпкерлер кітабы · 4. Толық сценарий · 5. Кадрлар тізімі · 6. Клип промпттары · 7. Үздіксіздік және өту картасы · 8. Сапа тексерісі · 9. Генерацияға кеңестер

---

## 1. Шығармашылық бағыт

- **Жанры мен көңіл күйі.** Табиғи романтикалық драма, бірінші жартысында жеңіл юмор бар (нөмір үшін «сауда»). Актерлік ойын ұстамды: сезім үлкен қимылмен емес, көзқараспен, кідіріспен, жасырын күлкімен беріледі.
- **Үш акт.**
  - **I акт (1–4-сцена): «Нөмір».** Салқын, бейтарап жарық — кешкі спорт залы, күндізгі қала. Ойнақы пиццикато. Комедиялық сәттер қозғалмайтын кадрмен түсіріледі.
  - **II акт (5–6-сцена): «Жақындасу».** Жылы, алтын реңк. Акустикалық гитара — фильмнің махаббат тақырыбы. Ырғақты монтаж.
  - **III акт (7–8-сцена): «Мәңгілік».** Күн батудың алтын-қызғылт түсі және ішекті аспаптар; той — ақ пен алтын, салтанатты әуен.
- **Камера.** Себепсіз қозғалмайды. Комедия — тұрақты кадр. Сезім — баяу жақындау (push-in). Финалдар — баяу шегіну.
- **Фильмнің «қолтаңбасы».** *Телефон* — басты зат: нөмір → хабарлама → жауап → түнгі қоңырау. Әрі *экрандағы орын*: басында Жандос пен Қарақат экранның қарама-қарсы жақтарында; алғашқы кездесуден бастап олар үнемі қатар — Жандос солда, Қарақат оңда — тойға дейін.
- **Дыбыс.** Әр актінің өз әуені; маңызды сәттерде музыка тынады (комедиялық кідіріс, ұсыныс алдындағы тыныштық).
- **Формат.** 16:9; диалог клиптері — 10 с, монтаж және детальдар — 5 с. Финалдық жазулар мен телефон хабарламалары монтажда қосылады.

---

## 2. Оқиға құлпы (Story Lock)

**Сіздің мәтініңізден алынған нақты фактілер — өзгертілмеген:**
- Кейіпкерлер: Жандос пен Қарақат (басты), Арай (Қарақаттың құрбысы), Жандостың достары, Қарақаттың құрбылары.
- Хронология: волейбол залы, кеш (алғашқы көзқарас, таксиге кетіп қалуы) → келесі күн, кафе алды (Арайдан нөмір сұрау; Арай рұқсатсыз бермейді; Қарақат бас тартады) → үшінші күн, зал алды (ақша, «Үстінен қос!», нөмір, «айтпа») → хабарламалар, бірнеше күн жауап жоқ, Арайдың кеңесі, Қарақаттың жауабы → алғашқы кездесу (дайындық, кино, кафе, кітап дүкені, үйге шығарып салу, құшақ) → бірге өткен күндер (түнгі қоңыраулар, сағыну, атқа міну, «Гарри Поттер», кафелер, серуен, қол ұстасу) → теңіз жағасындағы ұсыныс (пикник: гүл, тәтті, шамдар; сақина; «иә»; құшақ) → тойға дайындық (көйлек, костюм, сақиналар, гүл шоғы, зал, екі жақтың жүздері) → қол ұстасып камераға қарай жүру → финалдық жазу.
- Барлық диалог — сіз жазғандай, сөзбе-сөз.
- Формат 16:9, ұзақтығы 3–4 минут, романтикалық кино стилі.

**Кинематографиялық шешімдер (менің ұсынысым, фактіні өзгертпейді):**
- Киімдер бүкіл фильмде референстегідей; тек тойда — сценарий бойынша ақ көйлек пен костюм (олардың сипаттамасы — менің ұсынысым).
- Арай мен Қарақаттың сөйлесетін орны (2 және 4-сцена) — саябақ аллеясы; мәтінде орын көрсетілмеген.
- 3-сцена кешкі алтын шақта өтеді — күндерді жарықпен ажырату үшін.
- Төртінші хабарлама («Неге жауап бермейсің?») бірнеше күннен кейін жіберілгендей көрсетілді — мағынасы солай.
- Жандостың кездесуге шақыруы оның қуанып жауап жазуы арқылы көрсетілді; хабарлама мәтіні ойдан қосылған жоқ.
- «Гарри Поттер» фильмінің өзі кадрда көрсетілмейді (авторлық құқық) — тек экран жарығы.
- Сақина — қарапайым алтын сақина, тасы кішкентай (мәтінде сипаттамасы жоқ).
- Қала, жыл мезгілі, теңіздің аты көрсетілмеген — бейтарап жылы ауа райы алынды.

**Нақтылауды қажет ететін нәрселер:**
1. Суреттердің реті (беттің жоғарғы жағында).
2. 7-сценадағы сөйлем: «Сол кезде **сенің бір күнің** менің бүкіл өмірімді өзгертетінін білмеппін». Мүмкін «сол бір күннің» деген ой шығар? Түпнұсқаны өзгертпедім — қаласаңыз, түзетемін.

---
"""

TIPS = """## 9. Генерацияға кеңестер

1. **Референстер.** Үш парақты толық жүктеуге болады, промпттардағы «reference image 1/2/3»: 1 — Жандос, 2 — Қарақат, 3 — Арай. Генератор кадрға тор немесе бір адамның бірнеше көшірмесін шығарса, бет пен толық бойды бөлек кесіп алыңыз.
2. **Ең сенімді жол — алдымен сурет, сосын видео.** Әр клиптің бірінші кадрын референстермен сурет етіп жасап, сосын сол суреттен видео шығарыңыз (image-to-video). Тек мәтін беттің ұқсастығына кепілдік бермейді — референс пен бастапқы кадр әлдеқайда күшті.
3. **Тығыз жалғасатын жұптар:** 10→11 және 36→37. Алдыңғы клиптің соңғы кадрын келесісінің бірінші кадры ретінде беріңіз.
4. **Қазақша диалог.** Көп генераторлар қазақ тілінде қате айтады немесе ерін қимылы сәйкес келмейді. Диалогты генерацияда ойнатып, дыбысын кейін ауыстырыңыз. Ең жақсысы — Жандос пен Қарақаттың өз дауыстары. Екінші жол — ElevenLabs арқылы қазақша дыбыстау (қаласаңыз, дайындап беремін). 35-клипте Жандос арқасымен тұр, сондықтан оның сөзін ерін қимылынсыз-ақ дыбыстауға болады.
5. **Мәтін — тек монтажда:** телефон хабарламалары (13, 15) мен финалдық жазулар.
6. **Платформалар.** Барлық промпт кез келген генераторға жарайды. Референс суреттерді Veo/Flow-да «Ingredients», Kling-те «Elements», Runway-де «References» арқылы беріңіз. Seedance шынайы адам бетіне ұқсайтын референстерді қабылдамауы мүмкін. Генератор 10 секунд бермесе (мысалы, 8 с), әрекетті сол уақытқа сыйғызыңыз — монтажда ұзақтық соған қарай есептелген.
7. **Таңба шегі.** Промпттар толық жазылған (1 500–5 500 таңба). Veo/Flow, Sora, Seedance оны толық қабылдайды. Kling (~2 500 таңба) немесе Runway (~1 000 таңба) сияқты шегі бар генераторда: кейіпкер сипаттамасын 3-бөлімдегі **қысқа нұсқамен** ауыстырыңыз, VISUAL QUALITY мен AVOID бөлімдерін алып тастаңыз немесе қысқартыңыз, ал ACTION, CAMERA және AUDIO бөлімдерін міндетті түрде қалдырыңыз. Бетті референс суреттер ұстап тұрады.
8. **Нұсқаларға дайын болыңыз.** Диалогы бар және бет жақын түсірілген клиптерге 2–3 нұсқа жасауға тура келуі мүмкін. Ешбір промпт мінсіз нәтижеге кепілдік бермейді.
9. **44-клип (туыстар).** Нағыз той болса, бұл кадрды шынайы туыстардың бейнежазбасымен ауыстырған жөн.
"""

QC = """## 8. Сапа тексерісі

- ✅ Мәтіндегі барлық оқиға сценарийде бар, реті сақталған (1–8-сцена + финал).
- ✅ Жаңа маңызды оқиға, кездесу немесе қақтығыс қосылған жоқ; ұсынылған детальдар «Оқиға құлпында» белгіленді.
- ✅ Әр кейіпкерге бір ғана сипаттама бар, ол әр промптқа сөзбе-сөз кірген; Қарақат пен Арай киімі мен шашы арқылы анық ажыратылады.
- ✅ Киім тек жаңа күнге немесе жаңа оқиғаға (кездесу, ұсыныс, той) байланысты өзгереді.
- ✅ Әр клипте бір орын, бір үздіксіз әрекет, басы мен соңы бар; ұзақтығы әрекетке сай.
- ✅ Әр промпт өз бетінше түсінікті: кейіпкер, киім, орын, жарық қайталанған.
- ✅ Камераның әр қозғалысының себебі бар; мүмкін емес қозғалыс жоқ.
- ✅ Диалог дұрыс кейіпкерге берілген және қазақ тілінде сөзбе-сөз сақталған.
- ✅ Дыбыс кадрдағы әрекетке сай (жіберу/келу дыбыстары, есік, толқын).
- ✅ Әр клиптің соңғы кадры келесісінің бірінші кадрымен байланысты (7-бөлім).
- ✅ Пропорция барлық клипте 16:9.
- ✅ Платформаға тән параметр жалпы ереже ретінде берілмеген.
- ✅ Промпттарда толтырылмаған жақша қалған жоқ.
- ✅ Бет ұқсастығына немесе мінсіз нәтижеге кепілдік берілмеген.
"""


def build():
    tl, total = timeline()
    total += FINAL_CARD
    gen_total = sum(c["gen"] for c in CLIPS)
    out = [HEAD, bible(), "---", SCREENPLAY, "---"]

    # 5. shot list
    out.append("## 5. Кадрлар тізімі\n")
    out.append(f"Барлығы: **{len(CLIPS)} клип**, генерация — {gen_total} с, монтаждан кейін — **{tc(total)}** (финалдық жазуды қоса). «Монтаж» бағаны — клиптің фильмде қанша секунд көрінетіні; қалған бөлігі монтаждағы қор.\n")
    out.append("| № | Тайм-код | Сц. | Кадр | Түсірілім | Ген. | Монтаж |")
    out.append("|---|---|---|---|---|---|---|")
    for c in CLIPS:
        a, b = tl[c["n"]]
        edit = "бөлінген экран (27-мен)" if c["edit"] == 0 else f"{c['edit']} с"
        out.append(f"| {c['n']:02d} | {tc(a)}–{tc(b)} | {c['scene']} | {c['kk']} | {c['shot']} | {c['gen']} с | {edit} |")
    end_start = total - FINAL_CARD
    out.append(f"| — | {tc(end_start)}–{tc(total)} | Финал | Қара экран, ақ жазулар | Монтажда жасалады | — | {FINAL_CARD} с |")
    out.append("\n---\n")

    # 6. prompts
    out.append("## 6. Клип промпттары\n")
    out.append("Әр промпт — бөлек код блогында, жеке көшіруге болады. Промпттар ағылшынша (генераторлар оны жақсы түсінеді), диалог — қазақша, сөзбе-сөз. Әр промптқа тиісті кейіпкерлердің референс суреттерін қоса тіркеңіз.\n")
    current = None
    for c in CLIPS:
        if c["scene"] != current:
            current = c["scene"]
            out.append(f"### {current}-сцена · {SCENE_NAMES[current]}\n")
        a, b = tl[c["n"]]
        refs = ", ".join(f"{CHAR[k]['ref']}-сурет ({CHAR[k]['kk']})" for k, _ in c["cast"]) or "референс қажет емес"
        place = "бөлінген экран, 27-клиппен қатар" if c["edit"] == 0 else f"монтажда ~{c['edit']} с, {tc(a)}–{tc(b)}"
        out.append(f"**CLIP {c['n']:02d} — {c['en']} | {c['gen']} s | {ASPECT}**  ")
        out.append(f"*{c['kk']}* · {place} · Референс: {refs}\n")
        out.append("```text\n" + prompt(c) + "\n```")
        if c.get("note"):
            out.append(f"> {c['note']}")
        out.append("")
    out.append("---\n")

    # 7. continuity + transition map
    out.append("## 7. Үздіксіздік және өту картасы\n")
    out.append("Әр көршілес клип жұбы үшін: A клиптің соңғы кадры, өту әдісі және себебі, механизмі, B клиптің алғашқы кадры, сәйкес болуы тиіс нәрселер, дыбыс және өтудің қайда жасалатыны.\n")
    for i, c in enumerate(CLIPS):
        nxt = CLIPS[i + 1] if i + 1 < len(CLIPS) else None
        t = c["tr"]
        target = f"{nxt['n']:02d}" if nxt else "ФИНАЛ"
        out.append(f"**{c['n']:02d} → {target} · {t['tech']}**")
        out.append(f"- A соңғы кадры: {c['last']}")
        out.append(f"- Неге: {t['why']}")
        out.append(f"- Механизм: {t['mech']}")
        out.append(f"- B алғашқы кадры: {nxt['first'] if nxt else 'Қара экран, ақ жазулар баяу пайда болады.'}")
        out.append(f"- Сәйкестік: {t['match']}")
        out.append(f"- Дыбыс: {t['sound']}")
        out.append(f"- Қайда жасалады: {t['where']}")
        out.append("")
    out.append("---\n")
    out.append(QC)
    out.append("---\n")
    out.append(TIPS)

    text = "\n".join(out)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "FILM.md"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"FILM.md: {len(CLIPS)} clips, generate {gen_total}s, final cut {tc(total)}, {len(text)} chars")


if __name__ == "__main__":
    build()
