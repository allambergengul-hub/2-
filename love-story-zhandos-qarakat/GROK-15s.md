# «БІР НӨМІРДЕН БАСТАЛҒАН МАХАББАТ» — Grok нұсқасы

Жандос ❤️ Қарақат · **16 клип × 15 секунд = 4:00** · 16:9 · Grok қосымшасына арналған

Бұл файл `FILM.md` негізінде жасалған: сценарий, кейіпкерлер кітабы және кадр-кадрмен жазылған резерв промпттар сонда тұр. Мұнда әр клип 15 секундқа және үш бөлікке бөлінген (0–5, 5–10, 10–15 с). Оқиға мен диалогтар бұрынғыдай, сөзбе-сөз сақталған.

> **Референстер — әр клипте үшеуін де, осы ретпен жүктеңіз:** **1** — Жандос (`1000098369.jpg`), **2** — Қарақат (`1000098361.jpg`), **3** — Арай (`1000098562.jpg`).
> **Беттер мен киімдер барлық клипте референстегідей, өзгеріссіз.** Жалғыз ерекшелік — той (G15–G16): сценарий бойынша Қарақат ақ көйлек, Жандос костюм киеді.

---

## Grok-та қалай жасау керек

1. **Референстер.** Үш парақты толық жүктеңіз, әр клипте бірдей ретпен: 1 — Жандос, 2 — Қарақат, 3 — Арай. Промптта `@image1/2/3` осы ретке сілтейді, ал «IN THIS CLIP» жолы кім кадрда бар, кім жоқ екенін айтады.
2. **Әр клипте:** Grok → Imagine → Video, ұзақтығы **15 с**, пропорция **16:9**, үш суретті жүктеп, промптты толық қойыңыз.
3. **Тор немесе көшірмелер шықса:** Grok кадрға парақтың торын немесе бір адамның бірнеше көшірмесін шығарса, әр парақтан бет пен толық бойды бөлек кесіп алып, соларды жүктеңіз (рет сол күйінде: 1, 2, 3).
4. **Grok бір ғана сурет қабылдаса:** алдымен Grok-тың сурет режимінде клиптің бірінші кадрын кейіпкерлермен бірге жасаңыз, сосын сол суретті видеоға айналдырыңыз.
5. **Бір клипте бірнеше кадр.** Көп клипте 15 секунд ішінде «CUT TO» бар. Grok оларды араластырып жіберсе, сол клипті `FILM.md`-дегі қысқа промпттармен бөліп жасаңыз («Резерв» бағаны).
6. **Тығыз жалғаулар:** G05→G06 және G13→G14. Алдыңғы клиптің соңғы кадрын скриншот алып, келесі клипке бастапқы сурет етіп беріңіз.
7. **Музыка.** Grok әр клипке өз музыкасын жасайды, сондықтан клиптер жалғанғанда әуен үзіліп-ауысып тұрады. Монтажда Grok музыкасын өшіріп, бүкіл фильмге бір саундтрек қойыңыз. Диалог пен табиғи дыбыстарды қалдырыңыз.
8. **Қазақша диалог.** Grok қазақша қате айтуы мүмкін. Дыбысты кейін өз дауыстарыңызбен немесе ElevenLabs арқылы ауыстырыңыз.
9. **Мәтін — тек монтажда:** телефон хабарламалары (G07) мен финалдық жазу (G16-дан кейін).
10. **Нұсқаларға дайын болыңыз.** Ешбір промпт беттің дәл ұқсас шығуына кепілдік бермейді. Диалогы бар клиптерге 2–3 нұсқа жасауға тура келуі мүмкін.

---

## Клиптер тізімі

