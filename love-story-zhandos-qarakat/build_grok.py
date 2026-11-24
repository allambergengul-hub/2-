#!/usr/bin/env python3
"""Builds GROK-15s.md: the Zhandos & Qarakat film as 16 Grok clips of 15 seconds.

@imageN numbers follow the upload order of each clip (Zhandos, then Qarakat, then Arai —
only the ones in the clip). Identity and wardrobe strings are defined once below.
Run:  python3 build_grok.py
"""
import os

ID = {
    "ZH": '''ZHANDOS — the young man from @image{n}. Keep his exact face, facial structure, hair and body proportions from @image{n}; never a look-alike. Twenties, tall and lean, thick slightly messy jet-black hair, calm dark-brown eyes, a few small moles on his cheeks, clean-shaven.''',
    "QA": '''QARAKAT — the young woman from @image{n}. Keep her exact face, facial structure and body proportions from @image{n}; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always in a high round bun; large thin silver hoop earrings in every shot; calm almond-shaped dark eyes.''',
    "AR": '''ARAI — the young woman from @image{n}. Keep her exact face and body proportions from @image{n}; never a look-alike. Twenties, freckles across her nose and cheeks, long curly chestnut-brown hair in a high curly ponytail.''',
}
KK = {"ZH": "Жандос", "QA": "Қарақат", "AR": "Арай"}
ORDER = ["ZH", "QA", "AR"]

WARD = {
    "ZH_SPORT": "black pullover hoodie with three white stripes down each sleeve and a small white chest emblem, black track pants with three white side stripes, white sneakers with three black stripes (as in his reference image)",
    "ZH_DATE": "black bomber jacket, plain white T-shirt, dark-indigo jeans, white sneakers",
    "ZH_SEA": "white linen shirt with rolled sleeves, beige chinos",
    "ZH_SUIT": "black two-piece suit, white shirt, slim black tie, black leather shoes",
    "QA_SPORT": "oversized dark-navy hoodie, light heather-grey jogger sweatpants, white sneakers, a silver dog-tag pendant on a long chain (as in her reference image)",
    "QA_DATE": "cream chunky knit sweater, high-waisted dark-navy pleated midi skirt, white sneakers, the silver dog-tag pendant",
    "QA_SEA": "flowing cream linen midi dress, tan sandals",
    "QA_BRIDE": "white wedding gown with a lace bodice and a full skirt, a sheer veil pinned under her high bun",
    "AR_DAY": "camel-beige oversized knit cardigan, white T-shirt, light-blue jeans, white canvas sneakers, a beige canvas tote bag",
}

FRIENDS = "Zhandos's two friends (supporting, never in close-up): one with buzz-cut hair in a grey hoodie, one in a black cap and dark-green track jacket."
TEAM = "Qarakat's teammates (supporting, soft focus): young women in black leggings and white or grey T-shirts — none with a navy hoodie, a high bun or hoop earrings."

STYLE = "Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition."
AVOID = "face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, extra logos"

CLIPS = []


def G(**k):
    CLIPS.append(k)


G(n=1, scene=1, kk="Алғашқы көзқарас", en="The First Look",
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT")], extra=[TEAM, FRIENDS],
  sum="Ойын бітті, Қарақат құрбыларымен шығып барады; Жандос оны көріп қалады: «Анау қыз кім өзі?»",
  loc="An indoor volleyball gym in the evening: polished honey-coloured wooden floor with white court lines, a net, wooden bleachers along the right wall, exit doors on the left, dark windows high up.",
  tl=[("0–5 s", "Low angle at floor level: a volleyball bounces twice on the wooden floor and rolls out of frame. The women's game has just ended; QARAKAT slings her sports bag over her shoulder and walks screen-left toward the exit with two teammates, laughing. The camera tracks slowly left with them."),
      ("5–10 s", "CUT TO a medium shot of ZHANDOS by the bleachers at screen-right, laughing with his two friends. His eyes drift screen-left and stop on Qarakat; his laugh fades and he blinks once. The camera pushes in slowly to a close-up of his face as the gym noise fades."),
      ("10–15 s", 'Close-up, eyes still on her, Zhandos says quietly: "Анау қыз кім өзі?" CUT TO a medium three-shot: FRIEND 1 follows his gaze and answers casually: "Қайсы? Қарақат па? Ол біздің танысымыз ғой." Final frame: Zhandos turning to his friend, interested.')],
  cam="35mm wide tracking shot, then a slow 50→85mm push-in on Zhandos, then a 40mm three-shot with gentle handheld breathing; shallow depth of field.",
  light="Even overhead LED panels, warm bounce from the wooden floor, natural skin tones.",
  sound="Two hollow ball bounces echoing, sneakers squeaking, indistinct happy chatter (no clear words); the gym reverb fades as one soft piano note begins. Dialogue in Kazakh with the exact words above.",
  avoid="extra players crowding the frame, a second woman with a high bun",
  fb="01, 02, 03",
  seam="G02 сол үш адамдық кадрдан, сол позициялардан басталады — монтажда тікелей кесу.")

