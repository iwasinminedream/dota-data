import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'fs';
import { dirname, join } from 'path';

// dumper/native_modifiers.json (written by the dumper from server.dll, see dumper/native-modifiers.mts)
// -> files/vscripts/native_modifiers.json, checked against the dump and linked to the abilities whose
// special values the formulas read. dumper/native_modifiers_client.json (the same from client.dll) is
// merged in: the client's formula where it differs from the server's, and what only one side has.

const inputPath = join('dumper', 'native_modifiers.json');
const clientPath = join('dumper', 'native_modifiers_client.json');
const dumpPath = join('dumper', 'dump');
const abilitiesPath = join('files', 'abilities.json');
const outputPath = join('files', 'vscripts', 'native_modifiers.json');

interface NativeValue {
  status: 'constant' | 'formula' | 'partial' | 'unresolved' | 'event';
  formula?: string;
  specials?: string[];
  kv?: string[];
  reason?: string[];
}

interface NativeFunction extends NativeValue {
  function: string;
  handler?: string;
  // client.dll's handler when its result differs from server.dll's
  client?: NativeValue;
  // declared by one DLL only
  side?: 'server' | 'client';
}

interface NativeModifier {
  class: string;
  bases: string[];
  functions: NativeFunction[];
  fields?: Record<string, { in: string; value: string }[]>;
  // CheckState: true / false the modifier sets the state to (null: not followed), `when` its condition
  states?: { state: string; value: boolean | null; when?: string }[];
  // it overrides CheckState, but builds the masks from data the analysis cannot read (KV, fields)
  states_unresolved?: boolean;
  ability?: string;
  abilities?: string[];
  // the modifier exists in one DLL only
  side?: 'server' | 'client';
}

if (!existsSync(inputPath)) {
  console.log(`No ${inputPath} — skipping native modifiers.`);
  process.exit(0);
}

const input: { version: string | null; modifiers: Record<string, NativeModifier> } = JSON.parse(
  readFileSync(inputPath, 'utf8'),
);

// --- the dump this build is made from: version and modifierfunction enum
const dump = existsSync(dumpPath) ? readFileSync(dumpPath, 'utf8') : '';
const dumpVersion = dump.match(/ClientVersion=(\d+)/)?.[1];
if (input.version && dumpVersion && input.version !== dumpVersion) {
  console.warn(
    `! ${inputPath} was read from server.dll of build ${input.version}, the dump is build ${dumpVersion}: ` +
      'run `npm run auto-dump` for the installed build, or bring in the dump of that build.',
  );
}
const enumBody = dump.match(/declare enum modifierfunction\s*\r?\n\{([\s\S]*?)\r?\n\}/)?.[1] ?? '';
const enumMembers = new Set([...enumBody.matchAll(/^\s*(MODIFIER_\w+)\s*=/gm)].map((m) => m[1]));
if (enumMembers.size > 0) {
  const unknown = new Set<string>();
  for (const modifier of Object.values(input.modifiers)) {
    for (const f of modifier.functions) if (!enumMembers.has(f.function)) unknown.add(f.function);
  }
  if (unknown.size > 0) {
    console.warn(
      `! Modifier functions not in the dump's modifierfunction enum: ${[...unknown].join(', ')}`,
    );
  }
}

// --- client.dll
// the formula (the status when there is none: events, unresolved; a path the executor gave up on can make
// the same formula `partial` on one side only); field offsets differ between the DLLs, so the fields are
// numbered in order of appearance
function comparable(v: NativeValue): string {
  if (v.formula === undefined) return v.status;
  const fields = new Map<string, string>();
  return v.formula.replace(/self[.]field_[0-9a-f]+/g, (f) => {
    if (!fields.has(f)) fields.set(f, `self.field#${fields.size}`);
    return fields.get(f)!;
  });
}

function clientValue(f: NativeFunction): NativeValue {
  const { function: _f, handler: _h, client: _c, side: _s, ...value } = f;
  return value;
}