| Клип | Тайм-код | Сцена | Не болады | Кадрда | Резерв (FILM.md) |
|---|---|---|---|---|---|
| G01 | 00:00–00:15 | 1 | Ойын бітті, Қарақат құрбыларымен шығып барады; Жандос оны көріп қалады: «Анау қыз кім өзі?» | Жандос, Қарақат | 01, 02, 03 |
| G02 | 00:15–00:30 | 1 | Достарында нөмір жоқ; Жандос сыртқа жүгіреді, бірақ Қарақат таксиге отырып кетіп қалады. | Жандос, Қарақат | 03, 04 |
| G03 | 00:30–00:45 | 2 | Келесі күні Қарақат кафеден кетеді, Арай жалғыз шығады; Жандос онымен танысып, Қарақатты сұрайды. | Жандос, Қарақат, Арай | 05, 06 |
| G04 | 00:45–01:00 | 2 | Арай нөмірді рұқсатсыз бермейді; саябақта Қарақатқа айтады — Қарақат бас тартады. | Жандос, Қарақат, Арай | 07, 08 |
| G05 | 01:00–01:15 | 3 | Үшінші күні Жандос Арайға ақша ұсынады; Арай «Ойланып көрейін... Үстінен қос!» дейді. | Жандос, Арай | 09, 10 |
| G06 | 01:15–01:30 | 3 | Жандос тағы ақша қосады; Арай нөмірді береді: «Мә, бірақ мен бергенімді айтпа!» Жандос қуанады. | Жандос, Арай | 11, 12 |
| G07 | 01:30–01:45 | 4 | Жандос алғаш жазады; Қарақат оқиды, бірақ жауап бермейді; бірнеше күннен соң Жандос тағы жазады. | Жандос, Қарақат | 13, 14, 15 |
| G08 | 01:45–02:00 | 4 | Арай: «Мүмкіндік беріп көр». Кешке Қарақат жауап жазады — Жандос қуанып, бірден жауап жазады. | Жандос, Қарақат, Арай | 16, 17, 18 |
| G09 | 02:00–02:15 | 5 | Қарақат айна алдында дайындалады; Жандос кинотеатр алдында күтеді; екеуі ұялып кездесіп, киноға кіреді. | Жандос, Қарақат | 19, 20, 21 |
| G10 | 02:15–02:30 | 5 | Кинода, кафеде, кітап дүкенінде бірге; түнде есік алдында Қарақат оны кенет құшақтап, үйге кіріп кетеді. | Жандос, Қарақат | 22, 23, 24, 25, 26 |
| G11 | 02:30–02:45 | 6 | Жылдам монтаж: түнгі қоңырау, атқа міну, үйдегі кино кеші, кафе, түнгі серуен. | Жандос, Қарақат | 27, 28, 29, 30, 31, 32 |
| G12 | 02:45–03:00 | 7 | Күн батарда теңіз жағасындағы пикник; Жандос оның қолын алып: «Білесің бе, сені алғаш көрген күнім…» | Жандос, Қарақат | 33, 34 |
| G13 | 03:00–03:15 | 7 | Қарақат тыңдап отыр, көзі жасаурайды; Жандос сақина қорабын ашып: «Қарақат, менің өмірлік серігім болуға келісесің бе?» | Жандос, Қарақат | 35, 36 |
| G14 | 03:15–03:30 | 7 | Қарақат басын изеп келіседі; Жандос сақинаны тағады; құшақтасады; камера теңіз бен күн батуға шегінеді. | Жандос, Қарақат | 37, 38 |
| G15 | 03:30–03:45 | 8 | Қарақат той көйлегін киеді, Жандос костюмін түзейді; сақиналар; гүл шоғы. | Жандос, Қарақат | 39, 40, 41, 42 |
| G16 | 03:45–04:00 | 8 | Той залы, екі жақтың қуанышты жүздері; Жандос пен Қарақат қол ұстасып, камераға қарай жүреді. | Жандос, Қарақат | 43, 44, 45 |
| Финал | 04:00–04:05 | — | Қара экран, ақ жазулар (монтажда) | — | — |

---

## Grok промпттары

### 1-сцена · Алғашқы көзқарас

**G01 — Алғашқы көзқарас · 00:00–00:15**  
Ойын бітті, Қарақат құрбыларымен шығып барады; Жандос оны көріп қалады: «Анау қыз кім өзі?»  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.
- Qarakat's teammates (supporting, soft focus): young women in black leggings and white or grey T-shirts — none in a navy or cream hoodie, none with a high bun or hoop earrings.
- Zhandos's two friends (supporting, never in close-up): one with buzz-cut hair in a grey hoodie, one in a black cap and dark-green track jacket.

LOCATION: An indoor volleyball gym in the evening: polished honey-coloured wooden floor, a net, wooden bleachers along the BACK wall, exit double doors in the LEFT wall.
SPACE & EYELINES: Zhandos and his friends stand at the RIGHT end of the bleachers. Qarakat walks from right to left toward the exit doors — away from him. Everything Zhandos looks at is to his LEFT, so he always looks screen-LEFT. When his face is on screen, Qarakat is OFF-SCREEN left, never in the background behind him.

TIMELINE:
0–4 s: SHOT 1 — low wide from the near side of the court, facing the back wall: exit doors at screen-left, Zhandos and two friends small and still at the right end of the bleachers. A volleyball lying on the floor in the foreground bounces twice, low, and rolls out of frame left. QARAKAT and two teammates walk from screen-right to screen-left, side-on to the camera, toward the exit, laughing. Qarakat carries nothing.
4–8 s: SHOT 2 — over-the-shoulder from directly behind ZHANDOS: the back of his head and right shoulder soft in the right foreground; he slowly turns his head left. Sharp in the middle distance at screen-left, Qarakat walks away from him toward the exit doors. We see what he sees.
8–11 s: SHOT 3 — close-up of ZHANDOS in three-quarter profile facing screen-LEFT; behind him only the bleachers, no girls. His eyes stay fixed off-screen left, past the lens, following her; his smile fades, he blinks once and says quietly and slowly, every word separate: "Анау қыз... кім өзі?"
11–15 s: SHOT 4 — eye-level three-shot: FRIEND 1 (buzz-cut, grey hoodie) at screen-left, Zhandos centre, FRIEND 2 (black cap, green track jacket) at screen-right. Friend 1 glances left toward the exit and answers casually: "Қайсы? Қарақат па? Ол біздің танысымыз ғой." Zhandos turns his head left to him, interested; Friend 2 smiles, silent.