G(n=2, scene=1, kk="Кешікті", en="Too Late",
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT")], extra=[FRIENDS, TEAM],
  sum="Достарында нөмір жоқ; Жандос сыртқа жүгіреді, бірақ Қарақат таксиге отырып кетіп қалады.",
  loc="Inside: the same evening volleyball gym by the bleachers. Outside: the sports complex at night — wide concrete steps, glass doors glowing at screen-right, a quiet street running left–right, warm street lamps.",
  tl=[("0–5 s", 'Medium three-shot by the bleachers. ZHANDOS turns to his friend, eager: "Қарақат дейсің бе? Нөмірі бар ма?" FRIEND 2 shrugs: "Жоқ, нөмірі бізде жоқ." Zhandos immediately hurries out of frame screen-left toward the exit.'),
      ("5–10 s", "CUT TO outside at night, wide shot from across the street: a white taxi waits at the curb; the teammates get in, QARAKAT (navy hoodie, high bun, silver hoops) gets in last and the door shuts; the taxi pulls away screen-left. The glass doors at screen-right swing open and Zhandos runs down the steps."),
      ("10–15 s", "Zhandos slows and stops at the curb, watching the red tail lights shrink into the distance; he exhales and gives a small rueful smile to himself. Final frame: Zhandos alone at the curb in a three-quarter back view under the street lamps.")],
  cam="Handheld 40mm three-shot, then a locked-off 35mm wide across the street, ending with a slow push-in toward his back.",
  light="Gym LED light inside; outside warm sodium street lamps, cool blue night, red tail lights.",
  sound="Dialogue in Kazakh with the exact words above; the door pushed open; a car door shutting, the engine pulling away, a quiet night street; the piano phrase stops unresolved.",
  avoid="readable licence plates or taxi branding",
  fb="03, 04",
  seam="Түннен күндізге тікелей кесу; кафе есігінің қоңырауы кесуден сәл бұрын естіледі (J-cut).")

G(n=3, scene=2, kk="«Сен Арайсың ғой?»", en="You're Arai, Right?",
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT"), ("AR", "AR_DAY")], extra=[TEAM],
  sum="Келесі күні Қарақат кафеден кетеді, Арай жалғыз шығады; Жандос онымен танысып, Қарақатты сұрайды.",
  loc="A small modern café on a quiet city street in daylight: a glass front and glass door, two small outdoor tables, a tree-lined sidewalk running left–right.",
  tl=[("0–4 s", "QARAKAT and one teammate step out of the café door laughing and walk off screen-right. The door swings shut; a moment later it opens again and ARAI steps out alone, settling her tote bag on her shoulder."),
      ("4–9 s", 'ZHANDOS walks up from screen-left and stops in front of her — medium two-shot in profile, Zhandos screen-left, Arai screen-right. Rubbing the back of his neck: "Сәлем! Сен Арайсың ғой?" Arai: "Иә, не болды?"'),
      ("9–15 s", 'Zhandos: "Бір нәрсе сұрайын деп едім. Қарақат деген қызды танисың ба?" Arai raises one eyebrow and tilts her head: "Иә, танимын. Неге?" Final frame: Arai\'s sceptical half-smile as she waits for his answer.')],
  cam="35mm wide-medium from across the sidewalk, then a 50mm medium two-shot in profile with subtle handheld breathing.",
  light="Soft overcast daylight, neutral natural colours.",
  sound="A small door chime, street ambience, footsteps, a light playful pizzicato tune; dialogue in Kazakh with the exact words above.",
  avoid="readable café name or menu, the two women looking alike",
  fb="05, 06",
  seam="Арайдың «Неге?» деген сөзінен кейінгі кідірісте Жандостың иығы үстінен түсірілген кадрға кесу.")

G(n=4, scene=2, kk="«Рұқсатынсыз бере алмаймын»", en="Not Without Her Permission",
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT"), ("AR", "AR_DAY")], extra=[],
  sum="Арай нөмірді рұқсатсыз бермейді; саябақта Қарақатқа айтады — Қарақат бас тартады.",
  loc="First the café sidewalk in daylight, then a tree-lined park alley with a paved path and wooden benches, the same day.",
  tl=[("0–7 s", 'Over Zhandos\'s shoulder (soft in the left foreground) onto ARAI: Zhandos asks: "Сол қызбен танысқым келіп жүр. Нөмірін бере аласың ба?" Arai shakes her head, polite but firm: "Жоқ, рұқсатынсыз бере алмаймын. Алдымен өзінен сұрайын." She nods and walks away screen-right.'),
      ("7–11 s", 'CUT TO the park alley: QARAKAT stands by a bench at screen-right looking at her phone; Arai walks into frame from screen-left and leans in with a playful smile: "Қарақат, саған бір жігіт қызығып жүр. Аты Жандос. Нөміріңді сұрап жатыр."'),
      ("11–15 s", 'Qarakat lifts her eyebrows in surprise, then shakes her head with a shy half-smile: "Жоқ, бермей-ақ қойшы. Танымаймын ғой." She looks down and adjusts her bag strap, hiding a smile. Final frame: Qarakat looking down, Arai shrugging.')],
  cam="50mm over-the-shoulder, static; then a 50mm medium two-shot at eye level with gentle handheld breathing.",
  light="Overcast daylight at the café, then dappled sunlight through the park trees.",
  sound="Dialogue in Kazakh with the exact words above; footsteps; birdsong and rustling leaves in the park; playful pizzicato.",
  avoid="the two women looking alike",
  fb="07, 08",
  seam="Есік арқылы өту: спорт кешенінің шыны есігі ашылып, Жандос шығады; ойнақы әуен екі клипке ортақ.")

