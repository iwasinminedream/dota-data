import { writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { findSteamAppById } from '@moddota/find-steam-app';
import vpk from 'vpk';
import { deserialize, isKvObject, KVObject } from 'valve-kv';

async function buildAbilities() {
  const dota2Dir = await findSteamAppById(570);
  if (!dota2Dir) {
    throw new Error('Could not locate a Dota 2 installation');
  }
  console.log(`Found Dota 2: ${dota2Dir}`);

  console.log('Opening game VPK...');
  const gameVpk = new vpk(join(dota2Dir, 'game', 'dota', 'pak01_dir.vpk'));
  gameVpk.load();

  // Extract base npc_abilities.txt
  console.log('Extracting npc_abilities.txt...');
  const abilitiesText = gameVpk.getFile('scripts/npc/npc_abilities.txt').toString();

  console.log('Parsing abilities KV...');
  const parsed = deserialize(abilitiesText);
  const root = parsed[Object.keys(parsed)[0]] as KVObject;

  // Remove metadata
  delete root.Version;

  // Extract hero ability files from scripts/npc/heroes/
  const heroFiles = gameVpk.files.filter(
    (f: string) => f.startsWith('scripts/npc/heroes/') && f.endsWith('.txt'),
  );
  console.log(`Found ${heroFiles.length} hero ability files`);

  for (const filePath of heroFiles) {
    try {
      const text = gameVpk.getFile(filePath).toString();
      const heroParsed = deserialize(text);
      const heroRoot = heroParsed[Object.keys(heroParsed)[0]] as KVObject;
      if (heroRoot && typeof heroRoot === 'object') {
        for (const [key, value] of Object.entries(heroRoot)) {
          if (key === 'Version') continue;
          root[key] = value;
        }
      }
    } catch (e) {
      console.warn(`  Warning: failed to parse ${filePath}: ${e}`);
    }
  }

  // Extract items.txt
  console.log('Extracting items.txt...');
  const itemsText = gameVpk.getFile('scripts/npc/items.txt').toString();
  const itemsParsed = deserialize(itemsText);
  const itemsRoot = itemsParsed[Object.keys(itemsParsed)[0]] as KVObject;
  delete itemsRoot.Version;

  for (const [key, value] of Object.entries(itemsRoot)) {
    root[key] = value;
  }

  // Convert string numbers to actual numbers recursively
  parseNumbersRecursive(root);

  // Remove duplicate keys (keep last)
  removeDuplicates(root);

  const outPath = join('files', 'abilities.json');
  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(outPath, JSON.stringify(root, null, 2), 'utf8');

  const count = Object.keys(root).length;
  console.log(`✔ Extracted ${count} abilities + items → ${outPath}`);
}

function parseNumbersRecursive(object: KVObject) {
  for (const [key, value] of Object.entries(object)) {
    if (typeof value === 'string' && value.length > 0) {
      // Preserve strings with operators: "+10", "+50%", "*2", "/3" etc.
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

buildAbilities().catch((error) => {
  console.error(error);
  process.exit(1);
});