CAMERA: 24mm low wide → 50mm over-the-shoulder with Qarakat in focus → 85mm close-up → 40mm three-shot; hard cuts; the 180-degree line is kept — Zhandos always looks screen-left.
LIGHTING: Even overhead LED panels, warm bounce from the wooden floor, natural skin tones.
SOUND: Two low ball bounces, sneakers squeaking, indistinct happy chatter; the gym noise fades in Shot 2 and a soft piano note begins. Kazakh dialogue, exact words, slow and clear: "Анау қыз кім өзі?" is four separate words, never merged; "..." is a short pause.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, Qarakat or the exit doors behind Zhandos in his close-up, Zhandos looking right, Zhandos walking onto the court, the girls walking toward the camera, a bag on Qarakat, white or cream trousers on Qarakat, swept-back hair on Zhandos.
```

**G02 — Кешікті · 00:15–00:30**  
Достарында нөмір жоқ; Жандос сыртқа жүгіреді, бірақ Қарақат таксиге отырып кетіп қалады.  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.
- Zhandos's two friends (supporting, never in close-up): one with buzz-cut hair in a grey hoodie, one in a black cap and dark-green track jacket.
- Qarakat's teammates (supporting, soft focus): young women in black leggings and white or grey T-shirts — none in a navy or cream hoodie, none with a high bun or hoop earrings.

LOCATION: Inside: the same evening volleyball gym — bleachers along the back wall, exit doors in the left wall. Outside: the sports complex at night — wide concrete steps, glass doors glowing at screen-right, a quiet street running left–right, warm street lamps.

TIMELINE:
0–5 s: Medium three-shot by the bleachers. ZHANDOS turns to his friend, eager: "Қарақат дейсің бе? Нөмірі бар ма?" FRIEND 2 shrugs: "Жоқ, нөмірі бізде жоқ." Zhandos immediately hurries out of frame screen-left toward the exit.
5–10 s: CUT TO outside at night, wide shot from across the street: a white taxi waits at the curb; the teammates get in, QARAKAT (navy hoodie, high bun, silver hoops) gets in last and the door shuts; the taxi pulls away screen-left. The glass doors at screen-right swing open and Zhandos runs down the steps.
10–15 s: Zhandos slows and stops at the curb, watching the red tail lights shrink into the distance; he exhales and gives a small rueful smile to himself. Final frame: Zhandos alone at the curb in a three-quarter back view under the street lamps.

CAMERA: Handheld 40mm three-shot, then a locked-off 35mm wide across the street, ending with a slow push-in toward his back.
LIGHTING: Gym LED light inside; outside warm sodium street lamps, cool blue night, red tail lights.
SOUND: Dialogue in Kazakh with the exact words above; the door pushed open; a car door shutting, the engine pulling away, a quiet night street; the piano phrase stops unresolved.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, readable licence plates or taxi branding.
```

### 2-сцена · Араймен танысу

**G03 — «Сен Арайсың ғой?» · 00:30–00:45**  
Келесі күні Қарақат кафеден кетеді, Арай жалғыз шығады; Жандос онымен танысып, Қарақатты сұрайды.  
Кадрда: Жандос, Қарақат, Арай · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2), ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.
- ARAI (@image3): the young woman from @image3 — keep her exact face and body proportions; never a look-alike. Twenties, warm smiley face with light freckles, long curly chestnut-brown hair in a high curly ponytail tied with a black hair tie. Outfit: exactly the outfit from @image3, unchanged: oversized cream-ivory hoodie with pale-pink drawstrings and a small pale-pink heart on the left chest, black track pants with two white side stripes, pink-and-white low-top sneakers.
- Qarakat's teammates (supporting, soft focus): young women in black leggings and white or grey T-shirts — none in a navy or cream hoodie, none with a high bun or hoop earrings.

LOCATION: A small modern café on a quiet city street in daylight: a glass front and glass door, two small outdoor tables, a tree-lined sidewalk running left–right.

TIMELINE:
0–4 s: QARAKAT and one teammate step out of the café door laughing and walk off screen-right. The door swings shut; a moment later it opens again and ARAI steps out alone in her cream hoodie, glancing at her phone.
4–9 s: ZHANDOS walks up from screen-left and stops in front of her — medium two-shot in profile, Zhandos screen-left, Arai screen-right. Rubbing the back of his neck: "Сәлем! Сен Арайсың ғой?" Arai: "Иә, не болды?"
9–15 s: Zhandos: "Бір нәрсе сұрайын деп едім. Қарақат деген қызды танисың ба?" Arai raises one eyebrow and tilts her head: "Иә, танимын. Неге?" Final frame: Arai's sceptical half-smile as she waits for his answer.

CAMERA: 35mm wide-medium from across the sidewalk, then a 50mm medium two-shot in profile with subtle handheld breathing.
LIGHTING: Soft overcast daylight, neutral natural colours.
SOUND: A small door chime, street ambience, footsteps, a light playful pizzicato tune; dialogue in Kazakh with the exact words above.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, readable café name or menu, the two women looking alike.
```

**G04 — «Рұқсатынсыз бере алмаймын» · 00:45–01:00**  
Арай нөмірді рұқсатсыз бермейді; саябақта Қарақатқа айтады — Қарақат бас тартады.  
Кадрда: Жандос, Қарақат, Арай · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2), ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.
- ARAI (@image3): the young woman from @image3 — keep her exact face and body proportions; never a look-alike. Twenties, warm smiley face with light freckles, long curly chestnut-brown hair in a high curly ponytail tied with a black hair tie. Outfit: exactly the outfit from @image3, unchanged: oversized cream-ivory hoodie with pale-pink drawstrings and a small pale-pink heart on the left chest, black track pants with two white side stripes, pink-and-white low-top sneakers.

LOCATION: First the café sidewalk in daylight, then a tree-lined park alley with a paved path and wooden benches, the same day.

TIMELINE:
0–7 s: Over Zhandos's shoulder (soft in the left foreground) onto ARAI: Zhandos asks: "Сол қызбен танысқым келіп жүр. Нөмірін бере аласың ба?" Arai shakes her head, polite but firm: "Жоқ, рұқсатынсыз бере алмаймын. Алдымен өзінен сұрайын." She nods and walks away screen-right.
7–11 s: CUT TO the park alley: QARAKAT stands by a bench at screen-right looking at her phone; Arai walks into frame from screen-left and leans in with a playful smile: "Қарақат, саған бір жігіт қызығып жүр. Аты Жандос. Нөміріңді сұрап жатыр."
11–15 s: Qarakat lifts her eyebrows in surprise, then shakes her head with a shy half-smile: "Жоқ, бермей-ақ қойшы. Танымаймын ғой." She looks down and tucks her hands into her hoodie pocket, hiding a smile. Final frame: Qarakat looking down, Arai shrugging.

CAMERA: 50mm over-the-shoulder, static; then a 50mm medium two-shot at eye level with gentle handheld breathing.
LIGHTING: Overcast daylight at the café, then dappled sunlight through the park trees.
SOUND: Dialogue in Kazakh with the exact words above; footsteps; birdsong and rustling leaves in the park; playful pizzicato.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, the two women looking alike.
```