G(n=5, scene=3, kk="«Үстінен қос!»", en="Can We Make a Deal?",
  cast=[("ZH", "ZH_SPORT"), ("AR", "AR_DAY")], extra=[FRIENDS],
  sum="Үшінші күні Жандос Арайға ақша ұсынады; Арай «Ойланып көрейін... Үстінен қос!» дейді.",
  loc="In front of the sports complex in the late afternoon: wide concrete steps, glass doors, a pale facade, young trees, the sidewalk running left–right.",
  tl=[("0–5 s", 'ZHANDOS comes down the steps with his two friends, spots ARAI on the sidewalk and jogs over (Zhandos screen-left, Arai screen-right): "Арай, Қарақат не деді? Нөмірін бермеді ме?" Arai shakes her head: "Жоқ, келіспеді."'),
      ("5–10 s", 'Locked-off medium two-shot. Zhandos\'s shoulders drop; he thinks, lips pressed, then pulls a few folded banknotes from his hoodie pocket and holds them out with a sly, hopeful smile: "Мынаған келісе алмаймыз ба?"'),
      ("10–15 s", 'Arai looks at the money, then at him, narrows her eyes and weighs it theatrically: "Ойланып көрейін..." — a beat of silence — then, deadpan: "Үстінен қос!" She holds out her open palm. Final frame: Arai\'s open palm and raised eyebrows; Zhandos frozen mid-smile.')],
  cam="Handheld 35mm follow on the steps, then a completely locked-off 40mm medium two-shot — the stillness carries the comedy.",
  light="Low warm late-afternoon sun from screen-left, soft golden rim light.",
  sound="Dialogue in Kazakh with the exact words above; footsteps on concrete; playful music that stops for the pause and comes back on \"Үстінен қос!\".",
  avoid="close-up fake banknote designs",
  fb="09, 10",
  seam="Ең тығыз жалғау: G05 соңғы кадрын (Арайдың ашық алақаны) скриншот алып, G06-ға бастапқы сурет етіп беріңіз.")

G(n=6, scene=3, kk="Нөмір сақталды", en="Saved",
  cast=[("ZH", "ZH_SPORT"), ("AR", "AR_DAY")], extra=[],
  sum="Жандос тағы ақша қосады; Арай нөмірді береді: «Мә, бірақ мен бергенімді айтпа!» Жандос қуанады.",
  loc="The same spot in front of the sports complex, late afternoon.",
  tl=[("0–5 s", "Same locked-off two-shot: ZHANDOS sighs with a laugh and places more banknotes into ARAI's open palm. She tucks the money into her cardigan pocket."),
      ("5–10 s", 'Arai takes out her phone and turns the screen toward him (away from the camera), whispering: "Мә, бірақ мен бергенімді айтпа!" Zhandos quickly types the number into his own phone. Arai walks off screen-right with a knowing look.'),
      ("10–15 s", "CUT TO a close-up of Zhandos's hands; his thumb taps save; the camera tilts up to his face as he breaks into a wide, boyish grin and gives a small fist pump. Final frame: his grin in golden light.")],
  cam="40mm two-shot with a very slow push-in, then an 85mm close-up with a smooth tilt up from hands to face.",
  light="Low golden-hour sun from screen-left, warm rim light on his hair.",
  sound="Dialogue in Kazakh with the exact words above; soft screen taps; the playful music lands on one bright final note.",
  avoid="readable phone screens or numbers",
  fb="11, 12",
  seam="Телефон → телефон: күндізгі қолдағы телефоннан түнгі бөлмедегі телефонға кесу.")

