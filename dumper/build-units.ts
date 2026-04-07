import { writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { findSteamAppById } from '@moddota/find-steam-app';
import vpk from 'vpk';
import { deserialize, isKvObject, KVObject } from 'valve-kv';

async function buildUnits() {
  const dota2Dir = await findSteamAppById(570);
  if (!dota2Dir) {
    throw new Error('Could not locate a Dota 2 installation');
  }
  console.log(`Found Dota 2: ${dota2Dir}`);

  console.log('Opening game VPK...');
  const gameVpk = new vpk(join(dota2Dir, 'game', 'dota', 'pak01_dir.vpk'));
  gameVpk.load();

  const result: KVObject = {};

  // Extract npc_units.txt
  console.log('Extracting npc_units.txt...');
  const unitsText = gameVpk.getFile('scripts/npc/npc_units.txt').toString();
  const unitsParsed = deserialize(unitsText);
  const unitsRoot = unitsParsed[Object.keys(unitsParsed)[0]] as KVObject;
  delete unitsRoot.Version;
  Object.assign(result, unitsRoot);

  // Extract npc_heroes.txt
  console.log('Extracting npc_heroes.txt...');
  try {
    const heroesText = gameVpk.getFile('scripts/npc/npc_heroes.txt').toString();
    const heroesParsed = deserialize(heroesText);
    const heroesRoot = heroesParsed[Object.keys(heroesParsed)[0]] as KVObject;
    delete heroesRoot.Version;
    Object.assign(result, heroesRoot);
  } catch (e) {
    console.warn(`Warning: failed to parse npc_heroes.txt: ${e}`);
  }

  parseNumbersRecursive(result);
  removeDuplicates(result);

  const outPath = join('files', 'units.json');
  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(outPath, JSON.stringify(result, null, 2), 'utf8');

  const count = Object.keys(result).length;
  console.log(`✔ Extracted ${count} units/heroes → ${outPath}`);
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