### 3-сцена · Нөмір үшін келіссөз

**G05 — «Үстінен қос!» · 01:00–01:15**  
Үшінші күні Жандос Арайға ақша ұсынады; Арай «Ойланып көрейін... Үстінен қос!» дейді.  
Кадрда: Жандос, Арай · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), ARAI (@image3) only. Not in this clip: QARAKAT (@image2).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- ARAI (@image3): the young woman from @image3 — keep her exact face and body proportions; never a look-alike. Twenties, warm smiley face with light freckles, long curly chestnut-brown hair in a high curly ponytail tied with a black hair tie. Outfit: exactly the outfit from @image3, unchanged: oversized cream-ivory hoodie with pale-pink drawstrings and a small pale-pink heart on the left chest, black track pants with two white side stripes, pink-and-white low-top sneakers.
- Zhandos's two friends (supporting, never in close-up): one with buzz-cut hair in a grey hoodie, one in a black cap and dark-green track jacket.

LOCATION: In front of the sports complex in the late afternoon: wide concrete steps, glass doors, a pale facade, young trees, the sidewalk running left–right.

TIMELINE:
0–5 s: ZHANDOS comes down the steps with his two friends, spots ARAI on the sidewalk and jogs over (Zhandos screen-left, Arai screen-right): "Арай, Қарақат не деді? Нөмірін бермеді ме?" Arai shakes her head: "Жоқ, келіспеді."
5–10 s: Locked-off medium two-shot. Zhandos's shoulders drop; he thinks, lips pressed, then pulls a few folded banknotes from his hoodie pocket and holds them out with a sly, hopeful smile: "Мынаған келісе алмаймыз ба?"
10–15 s: Arai looks at the money, then at him, narrows her eyes and weighs it theatrically: "Ойланып көрейін..." — a beat of silence — then, deadpan: "Үстінен қос!" She holds out her open palm. Final frame: Arai's open palm and raised eyebrows; Zhandos frozen mid-smile.

CAMERA: Handheld 35mm follow on the steps, then a completely locked-off 40mm medium two-shot — the stillness carries the comedy.
LIGHTING: Low warm late-afternoon sun from screen-left, soft golden rim light.
SOUND: Dialogue in Kazakh with the exact words above; footsteps on concrete; playful music that stops for the pause and comes back on "Үстінен қос!".

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, close-up fake banknote designs.
```

**G06 — Нөмір сақталды · 01:15–01:30**  
Жандос тағы ақша қосады; Арай нөмірді береді: «Мә, бірақ мен бергенімді айтпа!» Жандос қуанады.  
Кадрда: Жандос, Арай · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), ARAI (@image3) only. Not in this clip: QARAKAT (@image2).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- ARAI (@image3): the young woman from @image3 — keep her exact face and body proportions; never a look-alike. Twenties, warm smiley face with light freckles, long curly chestnut-brown hair in a high curly ponytail tied with a black hair tie. Outfit: exactly the outfit from @image3, unchanged: oversized cream-ivory hoodie with pale-pink drawstrings and a small pale-pink heart on the left chest, black track pants with two white side stripes, pink-and-white low-top sneakers.

LOCATION: The same spot in front of the sports complex, late afternoon.

TIMELINE:
0–5 s: Same locked-off two-shot: ZHANDOS sighs with a laugh and places more banknotes into ARAI's open palm. She tucks the money into her hoodie pocket.
5–10 s: Arai takes out her phone and turns the screen toward him (away from the camera), whispering: "Мә, бірақ мен бергенімді айтпа!" Zhandos quickly types the number into his own phone. Arai walks off screen-right with a knowing look.
10–15 s: CUT TO a close-up of Zhandos's hands; his thumb taps save; the camera tilts up to his face as he breaks into a wide, boyish grin and gives a small fist pump. Final frame: his grin in golden light.

CAMERA: 40mm two-shot with a very slow push-in, then an 85mm close-up with a smooth tilt up from hands to face.
LIGHTING: Low golden-hour sun from screen-left, warm rim light on his hair.
SOUND: Dialogue in Kazakh with the exact words above; soft screen taps; the playful music lands on one bright final note.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, readable phone screens or numbers.
```

### 4-сцена · Жауапсыз хабарламалар

**G07 — Жауапсыз хабарламалар · 01:30–01:45**  
Жандос алғаш жазады; Қарақат оқиды, бірақ жауап бермейді; бірнеше күннен соң Жандос тағы жазады.  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.

LOCATION: Zhandos's small bedroom (bed, wooden desk with a lamp, window with city lights) and Qarakat's bedroom (white bedding, bedside lamp, sheer curtains).

