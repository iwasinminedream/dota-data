/// <reference path="../build/vpk.d.ts" />
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { findSteamAppById } from '@moddota/find-steam-app';
import vpk from 'vpk';

// ============================================================================
// Static configuration
// ============================================================================

// Modifiers that grant a single generic property (status, immunity, vision,
// stat bonus, etc.) and are not tied to a specific hero or item.
const GENERIC_MODIFIERS = new Set<string>([
  'modifier_attack_immune',
  'modifier_attribute_bonus',
  'modifier_bashed',
  'modifier_bonus_armor',
  'modifier_bonus_damage',
  'modifier_bonus_mres',
  'modifier_break',
  'modifier_debuff_immune',
  'modifier_disable_healing',
  'modifier_disable_taunt_animation_cancel',
  'modifier_disarmed',
  'modifier_dominated',
  'modifier_fear',
  'modifier_followthrough',
  'modifier_generic_hidden',
  'modifier_hexxed',
  'modifier_hidden_nodamage',
  'modifier_hide_on_minimap',
  'modifier_hp_regen',
  'modifier_ice_slide',
  'modifier_illusion',
  'modifier_invisible',
  'modifier_invisible_truesight_immune',
  'modifier_invulnerable',
  'modifier_invulnerable_hidden',
  'modifier_kill',
  'modifier_knockback',
  'modifier_magic_immune',
  'modifier_movespeed_percentage',
  'modifier_mp_regen',
  'modifier_muted',
  'modifier_no_healthbar',
  'modifier_no_invisibility',
  'modifier_not_on_minimap',
  'modifier_pet',
  'modifier_phased',
  'modifier_prevent_taunts',
  'modifier_projectile_vision',
  'modifier_projectile_vision_on_minimap',
  'modifier_provide_vision',
  'modifier_rooted',
  'modifier_rooted_undispellable',
  'modifier_silence',
  'modifier_stunned',
  'modifier_taunt',
  'modifier_teleporting',
  'modifier_teleporting_root_logic',
  'modifier_truesight',
  'modifier_truesight_all',
  'modifier_truesight_aura',
  'modifier_truesight_fow',
]);

// Aliases for heroes whose internal name differs from the spelling that
// appears in some modifier names. The key MUST exist in activelist.txt.
const HERO_ALIASES: Record<string, string[]> = {
  abyssal_underlord: ['underlord', 'abyssal_underling'],
  rattletrap: ['clockwerk'],
  invoker: ['forged_spirit'],
  magnataur: ['magnus'],
  necrolyte: ['necrophos', 'death_seeker'],
  ringmaster: ['ring_master'],
  juggernaut: ['jugg'],
  naga_siren: ['naga'],
  obsidian_destroyer: ['obsidian_destroy', 'obsidian'],
  omniknight: ['omninight'],
  pudge: ['butcher'],
  skywrath_mage: ['skywrath'],
  slardar: ['slithereen'],
  vengefulspirit: ['vengeful_spirit', 'vengeful'],
  wisp: ['io'],
  windrunner: ['windranger'],
  zuus: ['zeus'],
  furion: ['natures_prophet'],
  shredder: ['timbersaw'],
  skeleton_king: ['wraith_king'],
  witch_doctor: ['voodoo'],
};

// Modifier prefixes that indicate event/seasonal/holdout content.
// Anything that starts with `modifier_<prefix>` lands in the `event` group.
const EVENT_PREFIXES = [
  'aghsfort',
  'mutation',
  'nian',
  'ascension',
  'boss_',
  'greevil',
  'seasonal',
  'event',
  'holdout',
  'plus_high_five',
  'monster_hunter',
];

// Modifier names that should land in `event` even though their prefix doesn't
// match EVENT_PREFIXES. Add as needed.
const EVENT_EXACT = new Set<string>(['modifier_duel_accepted']);

// Manual overrides for sub-modifiers that don't share any token with the
// hero name or its abilities (so heuristics can't catch them).
// Format: modifier name → group name (hero key, "neutral", "event", etc.).
const MODIFIER_OVERRIDES: Record<string, string> = {
  modifier_do_not_cast_smash: 'neutral',
  modifier_do_not_cast_rock: 'neutral',
  modifier_do_not_cast_ensnare: 'neutral',
};

