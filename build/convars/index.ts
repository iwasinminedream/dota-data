import { outputJson, readDump } from '../util';

export async function generateConvars() {
  const dump = readDump('cvarlist');
  const lines = dump.split(/\r?\n/);

  const convars: Record<string, { default: string; flags: string[]; description: string }> = {};

  for (const line of lines) {
    if (
      !line.includes(':') ||
      line.startsWith('cvar list') ||
      line.startsWith('-----') ||
      line.match(/^\d+ convars\/concommands for/)
    )
      continue;

    const parts = line.split(' : ');
    if (parts.length < 3) continue;

    const name = parts[0].trim();
    const value = parts[1].trim();

    const flagsPart = parts[2].trim();
    const desc = parts.slice(3).join(' : ').trim();

    const flags = flagsPart
      .split(',')
      .map((f) => f.trim().replace(/^"|"$/g, ''))
      .filter((f) => f);

    convars[name] = {
      default: value,
      flags,
      description: desc,
    };
  }

  outputJson('convars', convars);
}