if (existsSync(clientPath)) {
  const client: { version: string | null; modifiers: Record<string, NativeModifier> } = JSON.parse(
    readFileSync(clientPath, 'utf8'),
  );
  if (client.version !== input.version) {
    console.warn(
      `! ${clientPath} is from client.dll of build ${client.version}, ${inputPath} from server.dll of ` +
        `build ${input.version}: run \`npm run dump:native-modifiers\` again.`,
    );
  }
  let differ = 0;
  for (const [name, modifier] of Object.entries(input.modifiers)) {
    const other = client.modifiers[name];
    if (!other) {
      modifier.side = 'server';
      continue;
    }
    const theirs = new Map(other.functions.map((f) => [f.function, f]));
    for (const f of modifier.functions) {
      const c = theirs.get(f.function);
      theirs.delete(f.function);
      if (!c) f.side = 'server';
      else if (comparable(c) !== comparable(f)) {
        f.client = clientValue(c);
        differ += 1;
      }
    }
    for (const c of theirs.values()) modifier.functions.push({ ...c, side: 'client' });
  }
  for (const [name, modifier] of Object.entries(client.modifiers)) {
    // CheckState and fields stay the server's: of a client-only modifier only its functions
    const { class: cls, bases, functions } = modifier;
    if (!input.modifiers[name]) input.modifiers[name] = { class: cls, bases, functions, side: 'client' };
  }
  input.modifiers = Object.fromEntries(
    Object.entries(input.modifiers).sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0)),
  );
  console.log(`client.dll: ${differ} functions with a different result`);
} else {
  console.warn(`! No ${clientPath} — native modifiers without the client's formulas.`);
}

// --- abilities whose values the formulas read
const valuesOf = new Map<string, Set<string>>(); // special value name -> abilities that define it
if (existsSync(abilitiesPath)) {
  const abilities: Record<string, any> = JSON.parse(readFileSync(abilitiesPath, 'utf8'));
  for (const [ability, kv] of Object.entries(abilities)) {
    const names = new Set<string>();
    if (kv && typeof kv.AbilityValues === 'object')
      Object.keys(kv.AbilityValues).forEach((k) => names.add(k));
    if (kv && typeof kv.AbilitySpecial === 'object') {
      for (const entry of Object.values<any>(kv.AbilitySpecial)) {
        if (entry && typeof entry === 'object') Object.keys(entry).forEach((k) => names.add(k));
      }
    }
    for (const name of names) {
      if (!valuesOf.has(name)) valuesOf.set(name, new Set());
      valuesOf.get(name)!.add(ability);
    }
  }
} else {
  console.warn(
    `! ${abilitiesPath} not found — run build:abilities first to link modifiers to abilities`,
  );
}

function linkAbility(name: string, modifier: NativeModifier) {
  const specials = new Set(
    modifier.functions.flatMap((f) => [...(f.specials ?? []), ...(f.client?.specials ?? [])]),
  );
  if (specials.size === 0 || valuesOf.size === 0) return;
  let candidates: Set<string> | undefined;
  for (const special of specials) {
    const holders = valuesOf.get(special) ?? new Set<string>();
    candidates = candidates
      ? new Set([...candidates].filter((a) => holders.has(a)))
      : new Set(holders);
  }
  if (!candidates || candidates.size === 0) return;
  let list = [...candidates];
  if (list.length > 1) {
    // several abilities define all of these values: prefer the one the modifier is named after
    const body = name.replace(/^modifier_/, '');
    const named = list.filter((a) => body.startsWith(a) || body.includes(a.replace(/^item_/, '')));
    if (named.length > 0) {
      const longest = Math.max(...named.map((a) => a.length));
      list = named.filter((a) => a.length === longest);
    }
  }
  if (list.length === 1) modifier.ability = list[0];
  else modifier.abilities = list.sort().slice(0, 8);
}

const counts: Record<string, number> = {};
for (const [name, modifier] of Object.entries(input.modifiers)) {
  linkAbility(name, modifier);
  for (const f of modifier.functions) counts[f.status] = (counts[f.status] ?? 0) + 1;
}

mkdirSync(dirname(outputPath), { recursive: true });
writeFileSync(outputPath, `${JSON.stringify(input, null, 1)}\n`, 'utf8');
const summary = Object.entries(counts)
  .map(([status, n]) => `${n} ${status}`)
  .join(', ');
console.log(
  `Wrote ${Object.keys(input.modifiers).length} native modifiers (${summary}) → ${outputPath}`,
);