G(n=7, scene=4, kk="Жауапсыз хабарламалар", en="No Reply",
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT")], extra=[],
  sum="Жандос алғаш жазады; Қарақат оқиды, бірақ жауап бермейді; бірнеше күннен соң Жандос тағы жазады.",
  loc="Zhandos's small bedroom (bed, wooden desk with a lamp, window with city lights) and Qarakat's bedroom (white bedding, bedside lamp, sheer curtains).",
  tl=[("0–5 s", "Night, Zhandos's bedroom: ZHANDOS sits on the edge of his bed, phone in both hands; he types, hesitates, deletes, types again and sends — one, two, three messages."),
      ("5–10 s", "CUT TO Qarakat's bedroom at night: QARAKAT lies on her stomach on her bed; her phone lights up and buzzes. She reads, a tiny smile flickers, she bites her lip, then places the phone face-down and looks away toward the window."),
      ("10–15 s", "CUT TO Zhandos's room in daylight, days later: he picks up the phone from his desk, checks it — nothing — sends one more short message, puts the phone down and leans back with a sigh, running a hand through his hair.")],
  cam="50mm medium shots at eye level, static, shallow depth of field.",
  light="Night: warm lamps and the cool glow of phones on their faces. Day: soft flat window light — the colour of waiting.",
  sound="Screen taps, message-sent sounds, a phone vibrating on the bedspread, quiet rooms, sparse piano notes. No dialogue.",
  avoid="readable phone screens",
  note="Монтажда хабарлама көпіршіктерін қосыңыз: 0–5 с — «Сәлем, Қарақат!», «Қалайсың?», «Таныссақ бола ма?»; 10–15 с — «Неге жауап бермейсің?»",
  fb="13, 14, 15",
  seam="Жандостың күрсінісінен кейін Арайдың «Қарақат, бір сөйлесіп көрсеңші…» деген даусы алдын ала естіледі (J-cut).")

G(n=8, scene=4, kk="Ол жауап берді", en="She Answers",
  cast=[("ZH", "ZH_SPORT"), ("QA", "QA_SPORT"), ("AR", "AR_DAY")], extra=[],
  sum="Арай: «Мүмкіндік беріп көр». Кешке Қарақат жауап жазады — Жандос қуанып, бірден жауап жазады.",
  loc="A tree-lined park alley in daytime; then Qarakat's bedroom and Zhandos's bedroom at night.",
  tl=[("0–7 s", 'Park alley: ARAI (screen-left) and QARAKAT (screen-right) walk toward the camera; Arai gently bumps Qarakat\'s shoulder: "Қарақат, бір сөйлесіп көрсеңші. Жігіт жаман емес сияқты. Мүмкіндік беріп көр." Qarakat slows down, thinking, a small undecided smile.'),
      ("7–11 s", "CUT TO Qarakat's bedroom at night: she sits cross-legged on her bed, takes a breath, types a short reply and taps send, then hugs her knees with a shy smile."),
      ("11–15 s", "CUT TO Zhandos's bedroom at night: ZHANDOS lies on his back, the phone on his chest buzzes; he reads, sits bolt upright with a huge grin and immediately starts typing back fast.")],
  cam="35mm leading track walking backward in the park; 85mm close-up on Qarakat; 35mm medium on Zhandos rising as he sits up.",
  light="Dappled park sunlight; at night warm lamps and phone glow.",
  sound="Dialogue in Kazakh with the exact words above; birdsong; a message-sent sound, then a vibration and message tone; a warm acoustic guitar begins at the end.",
  avoid="readable phone screens, the two women looking alike",
  fb="16, 17, 18",
  seam="Жандос «жіберу» батырмасын басқанда гитара тақырыбы басталады; бірінші соққыда айна алдындағы Қарақатқа кесу.")

G(n=9, scene=5, kk="Алғашқы кездесу", en="The First Date",
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], extra=[],
  sum="Қарақат айна алдында дайындалады; Жандос кинотеатр алдында күтеді; екеуі ұялып кездесіп, киноға кіреді.",
  loc="Qarakat's bedroom with a tall mirror in late-afternoon light; then a city square in front of a lit cinema at blue hour, with blank unreadable signage.",
  tl=[("0–4 s", "Over QARAKAT's shoulder into a tall mirror: she is dressed for the date; two rejected outfits lie on the bed behind her. She re-pins her high bun, adjusts a silver hoop earring, takes a nervous breath and smiles at her reflection."),
      ("4–7 s", "CUT TO the cinema square: ZHANDOS adjusts the collar of his bomber jacket, checks the time on his phone, then looks up to screen-right and smiles nervously — he sees her."),
      ("7–15 s", "QARAKAT walks in from screen-right and stops in front of him. A shy pause: both smile, look down, look up; he gives a small awkward wave, she laughs softly. They turn and walk together screen-left toward the glowing cinema entrance. Final frame: the two side by side, seen from a three-quarter back view.")],
  cam="50mm over-the-shoulder into the mirror with a slow push-in; 50mm medium on Zhandos; 35mm medium-wide two-shot with a slow push-in during the greeting.",
  light="Warm window light in the bedroom; blue-hour sky mixed with warm street lamps and the cinema glow.",
  sound="Fabric rustle, a hairpin click; city evening ambience; their soft laughter (no clear words); the warm acoustic guitar theme. No dialogue.",
  avoid="mismatched mirror reflection, readable signs or posters",
  fb="19, 20, 21",
  seam="Кинотеатр кіреберісінің жарығынан қараңғы залға кесу (жарық арқылы өту).")

