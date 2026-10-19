import { findSteamAppById } from '@moddota/find-steam-app';
import fs from 'fs';
import path from 'path';

/**
 * Dota 2 installation root (the directory that contains `game/`). `DOTA2_DIR` wins, which is how
 * Linux servers with a steamcmd install (no Steam client, no libraryfolders.vdf) point at it.
 */
export async function findDota2Dir(): Promise<string> {
  const fromEnv = process.env.DOTA2_DIR;
  if (fromEnv) {
    if (!fs.existsSync(path.join(fromEnv, 'game', 'dota', 'gameinfo.gi'))) {
      throw new Error(`DOTA2_DIR=${fromEnv} does not look like a Dota 2 installation`);
    }
    return fromEnv;
  }

  const found = await findSteamAppById(570);
  if (!found) throw new Error('Could not locate a Dota 2 installation (set DOTA2_DIR)');
  return found;
}

/** The server module of whichever platform build is installed (Windows first on Windows). */
export function findServerBinary(dota2Dir: string): string {
  const bin = path.join(dota2Dir, 'game', 'dota', 'bin');
  const candidates = [
    path.join(bin, 'win64', 'server.dll'),
    path.join(bin, 'linuxsteamrt64', 'libserver.so'),
  ];
  if (process.platform !== 'win32') candidates.reverse();
  const found = candidates.find((x) => fs.existsSync(x));
  if (!found) throw new Error(`No server binary in ${bin}`);
  return found;
}
