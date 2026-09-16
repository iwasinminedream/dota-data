import { writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { findSteamAppById } from '@moddota/find-steam-app';
import VPK from '../build/util/vpk';
import { deserialize, isKvObject, KVObject } from 'valve-kv';

async function buildUnits() {
  const dota2Dir = await findSteamAppById(570);
  if (!dota2Dir) {
    throw new Error('Could not locate a Dota 2 installation');
  }
  console.log(`Found Dota 2: ${dota2Dir}`);

  console.log('Opening game VPK...');
  const gameVpk = new VPK(join(dota2Dir, 'game', 'dota', 'pak01_dir.vpk'));
  gameVpk.load();

  const result: KVObject = {};

  // Extract npc_units.txt
  console.log('Extracting npc_units.txt...');
  const unitsText = gameVpk.getFile('scripts/npc/npc_units.txt').toString();
  const unitsParsed = deserialize(unitsText);
  const unitsRoot = unitsParsed[Object.keys(unitsParsed)[0]] as KVObject;
  delete unitsRoot.Version;
  Object.assign(result, unitsRoot);

  // Extract heroes. Since 6933 npc_heroes.txt only holds the #base include list –
  // every hero lives in its own scripts/npc/heroes/*.txt and carries its abilities
  // in an AbilityDefinitions block, which belongs in abilities.json, not here.
  console.log('Extracting heroes...');
  const heroFiles = resolveHeroFiles(gameVpk);
  console.log(`Found ${heroFiles.length} hero files`);

  let heroCount = 0;
  for (const filePath of heroFiles) {
    try {
      const heroesParsed = deserialize(gameVpk.getFile(filePath).toString());
      const heroesRoot = heroesParsed[Object.keys(heroesParsed)[0]] as KVObject;
      for (const [key, value] of Object.entries(heroesRoot)) {
        if (key === 'Version') continue;
        if (isKvObject(value)) delete value.AbilityDefinitions;
        result[key] = value;
        heroCount++;
      }
    } catch (e) {
      console.warn(`  Warning: failed to parse ${filePath}: ${e}`);
    }
  }

  if (heroCount < 100) {
    throw new Error(
      `Only ${heroCount} heroes found in ${heroFiles.length} files – ` +
        'the hero KV layout has probably changed again, check resolveHeroFiles()',
    );
  }

  parseNumbersRecursive(result);
  removeDuplicates(result);

  const outPath = join('files', 'units.json');
  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(outPath, JSON.stringify(result, null, 2), 'utf8');

  const count = Object.keys(result).length;
  console.log(`✔ Extracted ${count} units/heroes → ${outPath}`);

  const heroes: KVObject = {};
  for (const [key, value] of Object.entries(result)) {
    if (key.startsWith('npc_dota_hero_')) {
      heroes[key] = value;
    }
  }

  const heroesPath = join('files', 'heroes.json');
  writeFileSync(heroesPath, JSON.stringify(heroes, null, 2), 'utf8');
  console.log(`✔ Extracted ${Object.keys(heroes).length} heroes → ${heroesPath}`);
}

// npc_heroes.txt lists the hero files in the order the engine loads them ("#base order
// below sets hero order, which InitUnitNameDict relies on"), so follow it and only fall
// back to the raw VPK listing for files it does not mention.
function resolveHeroFiles(gameVpk: VPK): string[] {
  const available: string[] = gameVpk.files.filter(
    (f: string) => f.startsWith('scripts/npc/heroes/') && f.endsWith('.txt'),
  );

  const ordered: string[] = [];
  try {
    const indexText = gameVpk.getFile('scripts/npc/npc_heroes.txt').toString();
    for (const [, relativePath] of indexText.matchAll(/^\s*#base\s+"([^"]+)"/gm)) {
      const filePath = `scripts/npc/${relativePath.replace(/\\/g, '/')}`;
      if (available.includes(filePath) && !ordered.includes(filePath)) ordered.push(filePath);
    }
  } catch (e) {
    console.warn(`Warning: failed to read npc_heroes.txt: ${e}`);
  }

  return [...ordered, ...available.filter((f) => !ordered.includes(f))];
}

function parseNumbersRecursive(object: KVObject) {
  for (const [key, value] of Object.entries(object)) {
    if (typeof value === 'string' && value.length > 0) {
      if (/^[+*\/]/.test(value) || /[%]/.test(value)) continue;
      const numberValue = Number(value);
      if (!Number.isNaN(numberValue)) {
        object[key] = numberValue;
      }
    } else if (isKvObject(value)) {
      parseNumbersRecursive(value);
    }
  }
}

function removeDuplicates(object: KVObject) {
  for (const [key, value] of Object.entries(object)) {
    if (Array.isArray(value)) {
      const newValue = value[value.length - 1];
      object[key] = newValue;
      if (isKvObject(newValue)) {
        removeDuplicates(newValue);
      }
    } else if (isKvObject(value)) {
      removeDuplicates(value);
    }
  }
}

buildUnits().catch((error) => {
  console.error(error);
  process.exit(1);
});
