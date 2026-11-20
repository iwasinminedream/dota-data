/*
 * Table keys: the keys server.dll reads from (and writes to) the Lua tables VScript functions take —
 * CreateIllusions' modifierKeys, ApplyDamage's options, the event tables of the Set*Filter callbacks… —
 * read offline by dumper/native-modifiers/table_keys.py (Python 3 + capstone, the same tooling as the
 * native modifiers) into dumper/table_keys.json. build/vscripts/table-keys.ts compares them with the
 * documented table types and adds the keys a type lacks to files/vscripts/api-types.json.
 *
 * Runs at the end of every successful `npm run auto-dump`, or alone: `npm run dump:table-keys`.
 * Needs the Windows server.dll (`DOTA_SERVER_BINARY`); with only libserver.so, without Python / capstone,
 * or when the analysis does not find the keys it always finds (it exits 3: a build it no longer
 * understands), the previous file is kept and a warning printed.
 */
import { spawnSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

// CommonJS module (build/ is not ESM): named imports are not visible from .mts.
import dotaDir from '../build/util/dota-dir';
import { installedVersion } from './native-modifiers.mts';

const OUTPUT = path.join('dumper', 'table_keys.json');
const SCRIPT = path.join('dumper', 'native-modifiers', 'table_keys.py');

function pythonCommands(): string[][] {
  if (process.env.DUMPER_PYTHON) return [[process.env.DUMPER_PYTHON]];
  return process.platform === 'win32'
    ? [['python'], ['py', '-3'], ['python3']]
    : [['python3'], ['python']];
}

/** Returns true when dumper/table_keys.json was rewritten. */
export function extractTableKeys(dota2Dir: string, version?: string): boolean {
  let binary: string;
  try {
    binary = dotaDir.findServerBinary(dota2Dir);
  } catch (error) {
    console.warn(`Table keys skipped: ${(error as Error).message}`);
    return false;
  }
  if (!binary.toLowerCase().endsWith('.dll')) {
    console.warn(
      `Table keys skipped: the analysis reads the Windows server.dll, found ${binary} ` +
        `(set DOTA_SERVER_BINARY). ${OUTPUT} was kept.`,
    );
    return false;
  }
  const partial = `${OUTPUT}.partial`;
  const args = [SCRIPT, '--dll', binary, '--out', partial];
  if (version) args.push('--version', version);
  for (const [command, ...prefix] of pythonCommands()) {
    console.log(`Table keys: ${command} ${[...prefix, ...args].join(' ')}`);
    const result = spawnSync(command, [...prefix, ...args], { stdio: 'inherit' });
    if (result.error && (result.error as NodeJS.ErrnoException).code === 'ENOENT') continue;
    if (result.status === 0 && fs.existsSync(partial)) {
      fs.renameSync(partial, OUTPUT);
      console.log(`Saved ${OUTPUT}`);
      return true;
    }
    fs.rmSync(partial, { force: true });
    console.warn(
      result.status === 3
        ? `Table keys: the analysis does not understand this build (see above); ${OUTPUT} was kept.`
        : `Table keys failed (exit ${result.status}); ${OUTPUT} was kept. ` +
            'The analysis needs Python 3 with capstone 5 (pip install capstone).',
    );
    return false;
  }
  console.warn(`Table keys skipped: no Python 3 found (set DUMPER_PYTHON). ${OUTPUT} was kept.`);
  return false;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const dota2Dir = await dotaDir.findDota2Dir();
  process.exit(extractTableKeys(dota2Dir, installedVersion(dota2Dir)) ? 0 : 1);
}