TIMELINE:
0–5 s: Night, Zhandos's bedroom: ZHANDOS sits on the edge of his bed, phone in both hands; he types, hesitates, deletes, types again and sends — one, two, three messages.
5–10 s: CUT TO Qarakat's bedroom at night: QARAKAT lies on her stomach on her bed; her phone lights up and buzzes. She reads, a tiny smile flickers, she bites her lip, then places the phone face-down and looks away toward the window.
10–15 s: CUT TO Zhandos's room in daylight, days later: he picks up the phone from his desk, checks it — nothing — sends one more short message, puts the phone down and leans back with a sigh, running a hand through his hair.

CAMERA: 50mm medium shots at eye level, static, shallow depth of field.
LIGHTING: Night: warm lamps and the cool glow of phones on their faces. Day: soft flat window light — the colour of waiting.
SOUND: Screen taps, message-sent sounds, a phone vibrating on the bedspread, quiet rooms, sparse piano notes. No dialogue.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, readable phone screens.
```
> Монтажда хабарлама көпіршіктерін қосыңыз: 0–5 с — «Сәлем, Қарақат!», «Қалайсың?», «Таныссақ бола ма?»; 10–15 с — «Неге жауап бермейсің?»

**G08 — Ол жауап берді · 01:45–02:00**  
Арай: «Мүмкіндік беріп көр». Кешке Қарақат жауап жазады — Жандос қуанып, бірден жауап жазады.  
Кадрда: Жандос, Қарақат, Арай · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2), ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.
- ARAI (@image3): the young woman from @image3 — keep her exact face and body proportions; never a look-alike. Twenties, warm smiley face with light freckles, long curly chestnut-brown hair in a high curly ponytail tied with a black hair tie. Outfit: exactly the outfit from @image3, unchanged: oversized cream-ivory hoodie with pale-pink drawstrings and a small pale-pink heart on the left chest, black track pants with two white side stripes, pink-and-white low-top sneakers.

LOCATION: A tree-lined park alley in daytime; then Qarakat's bedroom and Zhandos's bedroom at night.

TIMELINE:
0–7 s: Park alley: ARAI (screen-left) and QARAKAT (screen-right) walk toward the camera; Arai gently bumps Qarakat's shoulder: "Қарақат, бір сөйлесіп көрсеңші. Жігіт жаман емес сияқты. Мүмкіндік беріп көр." Qarakat slows down, thinking, a small undecided smile.
7–11 s: CUT TO Qarakat's bedroom at night: she sits cross-legged on her bed, takes a breath, types a short reply and taps send, then hugs her knees with a shy smile.
11–15 s: CUT TO Zhandos's bedroom at night: ZHANDOS lies on his back, the phone on his chest buzzes; he reads, sits bolt upright with a huge grin and immediately starts typing back fast.

CAMERA: 35mm leading track walking backward in the park; 85mm close-up on Qarakat; 35mm medium on Zhandos rising as he sits up.
LIGHTING: Dappled park sunlight; at night warm lamps and phone glow.
SOUND: Dialogue in Kazakh with the exact words above; birdsong; a message-sent sound, then a vibration and message tone; a warm acoustic guitar begins at the end.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, readable phone screens, the two women looking alike.
```

### 5-сцена · Алғашқы кездесу

**G09 — Алғашқы кездесу · 02:00–02:15**  
Қарақат айна алдында дайындалады; Жандос кинотеатр алдында күтеді; екеуі ұялып кездесіп, киноға кіреді.  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.

LOCATION: Qarakat's bedroom with a tall mirror in late-afternoon light; then a city square in front of a lit cinema at blue hour, with blank unreadable signage.

TIMELINE:
0–4 s: Over QARAKAT's shoulder into a tall mirror: she is in her navy hoodie with the silver dog-tag pendant, getting ready for the date; two other outfits she decided against lie on the bed behind her. She re-pins her high bun, adjusts a silver hoop earring, takes a nervous breath and smiles at her reflection.
4–7 s: CUT TO the cinema square: ZHANDOS straightens his three-stripe hoodie, smooths his hair, checks the time on his phone, then looks up to screen-right and smiles nervously — he sees her.
7–15 s: QARAKAT walks in from screen-right and stops in front of him. A shy pause: both smile, look down, look up; he gives a small awkward wave, she laughs softly. They turn and walk together screen-left toward the glowing cinema entrance. Final frame: the two side by side, seen from a three-quarter back view.

CAMERA: 50mm over-the-shoulder into the mirror with a slow push-in; 50mm medium on Zhandos; 35mm medium-wide two-shot with a slow push-in during the greeting.
LIGHTING: Warm window light in the bedroom; blue-hour sky mixed with warm street lamps and the cinema glow.
SOUND: Fabric rustle, a hairpin click; city evening ambience; their soft laughter (no clear words); the warm acoustic guitar theme. No dialogue.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, mismatched mirror reflection, readable signs or posters.
```

**G10 — Кино, кафе, кітап, құшақ · 02:15–02:30**  
Кинода, кафеде, кітап дүкенінде бірге; түнде есік алдында Қарақат оны кенет құшақтап, үйге кіріп кетеді.  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.

LOCATION: A dark cinema auditorium; a cosy café; a bookstore aisle with plain unreadable book spines; the lit entrance of Qarakat's apartment building at night.

TIMELINE:
0–3 s: Dark cinema: Zhandos (screen-left) and Qarakat (screen-right) sit side by side, lit by the flickering light of the off-screen projection; she steals a glance at him, he notices, both smile.
3–6 s: CUT TO a cosy café: across a small wooden table he tells a story with his hands; she laughs, covering her mouth.
6–9 s: CUT TO a bookstore aisle: she shows him a book; their shoulders touch; they smile.
9–15 s: CUT TO night at the steps of her building: they stop, a shy silent pause; QARAKAT suddenly gives him a quick hug, then runs up the steps and inside, the glass door closing behind her. ZHANDOS stands alone, surprised, then breaks into a wide quiet smile. Final frame: close on his smile under the street lamp.

CAMERA: 50mm two-shots for the cinema, café and bookstore; 35mm static medium-wide at the door, ending on an 85mm-feel close-up of his smile.
LIGHTING: Projector flicker; warm café pendants; warm bookstore light; at night one street lamp and the warm glow of the entrance door.
SOUND: Muffled indistinct film sound, café murmur, pages rustling, the door's soft click, his quiet laugh; the guitar theme throughout. No dialogue.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, the cinema screen or film footage in frame, readable book titles.
```

