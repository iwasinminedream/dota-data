/*
 * Helpers for running the Windows client under Wine (dumper/linux/wine-launch.sh).
 */
import { execFileSync, spawnSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const here = path.dirname(fileURLToPath(import.meta.url));

function buildGetclip(): string {
  const source = path.join(here, 'getclip.c');
  const output = path.join(here, '.build', 'getclip.exe');
  if (fs.existsSync(output) && fs.statSync(output).mtimeMs >= fs.statSync(source).mtimeMs) {
    return output;
  }
  fs.mkdirSync(path.dirname(output), { recursive: true });
  execFileSync('x86_64-w64-mingw32-gcc', ['-O2', '-o', output, source], { stdio: 'inherit' });
  return output;
}

/**
 * The Wine clipboard text (the layout XSD after panorama_generate_layout_xsd), read by a tiny
 * Windows program in the client's prefix; null when there is none.
 */
export function readWineClipboard(file: string): string | null {
  const result = spawnSync('wine', [buildGetclip(), `Z:${file.replace(/\//g, '\\')}`], {
    env: { ...process.env, WINEDEBUG: '-all' },
    timeout: 120_000,
  });
  if (result.status !== 0 || !fs.existsSync(file)) return null;
  return fs.readFileSync(file, 'utf8');
}

/** Ends every process of the client's Wine prefix (wineserver outlives a killed launcher). */
export function killWine(): void {
  spawnSync('wineserver', ['-k'], { env: process.env, timeout: 30_000 });
}