G(n=10, scene=5, kk="Кино, кафе, кітап, құшақ", en="Cinema, Café, Bookstore, Goodbye",
  cast=[("ZH", "ZH_DATE"), ("QA", "QA_DATE")], extra=[],
  sum="Кинода, кафеде, кітап дүкенінде бірге; түнде есік алдында Қарақат оны кенет құшақтап, үйге кіріп кетеді.",
  loc="A dark cinema auditorium; a cosy café; a bookstore aisle with plain unreadable book spines; the lit entrance of Qarakat's apartment building at night.",
  tl=[("0–3 s", "Dark cinema: Zhandos (screen-left) and Qarakat (screen-right) sit side by side, lit by the flickering light of the off-screen projection; she steals a glance at him, he notices, both smile."),
      ("3–6 s", "CUT TO a cosy café: across a small wooden table he tells a story with his hands; she laughs, covering her mouth."),
      ("6–9 s", "CUT TO a bookstore aisle: she shows him a book; their shoulders touch; they smile."),
      ("9–15 s", "CUT TO night at the steps of her building: they stop, a shy silent pause; QARAKAT suddenly gives him a quick hug, then runs up the steps and inside, the glass door closing behind her. ZHANDOS stands alone, surprised, then breaks into a wide quiet smile. Final frame: close on his smile under the street lamp.")],
  cam="50mm two-shots for the cinema, café and bookstore; 35mm static medium-wide at the door, ending on an 85mm-feel close-up of his smile.",
  light="Projector flicker; warm café pendants; warm bookstore light; at night one street lamp and the warm glow of the entrance door.",
  sound="Muffled indistinct film sound, café murmur, pages rustling, the door's soft click, his quiet laugh; the guitar theme throughout. No dialogue.",
  avoid="the cinema screen or film footage in frame, readable book titles",
  fb="22, 23, 24, 25, 26",
  seam="Жандостың күлкісінен монтаждағы түнгі қоңырауға (жүз сәйкестігі); монтаж әні басталады.")

G(n=11, scene=6, kk="Бірге өткен бақытты күндер", en="Our Happy Days",
  cast=[("ZH", None), ("QA", None)], extra=[],
  wardrobe_override=[
      "0–9 s (night call, horses, sofa): Zhandos in his black three-stripe hoodie and track pants; Qarakat in her oversized dark-navy hoodie and grey joggers with the silver dog-tag pendant.",
      "9–15 s (café, night walk): Zhandos in a black bomber jacket, white T-shirt and dark jeans; Qarakat in a cream knit sweater and navy pleated midi skirt.",
  ],
  sum="Жылдам монтаж: түнгі қоңырау, атқа міну, үйдегі кино кеші, кафе, түнгі серуен.",
  loc="Five quick locations: their bedrooms at night, golden steppe grassland, a cosy living room at night, a sunny café window, a city street at night.",
  tl=[("0–3 s", "Night: QARAKAT lies on her bed hugging a pillow, phone at her ear, laughing quietly — CUT TO ZHANDOS on his bed in the dark, phone at his ear, smiling with his eyes closed."),
      ("3–6 s", "CUT TO golden steppe in daylight: they ride two calm brown horses side by side at a slow walk; she laughs and looks at him."),
      ("6–9 s", "CUT TO a living room at night: under a knitted blanket on a sofa, watching a film (the TV is off-frame, its light on their faces); she rests her head on his shoulder."),
      ("9–12 s", "CUT TO a sunny café window: they clink coffee cups and laugh."),
      ("12–15 s", "CUT TO a city street at night: walking hand in hand toward the camera, swinging their joined hands, laughing and looking at each other.")],
  cam="Each cut lands on the music beat: close-ups at pillow level, a side tracking shot with the horses, a frontal two-shot on the sofa, a side two-shot in the café, a leading track on the street.",
  light="Moonlight and lamp glow; bright warm sun on the steppe; TV glow; sunny window; warm street lamps.",
  sound="One romantic song across the whole clip, every cut on a beat; hooves, popcorn, cups, footsteps under it. No dialogue.",
  avoid="the TV screen or film footage in frame, recognisable film characters, unnatural horse legs",
  note="Сценарийде кино кеші — «Гарри Поттер». Авторлық құқыққа байланысты фильмнің өзі кадрда көрсетілмейді.",
  fb="27, 28, 29, 30, 31, 32",
  seam="Түнгі көше шамдарынан күн батудың алтын жарығына 1,5 с dissolve; ән сөніп, толқын дыбысы кіреді.")

G(n=12, scene=7, kk="Теңіз жағасы", en="The Seaside",
  cast=[("ZH", "ZH_SEA"), ("QA", "QA_SEA")], extra=[],
  sum="Күн батарда теңіз жағасындағы пикник; Жандос оның қолын алып: «Білесің бе, сені алғаш көрген күнім…»",
  loc="A quiet sandy seashore at sunset: a calm sea, the sun low over the horizon, a golden-pink sky; a romantic picnic on the sand — a low wooden table on a cream blanket with cushions, white and blush flowers, plates of sweets, glowing candle jars. Zhandos sits on the left, Qarakat on the right. No other people.",
  tl=[("0–5 s", "Wide shot from behind: ZHANDOS (left) and QARAKAT (right) sit side by side at the picnic facing the sea; they talk quietly, she laughs and leans her shoulder against his. The camera pushes in slowly."),
      ("5–15 s", 'CUT TO over Qarakat\'s shoulder onto Zhandos: he turns to her, takes her hand in both of his, looks into her eyes and says slowly and sincerely: "Білесің бе, сені алғаш көрген күнім әлі есімде. Сол кезде сенің бір күнің менің бүкіл өмірімді өзгертетінін білмеппін." Final frame: Zhandos holding her hand, looking into her eyes, swallowing nervously.')],
  cam="35mm wide from behind with a slow push-in, then an 85mm-feel over-the-shoulder medium close-up, static with a barely perceptible drift.",
  light="Warm low sun backlighting them, a golden rim on hair and shoulders, soft candle fill on faces, no lens flares.",
  sound="Gentle waves, a light breeze, her soft laugh; slow strings that drop very low under his voice. Dialogue in Kazakh with the exact words above.",
  avoid="other people on the beach, oversaturated sky",
  fb="33, 34",
  seam="Кадр / кері кадр: Жандостың даусы үзілмей, Қарақаттың ірі планына кесу (L-cut).")

