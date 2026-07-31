/*
 * modifier_test_properties.lua keeps the previous dump's HasFunction state so the
 * in-game test can report what changed. That state is rewritten from every
 * successful dump, so the dumper never drifts out of sync with the game by hand.
 */
import * as fs from 'fs';

export const MODIFIER_TEST_LUA = 'dumper/modifier_test_properties.lua';
export const MODIFIER_TEST_OUTPUT = 'dumper/modifier_test_output.txt';

const BASELINE_START = '-- BASELINE START';
const BASELINE_END = '-- BASELINE END';

export interface BaselineSync {
  total: number;
  added: string[];
  removed: string[];
}

function readModifierNames(text: string): string[] {
  return [...text.matchAll(/\["(MODIFIER_\w+)"\]/g)].map((match) => match[1]);
}

/**
 * Rewrites the baseline in the test modifier from a captured dump and reports how
 * the modifier function list changed. Returns null when the capture is unusable,
 * in which case the baseline is left as it was.
 */
export function syncModifierBaseline(
  luaPath = MODIFIER_TEST_LUA,
  outputPath = MODIFIER_TEST_OUTPUT,
): BaselineSync | null {
  if (!fs.existsSync(outputPath)) return null;

  const output = fs.readFileSync(outputPath, 'utf8');
  const stateBlock = output.match(/local previous_state = \{[\s\S]*?\r?\n\}/)?.[0];
  if (!stateBlock) {
    console.warn('Modifier test produced no state — baseline left untouched.');
    return null;
  }

  const lua = fs.readFileSync(luaPath, 'utf8');
  const start = lua.indexOf(BASELINE_START);
  const end = lua.indexOf(BASELINE_END);
  if (start === -1 || end === -1 || end < start) {
    console.warn(`Could not find the baseline markers in ${luaPath} — not updating it.`);
    return null;
  }

  const previous = readModifierNames(lua.slice(start, end));
  const current = readModifierNames(stateBlock);
  // A truncated capture (the test output is streamed from the game console) must
  // not be allowed to wipe the baseline it is compared against.
  if (previous.length > 0 && current.length < previous.length * 0.9) {
    console.warn(
      `Modifier test output looks truncated (${current.length} of ~${previous.length} functions) — baseline left untouched.`,
    );
    return null;
  }

  const previousSet = new Set(previous);
  const currentSet = new Set(current);
  const added = current.filter((name) => !previousSet.has(name));
  const removed = previous.filter((name) => !currentSet.has(name));

  const newline = lua.includes('\r\n') ? '\r\n' : '\n';
  const body = stateBlock.replace(/\r?\n/g, newline);
  fs.writeFileSync(
    luaPath,
    `${lua.slice(0, start)}${BASELINE_START}${newline}${body}${newline}${lua.slice(end)}`,
    'utf8',
  );

  return { total: current.length, added, removed };
}

/**
 * The modifier function enum changes between Dota builds, and the dump log is long,
 * so the update is reported at the very end where it cannot be missed.
 */
export function reportBaselineChange(baseline: BaselineSync | null): void {
  if (baseline == null || (baseline.added.length === 0 && baseline.removed.length === 0)) return;

  const separator = '='.repeat(78);
  console.log(`\n${separator}`);
  console.log('THE MODIFIER FUNCTION LIST CHANGED IN THIS DOTA BUILD — THE DUMPER WAS UPDATED');
  if (baseline.added.length > 0) {
    console.log(`  + ${baseline.added.length} new: ${baseline.added.join(', ')}`);
  }
  if (baseline.removed.length > 0) {
    console.log(`  - ${baseline.removed.length} removed: ${baseline.removed.join(', ')}`);
  }
  console.log(
    `  ${MODIFIER_TEST_LUA} now holds the state of this dump (${baseline.total} functions).`,
  );
  console.log('  REPEAT THE DUMP: run `npm run auto-dump` again with the updated dumper.');
  console.log(`${separator}\n`);
}