### 6-сцена · Бірге өткен бақытты күндер

**G11 — Бірге өткен бақытты күндер · 02:30–02:45**  
Жылдам монтаж: түнгі қоңырау, атқа міну, үйдегі кино кеші, кафе, түнгі серуен.  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot.

LOCATION: Five quick locations: their bedrooms at night, golden steppe grassland, a cosy living room at night, a sunny café window, a city street at night.

TIMELINE:
0–3 s: Night: QARAKAT lies on her bed hugging a pillow, phone at her ear, laughing quietly — CUT TO ZHANDOS on his bed in the dark, phone at his ear, smiling with his eyes closed.
3–6 s: CUT TO golden steppe in daylight: they ride two calm brown horses side by side at a slow walk; she laughs and looks at him.
6–9 s: CUT TO a living room at night: under a knitted blanket on a sofa, watching a film (the TV is off-frame, its light on their faces); she rests her head on his shoulder.
9–12 s: CUT TO a sunny café window: they clink coffee cups and laugh.
12–15 s: CUT TO a city street at night: walking hand in hand toward the camera, swinging their joined hands, laughing and looking at each other.

CAMERA: Each cut lands on the music beat: close-ups at pillow level, a side tracking shot with the horses, a frontal two-shot on the sofa, a side two-shot in the café, a leading track on the street.
LIGHTING: Moonlight and lamp glow; bright warm sun on the steppe; TV glow; sunny window; warm street lamps.
SOUND: One romantic song across the whole clip, every cut on a beat; hooves, popcorn, cups, footsteps under it. No dialogue.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, the TV screen or film footage in frame, recognisable film characters, unnatural horse legs.
```
> Сценарийде кино кеші — «Гарри Поттер». Авторлық құқыққа байланысты фильмнің өзі кадрда көрсетілмейді.

### 7-сцена · Теңіз жағасындағы ұсыныс

**G12 — Теңіз жағасы · 02:45–03:00**  
Күн батарда теңіз жағасындағы пикник; Жандос оның қолын алып: «Білесің бе, сені алғаш көрген күнім…»  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.

LOCATION: A quiet sandy seashore at sunset: a calm sea, the sun low over the horizon, a golden-pink sky; a romantic picnic on the sand — a low wooden table on a cream blanket with cushions, white and blush flowers, plates of sweets, glowing candle jars. Zhandos sits on the left, Qarakat on the right. No other people.

TIMELINE:
0–5 s: Wide shot from behind: ZHANDOS (left) and QARAKAT (right) sit side by side at the picnic facing the sea; they talk quietly, she laughs and leans her shoulder against his. The camera pushes in slowly.
5–15 s: CUT TO over Qarakat's shoulder onto Zhandos: he turns to her, takes her hand in both of his, looks into her eyes and says slowly and sincerely: "Білесің бе, сені алғаш көрген күнім әлі есімде. Сол кезде сенің бір күнің менің бүкіл өмірімді өзгертетінін білмеппін." Final frame: Zhandos holding her hand, looking into her eyes, swallowing nervously.

CAMERA: 35mm wide from behind with a slow push-in, then an 85mm-feel over-the-shoulder medium close-up, static with a barely perceptible drift.
LIGHTING: Warm low sun backlighting them, a golden rim on hair and shoulders, soft candle fill on faces, no lens flares.
SOUND: Gentle waves, a light breeze, her soft laugh; slow strings that drop very low under his voice. Dialogue in Kazakh with the exact words above.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, other people on the beach, oversaturated sky.
```

**G13 — «Келісесің бе?» · 03:00–03:15**  
Қарақат тыңдап отыр, көзі жасаурайды; Жандос сақина қорабын ашып: «Қарақат, менің өмірлік серігім болуға келісесің бе?»  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.

LOCATION: The same sunset seashore picnic: candles, flowers, sweets on the low table, the calm sea and the low sun.

TIMELINE:
0–8 s: Over Zhandos's shoulder (his back to the camera) onto QARAKAT, listening, her hand in his. His voice continues: "Басында сенімен танысу үшін қанша тырысқанымды өзің де білесің. Бүгін сенімен бірге болашаққа қадам басқым келеді..." At "қанша тырысқанымды" she laughs softly, remembering; then her face grows serious and her eyes begin to glisten.
8–15 s: CUT TO a medium two-shot in profile, the sun on the horizon between them: ZHANDOS takes a small dark ring box from his pocket and opens it toward her, revealing a simple gold ring with a small stone: "Қарақат, менің өмірлік серігім болуға келісесің бе?" Qarakat's hand rises to her mouth; tears fill her eyes. Final frame: the open ring box and her hand over her mouth.