G(n=13, scene=7, kk="«Келісесің бе?»", en="Will You?",
  cast=[("ZH", "ZH_SEA"), ("QA", "QA_SEA")], extra=[],
  sum="Қарақат тыңдап отыр, көзі жасаурайды; Жандос сақина қорабын ашып: «Қарақат, менің өмірлік серігім болуға келісесің бе?»",
  loc="The same sunset seashore picnic: candles, flowers, sweets on the low table, the calm sea and the low sun.",
  tl=[("0–8 s", 'Over Zhandos\'s shoulder (his back to the camera) onto QARAKAT, listening, her hand in his. His voice continues: "Басында сенімен танысу үшін қанша тырысқанымды өзің де білесің. Бүгін сенімен бірге болашаққа қадам басқым келеді..." At "қанша тырысқанымды" she laughs softly, remembering; then her face grows serious and her eyes begin to glisten.'),
      ("8–15 s", 'CUT TO a medium two-shot in profile, the sun on the horizon between them: ZHANDOS takes a small dark ring box from his pocket and opens it toward her, revealing a simple gold ring with a small stone: "Қарақат, менің өмірлік серігім болуға келісесің бе?" Qarakat\'s hand rises to her mouth; tears fill her eyes. Final frame: the open ring box and her hand over her mouth.')],
  cam="85mm-feel over-the-shoulder close-up on Qarakat, static; then a 50mm static two-shot in profile.",
  light="Warm sunset light on her face, candle fill, golden backlight in the profile shot.",
  sound="Waves; strings slowly rising, then near-silence before the question. Dialogue in Kazakh with the exact words above.",
  avoid="an oversized or glowing ring, magical sparkles",
  fb="35, 36",
  seam="Тығыз жалғау: G13 соңғы кадрын (ашық қорап, Қарақаттың қолы аузында) G14-ке бастапқы сурет етіп беріңіз.")

G(n=14, scene=7, kk="«Иә»", en="Yes",
  cast=[("ZH", "ZH_SEA"), ("QA", "QA_SEA")], extra=[],
  sum="Қарақат басын изеп келіседі; Жандос сақинаны тағады; құшақтасады; камера теңіз бен күн батуға шегінеді.",
  loc="The same sunset seashore picnic.",
  tl=[("0–6 s", "Close two-shot: QARAKAT lowers her hand, smiles through her tears and nods several times; ZHANDOS, beaming, takes out the ring and gently slides it onto her ring finger; they look down at the ring, then into each other's eyes."),
      ("6–15 s", "They embrace, her chin on his shoulder, her eyes closed. The camera slowly pulls back and rises: the glowing candles and flowers, the empty beach, the calm sea, the sun touching the horizon. Final frame: a wide shot of the small embracing couple beside their glowing picnic.")],
  cam="85mm-feel close two-shot with a very slow push-in, then one smooth, slow pull-back and rise like a crane, stable and graceful, no spinning.",
  light="Golden sunset rim light, candles glowing warmer as the light fades, real tears, natural skin.",
  sound="No words. Waves; the strings swell on her nod and resolve into a warm chord.",
  avoid="distorted fingers, the ring changing shape, a drone circling them",
  fb="37, 38",
  seam="Күн батудың алтын жарығынан той таңының ақ жарығына 1,5 с dissolve; ішекті аккорд той әуеніне ұласады.")

