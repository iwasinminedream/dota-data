/*
 * Native modifiers: the modifier functions every native (C++) modifier implements and the formulas of
 * its properties, read offline from server.dll by dumper/native-modifiers/extract.py (Python 3 +
 * capstone, see dumper/native-modifiers/README.md) into dumper/native_modifiers.json.
 *
 * Runs at the end of every successful `npm run auto-dump`, or alone: `npm run dump:native-modifiers`.
 * Needs the Windows server.dll (`DOTA_SERVER_BINARY` points at it on Linux, as for build/engine-enums);
 * with only libserver.so, or without Python / capstone, the previous file is kept and a warning printed.
 */
import { spawnSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

// CommonJS module (build/ is not ESM): named imports are not visible from .mts.
import dotaDir from '../build/util/dota-dir';

const OUTPUT = path.join('dumper', 'native_modifiers.json');
const PARTIAL = `${OUTPUT}.partial`;
const SCRIPT = path.join('dumper', 'native-modifiers', 'extract.py');

function pythonCommands(): string[][] {
  if (process.env.DUMPER_PYTHON) return [[process.env.DUMPER_PYTHON]];
  return process.platform === 'win32'
    ? [['python'], ['py', '-3'], ['python3']]
    : [['python3'], ['python']];
}

/** Returns true when dumper/native_modifiers.json was rewritten. */
export function extractNativeModifiers(dota2Dir: string, version?: string): boolean {
  let binary: string;
  try {
    binary = dotaDir.findServerBinary(dota2Dir);
  } catch (error) {
    console.warn(`Native modifiers skipped: ${(error as Error).message}`);
    return false;
  }
  if (!binary.toLowerCase().endsWith('.dll')) {
    console.warn(
      `Native modifiers skipped: the analysis reads the Windows server.dll, found ${binary} ` +
        `(set DOTA_SERVER_BINARY). ${OUTPUT} was kept.`,
    );
    return false;
  }

  const args = [SCRIPT, '--dll', binary, '--out', PARTIAL];
  if (version) args.push('--version', version);
  for (const [command, ...prefix] of pythonCommands()) {
    console.log(`Native modifiers: ${command} ${[...prefix, ...args].join(' ')}`);
    const result = spawnSync(command, [...prefix, ...args], { stdio: 'inherit' });
    if (result.error && (result.error as NodeJS.ErrnoException).code === 'ENOENT') continue;
    if (result.status === 0 && fs.existsSync(PARTIAL)) {
      fs.renameSync(PARTIAL, OUTPUT);
      console.log(`Saved ${OUTPUT}`);
      return true;
    }
    fs.rmSync(PARTIAL, { force: true });
    console.warn(
      `Native modifiers failed (exit ${result.status}); ${OUTPUT} was kept. ` +
        'The analysis needs Python 3 with capstone 5 (pip install capstone).',
    );
    return false;
  }
  console.warn(
    `Native modifiers skipped: no Python 3 found (set DUMPER_PYTHON). ${OUTPUT} was kept.`,
  );
  return false;
}

/** ClientVersion of the installed game (the build its server.dll belongs to). */
export function installedVersion(dota2Dir: string): string | undefined {
  const inf = path.join(dota2Dir, 'game', 'dota', 'steam.inf');
  if (!fs.existsSync(inf)) return undefined;
  return fs.readFileSync(inf, 'utf8').match(/ClientVersion=(\d+)/)?.[1];
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const dota2Dir = await dotaDir.findDota2Dir();
  process.exit(extractNativeModifiers(dota2Dir, installedVersion(dota2Dir)) ? 0 : 1);
}