CAMERA: 85mm-feel over-the-shoulder close-up on Qarakat, static; then a 50mm static two-shot in profile.
LIGHTING: Warm sunset light on her face, candle fill, golden backlight in the profile shot.
SOUND: Waves; strings slowly rising, then near-silence before the question. Dialogue in Kazakh with the exact words above.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, an oversized or glowing ring, magical sparkles.
```

**G14 — «Иә» · 03:15–03:30**  
Қарақат басын изеп келіседі; Жандос сақинаны тағады; құшақтасады; камера теңіз бен күн батуға шегінеді.  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair, body and outfit, and keep all of it identical in every shot.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: exactly the outfit from @image1, unchanged: black adidas hoodie with three white stripes down each sleeve and a small white trefoil logo on the chest, black track pants with three white side stripes and a small white logo, white low-top sneakers with three black stripes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: exactly the outfit from @image2, unchanged: oversized plain dark-navy hoodie with dark drawstrings, a silver dog-tag pendant on a long thin chain worn over the hoodie, loose medium heather-grey jogger sweatpants with elastic cuffs — clearly grey, visibly darker than her white sneakers, not white, not cream, not beige, plain white low-top sneakers; she carries no bag or backpack.

LOCATION: The same sunset seashore picnic.

TIMELINE:
0–6 s: Close two-shot: QARAKAT lowers her hand, smiles through her tears and nods several times; ZHANDOS, beaming, takes out the ring and gently slides it onto her ring finger; they look down at the ring, then into each other's eyes.
6–15 s: They embrace, her chin on his shoulder, her eyes closed. The camera slowly pulls back and rises: the glowing candles and flowers, the empty beach, the calm sea, the sun touching the horizon. Final frame: a wide shot of the small embracing couple beside their glowing picnic.

CAMERA: 85mm-feel close two-shot with a very slow push-in, then one smooth, slow pull-back and rise like a crane, stable and graceful, no spinning.
LIGHTING: Golden sunset rim light, candles glowing warmer as the light fades, real tears, natural skin.
SOUND: No words. Waves; the strings swell on her nod and resolve into a warm chord.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles or outfits, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, distorted fingers, the ring changing shape, a drone circling them.
```

### 8-сцена · Тойға дайындық

**G15 — Тойға дайындық · 03:30–03:45**  
Қарақат той көйлегін киеді, Жандос костюмін түзейді; сақиналар; гүл шоғы.  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair and body, and keep these identical in every shot; in this wedding-day clip only, the outfits are the wedding outfits described below.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: WEDDING DAY ONLY — the story's single outfit change: classic black two-piece suit, white shirt, slim black tie, black leather shoes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: WEDDING DAY ONLY — the story's single outfit change: white wedding gown with a lace bodice and a full skirt, a sheer veil pinned under her high bun, her silver hoop earrings.
- A helper: only her hands are visible, never her face.

LOCATION: A bright bridal room with a full-length mirror; a hotel room with a mirror; a white table by a window.

TIMELINE:
0–4 s: Bright bridal room: QARAKAT in her white wedding gown stands before a full-length mirror; a helper's hands fasten the back of the gown; she smooths the skirt and smiles at her reflection, the veil falling from her high bun.
4–8 s: CUT TO ZHANDOS in his black suit in front of a mirror, buttoning his jacket and straightening his tie; a confident breath, a small smile.
8–11 s: CUT TO a macro shot: two simple gold wedding bands in an open white velvet box by a window; a slow slide, soft light catching the gold.
11–15 s: CUT TO a close-up of Qarakat's hands holding a bouquet of white roses and eucalyptus against her gown, the engagement ring on her finger; a rack focus from soft to sharp.

CAMERA: 50mm over-the-shoulder into mirrors; macro for the rings; 85mm close-up with a rack focus for the bouquet.
LIGHTING: Bright soft window light, white and warm gold tones.
SOUND: Celebratory wedding music; fabric rustle. No dialogue.

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles, any outfit other than the wedding outfits described, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, mismatched mirror reflections, the helper's face, text on the ring box, Arai appearing.
```

**G16 — Бірге алға · 03:45–04:00**  
Той залы, екі жақтың қуанышты жүздері; Жандос пен Қарақат қол ұстасып, камераға қарай жүреді.  
Кадрда: Жандос, Қарақат · Жүктеу: 1 — Жандос, 2 — Қарақат, 3 — Арай

```text
Ultra-realistic live-action cinematic film footage, 15 seconds, 16:9 landscape, real-time natural motion.

REFERENCES: @image1 = ZHANDOS, @image2 = QARAKAT, @image3 = ARAI. These are character sheets showing several views of the same person: use them for each person's exact face, hair and body, and keep these identical in every shot; in this wedding-day clip only, the outfits are the wedding outfits described below.
IN THIS CLIP: ZHANDOS (@image1), QARAKAT (@image2) only. Not in this clip: ARAI (@image3).