G(n=15, scene=8, kk="Тойға дайындық", en="Getting Ready",
  cast=[("ZH", "ZH_SUIT"), ("QA", "QA_BRIDE")], extra=["A helper: only her hands are visible, never her face."],
  sum="Қарақат той көйлегін киеді, Жандос костюмін түзейді; сақиналар; гүл шоғы.",
  loc="A bright bridal room with a full-length mirror; a hotel room with a mirror; a white table by a window.",
  tl=[("0–4 s", "Bright bridal room: QARAKAT in her white wedding gown stands before a full-length mirror; a helper's hands fasten the back of the gown; she smooths the skirt and smiles at her reflection, the veil falling from her high bun."),
      ("4–8 s", "CUT TO ZHANDOS in his black suit in front of a mirror, buttoning his jacket and straightening his tie; a confident breath, a small smile."),
      ("8–11 s", "CUT TO a macro shot: two simple gold wedding bands in an open white velvet box by a window; a slow slide, soft light catching the gold."),
      ("11–15 s", "CUT TO a close-up of Qarakat's hands holding a bouquet of white roses and eucalyptus against her gown, the engagement ring on her finger; a rack focus from soft to sharp.")],
  cam="50mm over-the-shoulder into mirrors; macro for the rings; 85mm close-up with a rack focus for the bouquet.",
  light="Bright soft window light, white and warm gold tones.",
  sound="Celebratory wedding music; fabric rustle. No dialogue.",
  avoid="mismatched mirror reflections, the helper's face, text on the ring box",
  fb="39, 40, 41, 42",
  seam="Гүл шоғынан камераның алға жылжуымен той залына; музыка үдейді.")

G(n=16, scene=8, kk="Бірге алға", en="Together, Forward",
  cast=[("ZH", "ZH_SUIT"), ("QA", "QA_BRIDE")], extra=["Relatives of both families and two staff members (supporting, generic faces)."],
  sum="Той залы, екі жақтың қуанышты жүздері; Жандос пен Қарақат қол ұстасып, камераға қарай жүреді.",
  loc="A grand wedding banquet hall: crystal chandeliers, round tables with white tablecloths and gold accents, white and blush flowers, a wide aisle leading to tall double doors.",
  tl=[("0–4 s", "The camera glides slowly forward along the aisle between the decorated tables under glowing chandeliers; two staff members place the last flowers."),
      ("4–8 s", "CUT TO relatives of both families in festive clothes, smiling, hugging each other and applauding toward the doors."),
      ("8–15 s", "CUT TO the tall double doors swinging open: ZHANDOS (screen-left) and QARAKAT (screen-right, bouquet in her other hand) walk hand in hand toward the camera, glance at each other and smile, radiant. Warm light fills the frame as they come close. Final frame: the two of them close to the camera, smiling, bathed in warm light.")],
  cam="24–35mm rectilinear dolly forward; 50mm slow lateral drift past the guests; the camera moves backward ahead of the couple, wide to medium.",
  light="Warm chandelier light and a warm backlight from the doorway, white and gold, natural skin.",
  sound="Wedding music building to its peak, applause, joyful voices (no clear words).",
  avoid="an extra bride or groom, duplicate faces, fisheye distortion",
  note="Финалдық жазу монтажда қосылады (қара экран, ~5 с): «ЖАНДОС ❤️ ҚАРАҚАТ / Бір кездейсоқ көзқарастан басталған махаббат... / Бүгін мәңгілікке жалғасты. / Енді олар бір-бірінің өмірлік серігі! / Бақытты болыңыздар!» Нағыз той болса, 4–8 с бөлігін шынайы туыстардың бейнежазбасымен ауыстырған жақсы.",
  fb="43, 44, 45",
  seam="Жарық кадрды толтырады → қара экран, ақ жазулар; той әуенінің соңғы аккорды.")

SCENES = {1: "Алғашқы көзқарас", 2: "Араймен танысу", 3: "Нөмір үшін келіссөз", 4: "Жауапсыз хабарламалар",
          5: "Алғашқы кездесу", 6: "Бірге өткен бақытты күндер", 7: "Теңіз жағасындағы ұсыныс", 8: "Тойға дайындық"}


def tc(s):
    return f"{s // 60:02d}:{s % 60:02d}"


def build_prompt(c):
    keys = [k for k, _ in c["cast"]]
    num = {k: i + 1 for i, k in enumerate(keys)}
    L = ["Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.", ""]
    names = {'ZH': 'ZHANDOS', 'QA': 'QARAKAT', 'AR': 'ARAI'}
    refs = " ".join(f"@image{num[k]} = {names[k]}." for k in keys)
    L += ["REFERENCES: " + refs + " Use these images only for the characters' faces, hair and body proportions; keep them identical in every shot.", ""]
    L.append("CHARACTERS & WARDROBE:")
    for k, w in c["cast"]:
        line = "- " + ID[k].format(n=num[k])
        if w:
            line += " Wearing: " + WARD[w] + "."
        L.append(line)
    for w in c.get("wardrobe_override", []):
        L.append("- " + w)
    for e in c["extra"]:
        L.append("- " + e)
    L += ["", "LOCATION: " + c["loc"], "", "TIMELINE:"]
    for r, t in c["tl"]:
        L.append(f"{r}: {t}")
    L += ["", "CAMERA: " + c["cam"], "LIGHTING: " + c["light"], "SOUND: " + c["sound"], "", "STYLE: " + STYLE,
          "AVOID: " + AVOID + (", " + c["avoid"] if c.get("avoid") else "") + "."]
    return "\n".join(L)