// Extra creature category words to look for inside modifier names. These are
// safe substrings (no hero collision) used as a fallback when the unit name
// from npc_units.txt doesn't appear verbatim in the modifier name.
// Order matters only for readability — matching is substring-based.
const EXTRA_NEUTRAL_TOKENS = [
  'wildkin',
  'furbolg',
  'gnoll',
  'kobold',
  'satyr',
  'wolf',
  'golem',
  'harpy',
  'mudgolem',
  'hellbear',
  'dragonspawn',
  'thunder_lizard',
  'fel_beast',
  'frostbitten',
  'forest_troll',
  'hill_troll',
  'dark_troll',
  'frogmen',
  'corpselord',
  'pine_cone',
  'greevil',
  'spawnlord',
  'roshan',
];

// ============================================================================
// Main builder
// ============================================================================

async function buildModifiers() {
  const dota2Dir = await findSteamAppById(570);
  if (!dota2Dir) {
    throw new Error('Could not locate a Dota 2 installation');
  }
  console.log(`Found Dota 2: ${dota2Dir}`);

  console.log('Opening game VPK...');
  const gameVpk = new vpk(join(dota2Dir, 'game', 'dota', 'pak01_dir.vpk'));
  gameVpk.load();

  const heroListText = gameVpk.getFile('scripts/npc/activelist.txt').toString();
  const abilityListText = gameVpk.getFile('scripts/npc/npc_ability_ids.txt').toString();
  const neutralNamesText = gameVpk.getFile('scripts/npc/npc_units.txt').toString();

  const heroList = heroListText
    .split(/\r?\n/)
    .map((l: string) => l.trim())
    .filter((l: string) => /^"npc_dota_hero_/.test(l))
    .map((l: string) => l.match(/^"npc_dota_hero_(.+?)"/)?.[1])
    .filter((x: string | undefined): x is string => Boolean(x));

  const abilityList = abilityListText
    .split(/\r?\n/)
    .map((l: string) => l.trim())
    .filter((l: string) => /^"[a-zA-Z0-9_]+"/.test(l))
    .map((l: string) => l.match(/^"(.+?)"/)?.[1])
    .filter((x: string | undefined): x is string => Boolean(x));

  // Item list — prefer the authoritative abilities.json (built by build-abilities,
  // which includes items.txt) over npc_ability_ids.txt which can lag behind.
  let itemList = abilityList.filter((a: string) => a.startsWith('item_'));
  let abilitiesJson: Record<string, unknown> = {};
  const abilitiesJsonPath = join('files', 'abilities.json');
  if (existsSync(abilitiesJsonPath)) {
    abilitiesJson = JSON.parse(readFileSync(abilitiesJsonPath, 'utf8')) as Record<string, unknown>;
    const itemsFromJson = Object.keys(abilitiesJson).filter((k) => k.startsWith('item_'));
    itemList = Array.from(new Set([...itemList, ...itemsFromJson]));
    console.log(`Loaded items from abilities.json: ${itemsFromJson.length}`);
  }

  const NeutralList: string[] = [];
  for (const line of neutralNamesText.split('\n')) {
    const m = line.match(/"npc_dota_neutral_([^"]+)"/);
    if (m) NeutralList.push(m[1]);
  }
  for (const t of EXTRA_NEUTRAL_TOKENS) NeutralList.push(t);

  // ---------------------------------------------------------------------------
  // Hero alias map (every hero gets at least its canonical name + a no-underscore
  // variant; HERO_ALIASES adds extra aliases on top)
  // ---------------------------------------------------------------------------
  const heroAliases: Record<string, string[]> = {};
  for (const hero of heroList) {
    const aliases = new Set<string>([hero]);
    if (hero.includes('_')) aliases.add(hero.replace(/_/g, ''));
    for (const extra of HERO_ALIASES[hero] || []) {
      aliases.add(extra);
      if (extra.includes('_')) aliases.add(extra.replace(/_/g, ''));
    }
    heroAliases[hero] = [...aliases];
  }

  // Sorted alias → hero list (longer aliases first, so 'naga_siren' beats 'naga')
  const aliasEntries: { alias: string; hero: string; regex: RegExp }[] = [];
  for (const [hero, aliases] of Object.entries(heroAliases)) {
    for (const alias of aliases) {
      const escaped = alias.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      aliasEntries.push({ alias, hero, regex: new RegExp(`(^|_)${escaped}(_|$)`) });
    }
  }
  aliasEntries.sort((a, b) => b.alias.length - a.alias.length);

  // ---------------------------------------------------------------------------
  // Authoritative ability → hero map (built by build-abilities.ts from
  // scripts/npc/heroes/*.txt). Falls back to alias-prefix matching.
  // ---------------------------------------------------------------------------
  const abilityHeroMapPath = join('files', 'ability-hero-map.json');
  let abilityHeroMap: Record<string, string> = {};
  if (existsSync(abilityHeroMapPath)) {
    abilityHeroMap = JSON.parse(readFileSync(abilityHeroMapPath, 'utf8'));
    console.log(`Loaded ability-hero-map: ${Object.keys(abilityHeroMap).length} entries`);
  } else {
    console.warn(`! ability-hero-map.json not found — run build:abilities first for best results`);
  }

  const abilityToHero = new Map<string, string>();
  for (const [ability, hero] of Object.entries(abilityHeroMap)) {
    if (heroList.includes(hero)) abilityToHero.set(ability, hero);
  }

  // ---------------------------------------------------------------------------
  // Build a sorted list of all known abilities (longest name first) for direct
  // ability matching. Each entry knows whether the ability belongs to a hero
  // (in which case the modifier is assigned to that hero) or is a creature/unit
  // ability (in which case the modifier is assigned to neutral).
  // ---------------------------------------------------------------------------
  const allAbilityNames = new Set<string>();
  for (const a of abilityList) {
    if (!a.startsWith('item_') && !a.startsWith('special_bonus')) allAbilityNames.add(a);
  }
  for (const a of Object.keys(abilitiesJson)) {
    if (!a.startsWith('item_') && !a.startsWith('special_bonus')) allAbilityNames.add(a);
  }
  const knownAbilities: { name: string; hero: string | null }[] = [];
  for (const name of allAbilityNames) {
    knownAbilities.push({ name, hero: abilityHeroMap[name] || null });
  }
  knownAbilities.sort((a, b) => b.name.length - a.name.length);

  // ---------------------------------------------------------------------------
  // Hero ability suffix map (e.g. 'chilling_touch' → 'crystal_maiden') for
  // matching modifiers that use the ability name without the hero prefix.
  // ---------------------------------------------------------------------------
  const suffixEntries: { suffix: string; hero: string }[] = [];
  for (const [ability, hero] of abilityToHero) {
    for (const alias of heroAliases[hero] || []) {
      if (ability.startsWith(alias + '_')) {
        const suffix = ability.substring(alias.length + 1);
        if (suffix.length >= 5) suffixEntries.push({ suffix, hero });
        break;
      }
    }
  }
  suffixEntries.sort((a, b) => b.suffix.length - a.suffix.length);

  // ---------------------------------------------------------------------------
  // Read all modifier names from the dumper output
  // ---------------------------------------------------------------------------
  const dumpTxt = readFileSync(join('dumper', 'dump'), 'utf8');
  const allModifiers = Array.from(
    new Set(dumpTxt.split(/\r?\n/).filter((l) => l.startsWith('modifier_'))),
  );

  const SpecCheckFilter = ['roshan', 'rune', 'special_bonus'];

  const result: Record<string, string[]> = {
    generic: [],
    neutral: [],
    event: [],
    items: [],
    other: [],
  };

  const pushTo = (group: string, mod: string) => {
    if (!result[group]) result[group] = [];
    result[group].push(mod);
  };

  const eventPrefixRegex = new RegExp(
    `^modifier_(${EVENT_PREFIXES.map((p) => p.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})`,
  );

  for (const mod of allModifiers) {
    const modBody = mod.substring('modifier_'.length);
    let assigned = false;

    // 1. Manual overrides
    if (MODIFIER_OVERRIDES[mod]) {
      pushTo(MODIFIER_OVERRIDES[mod], mod);
      continue;
    }

    // 2. Generic property modifiers
    if (GENERIC_MODIFIERS.has(mod)) {
      result.generic.push(mod);
      continue;
    }

    // 3. Events (greevil, seasonal, miniboss-event content, etc.)
    if (EVENT_EXACT.has(mod) || eventPrefixRegex.test(mod)) {
      result.event.push(mod);
      continue;
    }

    // 4. Special groups (roshan, rune, special_bonus)
    for (const name of SpecCheckFilter) {
      if (mod.includes(name)) {
        pushTo(name, mod);
        assigned = true;
        break;
      }
    }
    if (assigned) continue;

    // 5. Items
    for (const item of itemList) {
      const itemBase = item.replace('item_', '');
      if (
        mod.includes(`modifier_${itemBase}`) ||
        mod.includes(`modifier_eul_${itemBase}`) ||
        mod.includes(`modifier_${item}`) ||
        mod.includes('modifier_item_')
      ) {
        result.items.push(mod);
        assigned = true;
        break;
      }
    }
    if (assigned) continue;

    // 6. Hero alias right after `modifier_` (high confidence — alias appears at
    //    the very start of the modifier name).
    for (const { alias, hero } of aliasEntries) {
      if (mod === `modifier_${alias}` || mod.startsWith(`modifier_${alias}_`)) {
        pushTo(hero, mod);
        assigned = true;
        break;
      }
    }
    if (assigned) continue;

    // 7. Direct ability match — modBody equals or starts with a known ability
    //    name (longest match wins). Hero abilities go to the hero, creature
    //    abilities go to neutrals.
    for (const { name, hero } of knownAbilities) {
      if (modBody === name || modBody.startsWith(name + '_')) {
        if (hero) {
          pushTo(hero, mod);
        } else {
          result.neutral.push(mod);
        }
        assigned = true;
        break;
      }
    }
    if (assigned) continue;

    // 8. Hero ability suffix as prefix of modBody — for modifiers that use the
    //    ability name without the hero prefix (e.g. modifier_chilling_touch).
    //    Note: only prefix-style match — no endsWith, to avoid creature
    //    modifiers being misclassified as heroes.
    for (const { suffix, hero } of suffixEntries) {
      if (modBody === suffix || modBody.startsWith(suffix + '_')) {
        pushTo(hero, mod);
        assigned = true;
        break;
      }
    }
    if (assigned) continue;

    // 9. Neutrals — substring match against npc_units.txt names + extra tokens
    for (const name of NeutralList) {
      if (mod.includes(name)) {
        result.neutral.push(mod);
        assigned = true;
        break;
      }
    }
    if (!assigned && /^modifier_(creature|creep|neutral)/.test(mod)) {
      result.neutral.push(mod);
      assigned = true;
    }
    if (assigned) continue;

    // 10. Hero alias anywhere (last-resort, lowest confidence)
    for (const { hero, regex } of aliasEntries) {
      if (regex.test(mod)) {
        pushTo(hero, mod);
        assigned = true;
        break;
      }
    }
    if (assigned) continue;

    // 11. Fallback
    result.other.push(mod);
  }

  // Deduplicate and sort all groups
  for (const key in result) {
    result[key] = Array.from(new Set(result[key])).sort();
  }

  const outPath = join('files', 'vscripts', 'modifier_list.json');
  mkdirSync(dirname(outPath), { recursive: true });
  writeFileSync(outPath, JSON.stringify(result, null, 2), 'utf8');

  const totalAssigned = Object.values(result).reduce((acc, arr) => acc + arr.length, 0);
  console.log(
    `✔ Grouped ${totalAssigned} modifiers (${result.other.length} unassigned) → ${outPath}`,
  );
}

buildModifiers().catch((error) => {
  console.error(error);
  process.exit(1);
});