CHARACTERS & WARDROBE:
- ZHANDOS (@image1): the young man from @image1 — keep his exact face, facial structure, hair and body proportions; never a look-alike. Twenties, tall and lean; long oval face, straight thick dark eyebrows, narrow calm dark-brown eyes, a few small dark moles on his cheeks, clean-shaven; thick, voluminous, slightly messy jet-black hair with loose strands falling forward over his forehead, exactly as in @image1 — not swept back, not short and neat on top. Outfit: WEDDING DAY ONLY — the story's single outfit change: classic black two-piece suit, white shirt, slim black tie, black leather shoes.
- QARAKAT (@image2): the young woman from @image2 — keep her exact face, facial structure and body proportions; never a look-alike. Twenties, slim, a little shorter than Zhandos; jet-black hair always pulled back into a high round bun; calm almond-shaped dark eyes; large thin silver hoop earrings in every shot. Outfit: WEDDING DAY ONLY — the story's single outfit change: white wedding gown with a lace bodice and a full skirt, a sheer veil pinned under her high bun, her silver hoop earrings.
- Relatives of both families and two staff members (supporting, generic faces).

LOCATION: A grand wedding banquet hall: crystal chandeliers, round tables with white tablecloths and gold accents, white and blush flowers, a wide aisle leading to tall double doors.

TIMELINE:
0–4 s: The camera glides slowly forward along the aisle between the decorated tables under glowing chandeliers; two staff members place the last flowers.
4–8 s: CUT TO relatives of both families in festive clothes, smiling, hugging each other and applauding toward the doors.
8–15 s: CUT TO the tall double doors swinging open: ZHANDOS (screen-left) and QARAKAT (screen-right, bouquet in her other hand) walk hand in hand toward the camera, glance at each other and smile, radiant. Warm light fills the frame as they come close. Final frame: the two of them close to the camera, smiling, bathed in warm light.

CAMERA: 24–35mm rectilinear dolly forward; 50mm slow lateral drift past the guests; the camera moves backward ahead of the couple, wide to medium.
LIGHTING: Warm chandelier light and a warm backlight from the doorway, white and gold, natural skin.
SOUND: Wedding music building to its peak, applause, joyful voices (no clear words).

STYLE: Characters never look into the camera lens — their eyes go to the person or place the action describes. One continuous real scene, each person appears only once (the reference images are character sheets — never show a grid, collage or duplicate copies). Photorealistic live-action romantic film, natural skin texture with visible pores, natural real-time motion (no slow motion), realistic hands and physics, motivated natural light, subtle film grain, cinematic 16:9 composition.
AVOID: face changes or look-alike actors, changed hairstyles, any outfit other than the wedding outfits described, distorted hands or extra fingers, duplicate people, warped backgrounds, slow motion, exaggerated acting, waxy skin, cartoon look, readable text on screens or signs, subtitles, watermarks, logos other than those on the reference outfits, character-sheet grids or split panels, duplicate copies of a person, eye contact with the camera, an extra bride or groom, duplicate faces, fisheye distortion.
```
> Финалдық жазу монтажда қосылады (қара экран, ~5 с): «ЖАНДОС ❤️ ҚАРАҚАТ / Бір кездейсоқ көзқарастан басталған махаббат... / Бүгін мәңгілікке жалғасты. / Енді олар бір-бірінің өмірлік серігі! / Бақытты болыңыздар!» Нағыз той болса, 4–8 с бөлігін шынайы туыстардың бейнежазбасымен ауыстырған жақсы.

---

## Клиптердің жалғануы

- **G01 → G02:** G02 сол үш адамдық кадрдан, сол позициялардан басталады — монтажда тікелей кесу.
- **G02 → G03:** Түннен күндізге тікелей кесу; кафе есігінің қоңырауы кесуден сәл бұрын естіледі (J-cut).
- **G03 → G04:** Арайдың «Неге?» деген сөзінен кейінгі кідірісте Жандостың иығы үстінен түсірілген кадрға кесу.
- **G04 → G05:** Есік арқылы өту: спорт кешенінің шыны есігі ашылып, Жандос шығады; ойнақы әуен екі клипке ортақ.
- **G05 → G06:** Ең тығыз жалғау: G05 соңғы кадрын (Арайдың ашық алақаны) скриншот алып, G06-ға бастапқы сурет етіп беріңіз.
- **G06 → G07:** Телефон → телефон: күндізгі қолдағы телефоннан түнгі бөлмедегі телефонға кесу.
- **G07 → G08:** Жандостың күрсінісінен кейін Арайдың «Қарақат, бір сөйлесіп көрсеңші…» деген даусы алдын ала естіледі (J-cut).
- **G08 → G09:** Жандос «жіберу» батырмасын басқанда гитара тақырыбы басталады; бірінші соққыда айна алдындағы Қарақатқа кесу.
- **G09 → G10:** Кинотеатр кіреберісінің жарығынан қараңғы залға кесу (жарық арқылы өту).
- **G10 → G11:** Жандостың күлкісінен монтаждағы түнгі қоңырауға (жүз сәйкестігі); монтаж әні басталады.
- **G11 → G12:** Түнгі көше шамдарынан күн батудың алтын жарығына 1,5 с dissolve; ән сөніп, толқын дыбысы кіреді.
- **G12 → G13:** Кадр / кері кадр: Жандостың даусы үзілмей, Қарақаттың ірі планына кесу (L-cut).
- **G13 → G14:** Тығыз жалғау: G13 соңғы кадрын (ашық қорап, Қарақаттың қолы аузында) G14-ке бастапқы сурет етіп беріңіз.
- **G14 → G15:** Күн батудың алтын жарығынан той таңының ақ жарығына 1,5 с dissolve; ішекті аккорд той әуеніне ұласады.
- **G15 → G16:** Гүл шоғынан камераның алға жылжуымен той залына; музыка үдейді.
- **G16 → Финал:** Жарық кадрды толтырады → қара экран, ақ жазулар; той әуенінің соңғы аккорды.
