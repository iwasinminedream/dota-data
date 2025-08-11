import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';

async function fetchText(url: string): Promise<string> {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP ${response.status} (${response.statusText}) during load: ${url}`);
  }
  return await response.text();
}

let heroListText: string;
let abilityListText: string;
let NeutralNames: string;

async function loadData() {

  const heroUrl = 'https://raw.githubusercontent.com/spirit-bear-productions/dota_vpk_updates/refs/heads/main/scripts/npc/activelist.txt';
  const abilityUrl = 'https://raw.githubusercontent.com/spirit-bear-productions/dota_vpk_updates/refs/heads/main/scripts/npc/npc_ability_ids.txt';
  const neutralUrl = 'https://raw.githubusercontent.com/spirit-bear-productions/dota_vpk_updates/refs/heads/main/scripts/npc/npc_units.txt';

  try {
    [heroListText, abilityListText, NeutralNames] = await Promise.all([
      fetchText(heroUrl),
      fetchText(abilityUrl),
      fetchText(neutralUrl)
    ]);

    buildModifiers()

  } catch (error) {
    console.error('Error get data', error);
    return;
  }
}

async function buildModifiers() {

  const SpecCheckFilter = ["roshan", "rune", "special_bonus"]
  
  const heroList = heroListText
    .split(/\r?\n/)
    .map(line => line.trim())
    .filter(line => /^"npc_dota_hero_/.test(line))
    .map(line => line.match(/^"npc_dota_hero_(.+?)"/)?.[1])
    .filter((x): x is string => Boolean(x));
    
  const abilityList = abilityListText
  .split(/\r?\n/)
  .map(line => line.trim())
    .filter(line => /^"[a-zA-Z0-9_]+"/.test(line))
    .map(line => line.match(/^"(.+?)"/)?.[1])
    .filter((x): x is string => Boolean(x));
    
  const itemList = abilityList.filter((a) => a.startsWith("item_"));
    
  let NeutralList: string[] = [];
  const lines = NeutralNames.split('\n');
  let currentNeutral: string;
  for (const line of lines) {
    const neutralMatch = line.match(/"npc_dota_neutral_([^"]+)"/);
    if (neutralMatch) {
      currentNeutral = neutralMatch[1];
      NeutralList.push(currentNeutral);
    }
  }
  NeutralList.push("furbolg");
  NeutralList.push("miniboss");
  NeutralList.push("pine_cone");
  NeutralList.push("greevil");
      
  const dumpTxt = readFileSync(join('dumper', 'dump'), 'utf8');
  const allModifiers = dumpTxt
    .split(/\r?\n/)
    .filter(l => l.startsWith('modifier_'));

    const result: Record<string, string[]> = {
      neutral: [],
      event: [],
      items: [],
      other: [],
    };

  for (const mod of allModifiers) {
    let assigned = false;

    // Events
    if (/^modifier_(aghsfort|mutation|nian|ascension|boss_)/.test(mod)) {
      result.event.push(mod);
      continue;
    }

    // Spec
    for (const name of SpecCheckFilter) {
      if (
        mod.includes(`${name}`)
      ) {
        if (!result[name]) result[name] = [];
        result[name].push(mod);
        assigned = true;
        break;
      }
    }
    if (assigned) continue;

    // items
    for (const item of itemList) {
      if (
        mod.includes(`modifier_${item.replace("item_","")}`) ||
        mod.includes(`modifier_eul_${item}`) ||// spec fix
        mod.includes(`modifier_${item}`) ||
        mod.includes(`modifier_item_`)
        // mod.includes(`item_`)
      ) {
        result.items.push(mod);
        assigned = true;
        break;
      }
    }
    
    if (assigned) continue;

    // Heroes
    for (const hero of heroList) {
      if (!result[hero]) result[hero] = [];
      if (hero == "abyssal_underlord")
      {
        if (
          mod.includes(`${"abyssal_underling"}`)
        ) {
          result[hero].push(mod);
          assigned = true;
          break;
        }
        if (
          mod.includes(`${"underlord"}`)
        ) {
          result[hero].push(mod);
          assigned = true;
          break;
        }
      }
      if (hero == "rattletrap")
      {
        if (
          mod.includes(`${"clockwerk"}`)
        ) {
          result[hero].push(mod);
          assigned = true;
          break;
        }
      }
      if (hero == "invoker")
      {
        if (
          mod.includes(`${"forged_spirit"}`)
        ) {
          result[hero].push(mod);
          assigned = true;
          break;
        }
      }
      if (hero == "magnataur")
      {
        if (
          mod.includes(`${"magnus"}`)
        ) {
          result[hero].push(mod);
          assigned = true;
          break;
        }
      }
      if (hero == "necrolyt")
      {
        if (
          mod.includes(`${"necrophos"}`)
        ) {
          result[hero].push(mod);
          assigned = true;
          break;
        }
      }
      if (hero == "ringmaster")
      {
        if (
          mod.includes(`${"ring_master"}`)
        ) {
          result[hero].push(mod);
          assigned = true;
          break;
        }
      }
      if (
        mod.includes(`modifier_${hero}`) ||
        mod.includes(`modifier_${hero.replace("_", "")}`)
      ) {
        result[hero].push(mod);
        assigned = true;
        break;
      }
      //may add iteration through abilities that include hero name
      //its huge increace build time and i give up on it
      // for (const ability of abilityList) {
      // }
    }

    if (assigned) continue;

    // Neutrals
    for (const name of NeutralList) {
      if (
        mod.includes(`${name}`)
      ) {
        result.neutral.push(mod);
        assigned = true;
        break;
      }
    }

    if (/^modifier_(creature|creep|neutral)/.test(mod)) {
      assigned = true;
      result.neutral.push(mod);
    }

    if (assigned) continue;

    // Other
    result.other.push(mod);
  }

  // Sort
  for (const key in result) {
    result[key].sort();
  }

  const outPath = join('files', 'vscripts', 'modifier_list.json');
  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(outPath, JSON.stringify(result, null, 2), 'utf8');

  console.log(`✔ Frouped ${allModifiers.length} modifiers → ${outPath}`);
}
loadData();
