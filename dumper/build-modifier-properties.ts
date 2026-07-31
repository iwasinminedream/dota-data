import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';

const inputPath = join('dumper', 'modifier_test_output.txt');
const dumpPath = join('dumper', 'dump');
const outputPath = join('files', 'vscripts', 'modifier_properties.json');

if (!existsSync(inputPath)) {
  console.log('No modifier_test_output.txt found — skipping modifier properties.');
  process.exit(0);
}

const content = readFileSync(inputPath, 'utf8');
const result: Record<string, boolean> = {};

for (const line of content.split(/\r?\n/)) {
  const match = line.match(/\["(MODIFIER_\w+)"\]\s*=\s*(true|false)/);
  if (match) {
    result[match[1]] = match[2] === 'true';
  }
}

const count = Object.keys(result).length;
if (count === 0) {
  console.warn('No modifier properties parsed from output.');
  process.exit(0);
}

// The test output is only meaningful for the exact modifierfunction enum of the
// dump it was captured with: the values are positional, so an enum member added in
// the middle shifts every result after it onto the name of its predecessor. Compare
// against the enum in the dump and refuse to overwrite known-good data when they
// disagree, instead of writing silently corrupted "broken" flags.
function readEnumMembers(): string[] | null {
  if (!existsSync(dumpPath)) return null;
  const dump = readFileSync(dumpPath, 'utf8');
  const body = dump.match(/declare enum modifierfunction\s*\r?\n\{([\s\S]*?)\r?\n\}/)?.[1];
  if (body == null) return null;

  const members = [...body.matchAll(/^\s*(MODIFIER_\w+)\s*=\s*\d+,?\s*$/gm)]
    .map((match) => match[1])
    // MODIFIER_FUNCTION_LAST / MODIFIER_FUNCTION_INVALID are sentinels, not functions.
    .filter((name) => /^MODIFIER_(PROPERTY|EVENT)_/.test(name));
  return members.length > 0 ? members : null;
}

const enumMembers = readEnumMembers();
if (enumMembers != null) {
  const tested = new Set(Object.keys(result));
  const missing = enumMembers.filter((name) => !tested.has(name));
  const unknown = [...tested].filter((name) => !enumMembers.includes(name));

  if (missing.length > 0 || unknown.length > 0) {
    const describe = (names: string[]) =>
      names.length > 5 ? `${names.slice(0, 5).join(', ')}, … (${names.length})` : names.join(', ');
    console.warn('='.repeat(78));
    console.warn('modifier_test_output.txt does not match the modifierfunction enum of the dump:');
    if (missing.length > 0) console.warn(`  not tested: ${describe(missing)}`);
    if (unknown.length > 0) console.warn(`  no longer in the enum: ${describe(unknown)}`);
    console.warn(`  ${outputPath} was NOT updated — its data would be shifted and wrong.`);
    console.warn('  REPEAT THE DUMP: run `npm run auto-dump` to capture the modifier test again.');
    console.warn('='.repeat(78));
    process.exit(0);
  }
}

mkdirSync(dirname(outputPath), { recursive: true });
writeFileSync(outputPath, JSON.stringify(result, null, 2), 'utf8');
console.log(`Wrote ${count} modifier properties → ${outputPath}`);
