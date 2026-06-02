import { writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';
import { findSteamAppById } from '@moddota/find-steam-app';
import VPK from '../build/util/vpk';
import { deserialize, isKvObject, KVObject } from 'valve-kv';

async function buildLocalization() {
  const dota2Dir = await findSteamAppById(570);
  if (!dota2Dir) {
    throw new Error('Could not locate a Dota 2 installation');
  }
  console.log(`Found Dota 2: ${dota2Dir}`);

  console.log('Opening game VPK...');
  const gameVpk = new VPK(join(dota2Dir, 'game', 'dota', 'pak01_dir.vpk'));
  gameVpk.load();

  const locFiles = (gameVpk.files as string[]).filter(
    (f) => f.startsWith('resource/localization/') && f.endsWith('.txt'),
  );
  console.log(`Found ${locFiles.length} localization files`);

  const byLanguage: Record<string, Record<string, string>> = {};

  for (const filePath of locFiles) {
    const fileName = filePath.split('/').pop()!.replace('.txt', '');
    const lastUnderscore = fileName.lastIndexOf('_');
    if (lastUnderscore === -1) continue;
    const language = fileName.slice(lastUnderscore + 1);

    let tokens: Record<string, string>;
    try {
      const text = gameVpk.getFile(filePath).toString('utf8');
      const parsed = deserialize(text);
      const root = parsed[Object.keys(parsed)[0]] as KVObject;
      const tokensRaw = root?.Tokens ?? root?.tokens;
      if (!tokensRaw || !isKvObject(tokensRaw)) continue;
      tokens = tokensRaw as unknown as Record<string, string>;
    } catch (e) {
      console.warn(`  Warning: failed to parse ${filePath}: ${e}`);
      continue;
    }

    if (!byLanguage[language]) byLanguage[language] = {};
    for (const [key, value] of Object.entries(tokens)) {
      if (typeof key === 'string' && typeof value === 'string' && !key.startsWith('[english]')) {
        byLanguage[language][key] = value;
      }
    }
  }

  const outDir = join('files', 'localization');
  mkdirSync(outDir, { recursive: true });

  for (const [language, tokens] of Object.entries(byLanguage)) {
    const outPath = join(outDir, `${language}.json`);
    writeFileSync(outPath, JSON.stringify(tokens, null, 2), 'utf8');
    console.log(`✔ ${language}: ${Object.keys(tokens).length} tokens → ${outPath}`);
  }

  console.log(`✔ Done. Wrote ${Object.keys(byLanguage).length} language files to ${outDir}`);
}

buildLocalization().catch((error) => {
  console.error(error);
  process.exit(1);
});