HEAD = """# «БІР НӨМІРДЕН БАСТАЛҒАН МАХАББАТ» — Grok нұсқасы

Жандос ❤️ Қарақат · **16 клип × 15 секунд = 4:00** · 16:9 · Grok қосымшасына арналған

Бұл файл `FILM.md` негізінде жасалған: сценарий, кейіпкерлер кітабы және кадр-кадрмен жазылған резерв промпттар сонда тұр. Мұнда әр клип 15 секундқа және үш бөлікке бөлінген (0–5, 5–10, 10–15 с). Оқиға мен диалогтар бұрынғыдай, сөзбе-сөз сақталған.

> **Кім қай суретте (тексеріңіз):** Жандос — ер адамның парағы; Қарақат — шашы түйілген, күміс сырғалы қыз; Арай — бұйра каштан шашты, сепкілді қыз.

---

## Grok-та қалай жасау керек

1. **Референстерді дайындаңыз.** Әр кейіпкердің парағынан бір бөлікті кесіп алыңыз: бет пен иықтар алдынан көрінетін бөлікті. Бүкіл торды жүктемеңіз. Арайдың парағындағы төңкерілген бөлікті қолданбаңыз.
2. **Әр клипте:** Grok → Imagine → Video, ұзақтығы **15 с**, пропорция **16:9**. Әр клиптің үстінде жазылған **ретпен** суреттерді жүктеңіз: `@image1`, `@image2`, `@image3` нөмірлері жүктеу ретіне байланысты.
3. **Промптты** код блогынан толық көшіріп қойыңыз.
4. **Grok бір ғана сурет қабылдаса:** алдымен Grok-тың сурет режимінде клиптің бірінші кадрын кейіпкерлермен бірге жасаңыз, сосын сол суретті видеоға айналдырыңыз.
5. **Бір клипте бірнеше кадр.** Көп клипте 15 секунд ішінде «CUT TO» бар. Grok оларды араластырып жіберсе, сол клипті `FILM.md`-дегі қысқа промпттармен бөліп жасаңыз («Резерв» бағаны).
6. **Тығыз жалғаулар:** G05→G06 және G13→G14. Алдыңғы клиптің соңғы кадрын скриншот алып, келесі клипке бастапқы сурет етіп беріңіз.
7. **Музыка.** Grok әр клипке өз музыкасын жасайды, сондықтан клиптер жалғанғанда әуен үзіліп-ауысып тұрады. Монтажда Grok музыкасын өшіріп, бүкіл фильмге бір саундтрек қойыңыз. Диалог пен табиғи дыбыстарды қалдырыңыз.
8. **Қазақша диалог.** Grok қазақша қате айтуы мүмкін. Дыбысты кейін өз дауыстарыңызбен немесе ElevenLabs арқылы ауыстырыңыз.
9. **Мәтін — тек монтажда:** телефон хабарламалары (G07) мен финалдық жазу (G16-дан кейін).
10. **Нұсқаларға дайын болыңыз.** Ешбір промпт беттің дәл ұқсас шығуына кепілдік бермейді. Диалогы бар клиптерге 2–3 нұсқа жасауға тура келуі мүмкін.

---
"""


def build():
    out = [HEAD, "## Клиптер тізімі\n", "| Клип | Тайм-код | Сцена | Не болады | Жүктеу реті | Резерв (FILM.md) |", "|---|---|---|---|---|---|"]
    for i, c in enumerate(CLIPS):
        a = i * 15
        up = ", ".join(f"{j + 1} — {KK[k]}" for j, (k, _) in enumerate(c["cast"]))
        out.append(f"| G{c['n']:02d} | {tc(a)}–{tc(a + 15)} | {c['scene']} | {c['sum']} | {up} | {c['fb']} |")
    out.append(f"| Финал | {tc(240)}–{tc(245)} | — | Қара экран, ақ жазулар (монтажда) | — | — |\n")
    out.append("---\n\n## Grok промпттары\n")
    cur = None
    for i, c in enumerate(CLIPS):
        if c["scene"] != cur:
            cur = c["scene"]
            out.append(f"### {cur}-сцена · {SCENES[cur]}\n")
        a = i * 15
        up = " · ".join(f"**{j + 1}** — {KK[k]}" for j, (k, _) in enumerate(c["cast"]))
        out.append(f"**G{c['n']:02d} — {c['kk']} · {tc(a)}–{tc(a + 15)}**  ")
        out.append(f"{c['sum']}  ")
        out.append(f"Жүктеу реті: {up}\n")
        out.append("```text\n" + build_prompt(c) + "\n```")
        if c.get("note"):
            out.append(f"> {c['note']}")
        out.append("")
    out.append("---\n\n## Клиптердің жалғануы\n")
    for i, c in enumerate(CLIPS):
        nxt = f"G{CLIPS[i + 1]['n']:02d}" if i + 1 < len(CLIPS) else "Финал"
        out.append(f"- **G{c['n']:02d} → {nxt}:** {c['seam']}")
    out.append("")
    text = "\n".join(out)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "GROK-15s.md"), "w", encoding="utf-8") as f:
        f.write(text)
    lens = [len(build_prompt(c)) for c in CLIPS]
    print(f"GROK-15s.md: {len(CLIPS)} clips, {len(CLIPS) * 15}s, prompt chars {min(lens)}–{max(lens)}")


if __name__ == "__main__":
    build()
