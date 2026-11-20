// Kazakh voiceover, one MP3 per sentence scene.
// Usage: node tools/voiceover.mjs [from] [to]   (1-based scene numbers, inclusive)
// The SDK reads ELEVENLABS_API_KEY from the environment; never put the key here.
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "fs";

const VOICE_ID = process.env.VO_VOICE_ID || "JBFqnCBsd6RMkjVDRZzb"; // George (pre-made, narrative)
const MODEL_ID = "eleven_v4";

const plan = JSON.parse(readFileSync("boards/plan.json", "utf8"));

// What is spoken can differ from the on-screen sentence: full wording, numbers as words.
const SPOKEN = {
  18: "Бүгін біз адам психологиясындағы өте қызықты құбылыс — әлеуметтік салыстыру туралы сөйлесеміз.",
};
const NUMBERS = [
  [/1954 жылы/g, "Мың тоғыз жүз елу төртінші жылы"],
  [/25 жасында/g, "жиырма бес жасында"],
  [/30 жаста/g, "отыз жаста"],
  [/300 мың/g, "үш жүз мың"],
];
const spoken = (s) => {
  let t = SPOKEN[s.n] || s.text;
  for (const [re, w] of NUMBERS) t = t.replace(re, w);
  return t;
};

const from = Number(process.argv[2] || 1);
const to = Number(process.argv[3] || plan.length);
mkdirSync("assets/voice", { recursive: true });
const client = new ElevenLabsClient();

for (const s of plan) {
  if (s.n < from || s.n > to) continue;
  const out = `assets/voice/${s.id}.mp3`;
  if (existsSync(out)) continue;
  const prev = plan.find((p) => p.n === s.n - 1);
  const next = plan.find((p) => p.n === s.n + 1);
  const audio = await client.textToSpeech.convert(VOICE_ID, {
    text: spoken(s),
    modelId: MODEL_ID,
    languageCode: "kk",
    previousText: prev ? spoken(prev) : undefined,
    nextText: next ? spoken(next) : undefined,
    outputFormat: "mp3_44100_128",
    voiceSettings: { stability: 0.5, similarityBoost: 0.75 },
  });
  const chunks = [];
  for await (const c of audio) chunks.push(Buffer.from(c));
  writeFileSync(out, Buffer.concat(chunks));
  console.log(`${s.id}  ${spoken(s)}`);
}
