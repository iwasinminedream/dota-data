/*
 * Utility script that automatically starts dota with the dumper addon.
 * npm run start:dumper
 */
import { execSync, spawn } from 'child_process';
import * as fs from 'fs';
import { Socket } from 'net';
import * as path from 'path';

import { findSteamAppById } from '@moddota/find-steam-app';
import { reportBaselineChange, syncModifierBaseline } from './modifier-baseline.mts';
import * as vConsole from './vconsole.mts';

const ADDON_NAME = 'dumper';

const dota2Dir = await findSteamAppById(570);

if (!dota2Dir) {
  throw 'Could not locate a dota 2 installation';
} else {
  console.log(`Found DotA 2 installation: ${dota2Dir}`);
}

console.log('Copying dumper addon...');

const addonPath = path.join(dota2Dir, 'game', 'dota_addons', ADDON_NAME);
if (!fs.existsSync(addonPath)) {
  fs.mkdirSync(addonPath);
}

const vscriptsPath = path.join(addonPath, 'scripts', 'vscripts');
if (!fs.existsSync(vscriptsPath)) {
  fs.mkdirSync(vscriptsPath, { recursive: true });
}
fs.copyFileSync(
  path.join('dumper', 'addon_game_mode.lua'),
  path.join(vscriptsPath, 'addon_game_mode.lua'),
);
fs.copyFileSync(path.join('dumper', 'addon_init.lua'), path.join(vscriptsPath, 'addon_init.lua'));

const modifiersPath = path.join(vscriptsPath, 'modifiers');
if (!fs.existsSync(modifiersPath)) {
  fs.mkdirSync(modifiersPath, { recursive: true });
}
fs.copyFileSync(
  path.join('dumper', 'modifier_test_properties.lua'),
  path.join(vscriptsPath, 'modifier_test_properties.lua'),
);

// Custom-game UI that instantiates known panel types, so their JS classes are
// registered by the time the panel declarations phase runs (the engine only
// has cl_panorama_typescript_declarations data for instantiated types).
const contentPanoramaPath = path.join(
  dota2Dir,
  'content',
  'dota_addons',
  ADDON_NAME,
  'panorama',
);
const contentLayoutPath = path.join(contentPanoramaPath, 'layout', 'custom_game');
const contentScriptsPath = path.join(contentPanoramaPath, 'scripts', 'custom_game');
fs.mkdirSync(contentLayoutPath, { recursive: true });
fs.mkdirSync(contentScriptsPath, { recursive: true });
for (const layoutFile of ['custom_ui_manifest.xml', 'dumper_panels.xml']) {
  fs.copyFileSync(
    path.join('dumper', 'panorama', layoutFile),
    path.join(contentLayoutPath, layoutFile),
  );
}
fs.copyFileSync(
  path.join('dumper', 'panorama', 'dumper_panels.js'),
  path.join(contentScriptsPath, 'dumper_panels.js'),
);

// The -tools launch does not compile the custom UI on its own, so compile it
// explicitly (compiling the manifest also compiles the layout and script it
// references). If this fails, the dump still works — the panel phase just
// captures fewer per-type interfaces.
try {
  execSync(
    `"${path.join(dota2Dir, 'game', 'bin', 'win64', 'resourcecompiler.exe')}" -i "${path.join(
      contentLayoutPath,
      'custom_ui_manifest.xml',
    )}"`,
    { stdio: 'ignore' },
  );
  console.log('Compiled dumper custom-game UI.');
} catch (err) {
  console.warn('Failed to compile the dumper custom-game UI:', err);
}

console.log('Starting dumper...');

const dotaBinDir = path.join(dota2Dir, 'game', 'bin', 'win64');
const dotaExe = path.join(dotaBinDir, 'dota2.exe');
const args = [
  '-novid',
  '-tools',
  '-addon',
  ADDON_NAME,
  `+dota_launch_custom_game ${ADDON_NAME} dota`,
];

const steamInfPath = path.join(dota2Dir, 'game', 'dota', 'steam.inf');
const steamInfContent = fs.readFileSync(steamInfPath);

// --- Tunables -------------------------------------------------------------
const CONNECT_PORT = 29000;
const STARTUP_DELAY_MS = 5000; // give Dota a moment before connecting to vConsole
const DUMP_TIMEOUT_MS = 8 * 60 * 1000; // hard cap from connect to the end of all phases
const INACTIVITY_TIMEOUT_MS = 120 * 1000; // no console output this long => Dota frozen
// (must exceed the gap between connecting and the match reaching GAME_IN_PROGRESS,
// when the dump fires — otherwise a slow load looks like a freeze)
const MODIFIER_GRACE_MS = 45 * 1000; // after the dump, wait this long for the modifier test
// (the modifier test is currently disabled in addon_game_mode.lua, so this is
// just the upper bound the dumper waits before finishing on the dump alone)
const PANELS_INACTIVITY_MS = 60 * 1000; // no output during the panel phase => keep partial capture
const HEARTBEAT_MS = 10 * 1000;
const MAX_ATTEMPTS = 3;

// The script_reload relay disruption can silently drop a whole section from the
// capture (the sacrificial cvarlist usually absorbs it, but not always), so a
// "successful" attempt still has to prove every expected section actually landed.
const REQUIRED_SECTIONS = [
  'script_reload',
  'cl_script_reload',
  'dump_panorama_css_properties',
  'dump_panorama_events',
  'cl_panorama_script_help *',
  'cl_dump_modifier_list',
  'panorama_generate_layout_xsd',
  'cvarlist',
  'cl_panorama_typescript_declarations',
  'panorama_panels',
];

function findMissingSections(): string[] {
  const content = fs.readFileSync('dumper/dump', 'utf8');
  return REQUIRED_SECTIONS.filter((section) => !content.includes(`$> ${section}`));
}

let succeeded = false;
for (let attempt = 1; attempt <= MAX_ATTEMPTS && !succeeded; attempt++) {
  console.log(`\n=== Dump attempt ${attempt}/${MAX_ATTEMPTS} ===`);
  succeeded = await runAttempt();
  if (succeeded) {
    const missing = findMissingSections();
    if (missing.length > 0) {
      console.warn(`Dump is missing sections: ${missing.join(', ')}`);
      succeeded = false;
    }
  }
  if (!succeeded && attempt < MAX_ATTEMPTS) {
    console.warn('Attempt did not produce a complete dump — retrying with a fresh Dota launch...');
    await delay(3000);
  }
}

if (!succeeded) {
  console.error(`Failed to capture a complete dump after ${MAX_ATTEMPTS} attempts.`);
  process.exit(1);
}

console.log('\nSaved dump + modifier test — dumper finished successfully.');

// Fold this dump's modifier state back into the dumper, and say so at the very end
// if the modifier function list itself changed in this Dota build.
reportBaselineChange(syncModifierBaseline());

process.exit(0);

// --------------------------------------------------------------------------

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function streamEnd(stream: fs.WriteStream): Promise<void> {
  return new Promise((resolve) => stream.end(() => resolve()));
}

async function runAttempt(): Promise<boolean> {
  const attemptStartTime = Date.now();
  const dumpWriteStream = fs.createWriteStream('dumper/dump');
  dumpWriteStream.write(steamInfContent);
  const modifierWriteStream = fs.createWriteStream('dumper/modifier_test_output.txt');

  console.log('Spawning Dota:', dotaExe, args.join(' '));
  const p1 = spawn(dotaExe, args, { cwd: dotaBinDir });

  let dotaExited = false;
  p1.on('error', (err) => console.error('Failed to spawn dota2.exe:', err));
  p1.on('exit', (code, signal) => {
    dotaExited = true;
    console.log(`dota2.exe exited with code=${code} signal=${signal}`);
  });

  const killDota = () => {
    if (dotaExited) return;
    // In -tools mode Dota spawns child processes; kill the whole tree so a
    // frozen instance can't linger and hold the vConsole port for the retry.
    try {
      if (p1.pid) spawn('taskkill', ['/F', '/T', '/PID', String(p1.pid)]);
    } catch {}
    try {
      p1.kill();
    } catch {}
  };

  try {
    await delay(STARTUP_DELAY_MS);

    let dotaConsole: Socket;
    try {
      dotaConsole = await vConsole.connect(CONNECT_PORT);
    } catch (err) {
      console.error('Could not connect to vConsole after launching Dota:', err);
      return false;
    }

    console.log('Connected! Waiting for dump...');

    let ok = false;
    try {
      ok = await readDump(
        dotaConsole,
        dumpWriteStream,
        modifierWriteStream,
        () => dotaExited,
        attemptStartTime,
      );
    } catch (err) {
      console.error('Error while reading dump:', err);
      ok = false;
    }

    try {
      await vConsole.disconnect(dotaConsole);
    } catch {}

    return ok;
  } finally {
    await streamEnd(dumpWriteStream);
    await streamEnd(modifierWriteStream);
    killDota();
  }
}

// The panel declarations phase is driven from here (not from the addon SCRIPT)
// because the list of panel types is only known after the dump has produced the
// layout XSD — we parse it, then ask Dota for per-type TypeScript declarations.
interface PanelAttribute {
  name: string;
  description?: string;
}

interface PanelInfo {
  name: string;
  base?: string;
  attributes: PanelAttribute[];
}

function decodeXmlEntities(text: string): string {
  return text
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/&amp;/g, '&');
}

// The XSD lists every panel type as a complexType with all attributes flattened
// down the inheritance chain; each attribute's documentation records the class
// that declared it ("(from X)") and the type header records the parent
// ("derived from X"). Keeping only the attributes declared by the type itself
// loses nothing — the full set is rebuilt by walking `base`.
function parseLayoutXsd(xsd: string): PanelInfo[] {
  const panels: PanelInfo[] = [];
  const blocks = xsd.split(/(?=<xs:complexType name=")/).slice(1);
  for (const block of blocks) {
    const typeMatch = block.match(/^<xs:complexType name="([\w.-]+)Type"/);
    if (!typeMatch) continue;
    const header = block.match(/&lt;b&gt;([\w.-]+)&lt;\/b&gt;(?: \(derived from ([\w.-]+)\))?/);
    const name = header?.[1] ?? typeMatch[1];
    if (name.startsWith('Internal_')) continue;

    const attributes: PanelAttribute[] = [];
    const seen = new Set<string>();
    for (const attr of block.matchAll(
      /<xs:attribute name="([\w.-]+)"[^>]*>\s*<xs:annotation><xs:documentation[^>]*>&lt;b&gt;[\w.-]+&lt;\/b&gt; \(from ([\w.-]+)\)&lt;br \/&gt;&lt;br \/&gt;([^<]*)</g,
    )) {
      const [, attrName, from, rawDescription] = attr;
      if (from !== name || seen.has(attrName)) continue;
      seen.add(attrName);
      const description = decodeXmlEntities(rawDescription.trim());
      attributes.push(description ? { name: attrName, description } : { name: attrName });
    }
    attributes.sort((a, b) => (a.name < b.name ? -1 : 1));

    const base = header?.[2];
    panels.push(base ? { name, base, attributes } : { name, attributes });
  }
  panels.sort((a, b) => (a.name < b.name ? -1 : 1));
  return panels;
}

// panorama_generate_layout_xsd prints "Layout XSD contents copied to clipboard."
// — the schema itself never reaches the console, so read it back via PowerShell.
function readClipboardXsd(): string | null {
  try {
    const clip = execSync('powershell -NoProfile -Command "Get-Clipboard -Raw"', {
      maxBuffer: 256 * 1024 * 1024,
    }).toString('utf8');
    return clip.includes('<xs:schema') ? clip : null;
  } catch {
    return null;
  }
}

// Split captured `cl_panorama_typescript_declarations <type>` output into
// interface blocks. Tolerates unrelated console lines between blocks.
function extractInterfaces(text: string): Map<string, string[]> {
  const result = new Map<string, string[]>();
  const lines = text.split(/\r?\n/);
  for (let i = 0; i < lines.length; i++) {
    const match = lines[i].match(/^interface ([\w$]+)$/);
    if (!match || lines[i + 1]?.trim() !== '{') continue;
    const body: string[] = [];
    let j = i + 2;
    while (j < lines.length && lines[j].trim() !== '}') {
      body.push(lines[j].trim());
      j++;
    }
    result.set(match[1], body);
    i = j;
  }
  return result;
}

// panorama_generate_layout_xsd may write its result to disk instead of the
// console; pick up any .xsd created after this attempt started.
function findFreshXsdFile(attemptStartTime: number): string | null {
  const found: { file: string; mtime: number }[] = [];
  const walk = (dir: string) => {
    let entries: fs.Dirent[];
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const entry of entries) {
      const entryPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(entryPath);
      } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.xsd')) {
        try {
          const stat = fs.statSync(entryPath);
          if (stat.mtimeMs >= attemptStartTime) found.push({ file: entryPath, mtime: stat.mtimeMs });
        } catch {}
      }
    }
  };
  walk(path.join(dota2Dir!, 'game'));
  walk(path.join(dota2Dir!, 'content'));
  found.sort((a, b) => b.mtime - a.mtime);
  return found.length > 0 ? found[0].file : null;
}

async function readDump(
  dota: Socket,
  dumpStream: fs.WriteStream,
  modifierStream: fs.WriteStream,
  isDotaExited: () => boolean,
  attemptStartTime: number,
): Promise<boolean> {
  return new Promise((resolve) => {
    let dumpReading = false;
    let dumpDone = false;
    let modifierReading = false;
    let modifierDone = false;
    let settled = false;
    let sawAnyMessage = false;
    let messageCount = 0;
    let lastActivity = Date.now();
    let modifierGraceTimer: ReturnType<typeof setTimeout> | null = null;
    let currentSection: string | null = null;
    let xsdText = '';
    let panelsStarted = false;
    let panelsCapturing = false;
    let panelsDone = false;
    let panelData: PanelInfo[] = [];
    const panelsBuffer: string[] = [];

    // Optional raw capture of every console message (set DUMP_DEBUG=1) for
    // diagnosing what Dota actually prints and in what order.
    const rawStream = process.env.DUMP_DEBUG ? fs.createWriteStream('dumper/console-raw.log') : null;

    const overall = setTimeout(() => {
      console.warn('Timed out waiting for the dump to complete.');
      if (dumpDone && panelsStarted && !panelsDone) {
        finishPanels();
      } else {
        settle(dumpDone);
      }
    }, DUMP_TIMEOUT_MS);

    const watchdog = setInterval(() => {
      if (isDotaExited()) {
        if (!dumpDone) {
          console.warn('Dota exited before the dump completed.');
          settle(false);
        } else {
          console.warn('Dota exited before the panel phase completed — keeping what was captured.');
          finishPanels();
          settle(true);
        }
        return;
      }

      const idleFor = Date.now() - lastActivity;
      if (panelsStarted && !panelsDone) {
        if (idleFor > PANELS_INACTIVITY_MS) {
          console.warn('Panel declarations phase stalled — keeping what was captured.');
          finishPanels();
        }
        return;
      }
      if (idleFor > INACTIVITY_TIMEOUT_MS) {
        if (dumpDone) {
          console.warn('No further output after the dump — continuing without the modifier test.');
          void startPanelsPhase();
        } else if (!sawAnyMessage) {
          console.warn('No console output at all — Dota appears frozen during load.');
          settle(false);
        } else {
          console.warn('Console output stalled before the dump completed — Dota appears frozen.');
          settle(false);
        }
      }
    }, 5000);

    const heartbeat = setInterval(() => {
      const stage = panelsStarted
        ? 'capturing panel declarations'
        : dumpDone
        ? 'waiting for modifier test'
        : 'capturing dump';
      console.log(
        `  …${stage}: ${messageCount} msgs, dump ${(dumpStream.bytesWritten / 1024).toFixed(0)} KB`,
      );
    }, HEARTBEAT_MS);

    function settle(ok: boolean) {
      if (settled) return;
      settled = true;
      clearTimeout(overall);
      clearInterval(watchdog);
      clearInterval(heartbeat);
      if (modifierGraceTimer) clearTimeout(modifierGraceTimer);
      if (rawStream) rawStream.end();
      resolve(ok);
    }

    function checkDone() {
      if (dumpDone && modifierDone) {
        console.log('Dump + modifier test complete.');
        void startPanelsPhase();
      }
    }

    async function startPanelsPhase() {
      if (panelsStarted || settled) return;
      panelsStarted = true;
      if (modifierGraceTimer) clearTimeout(modifierGraceTimer);

      try {
        let xsd = xsdText.includes('<xs:schema') ? xsdText : null;
        if (!xsd) xsd = readClipboardXsd();
        if (!xsd) {
          const xsdFile = findFreshXsdFile(attemptStartTime);
          if (xsdFile) {
            console.log(`Found generated layout XSD on disk: ${xsdFile}`);
            xsd = fs.readFileSync(xsdFile, 'utf8');
          }
        }

        panelData = xsd ? parseLayoutXsd(xsd) : [];
        if (panelData.length === 0) {
          console.warn('Could not obtain the layout XSD — skipping the panel phase.');
          settle(true);
          return;
        }

        // The raw XSD is ~22 MB of boilerplate (every type repeats all inherited
        // attributes), so the dump stores this compact digest instead.
        dumpStream.write(`\n$> panorama_panels\n${JSON.stringify(panelData, null, 2)}\n`);

        console.log(`Found ${panelData.length} panel types, dumping TypeScript declarations...`);
        panelsCapturing = true;
        lastActivity = Date.now();
        for (const [index, panel] of panelData.entries()) {
          await vConsole.execute(dota, `cl_panorama_typescript_declarations ${panel.name}`);
          // Give the console queue room to drain between bursts.
          if (index % 50 === 49) await delay(50);
        }
        await vConsole.execute(dota, 'echoln ===ENDOFPANELS');
      } catch (err) {
        console.warn('Panel declarations phase failed:', err);
        settle(dumpDone);
      }
    }

    function finishPanels() {
      if (panelsDone || settled) return;
      panelsDone = true;

      const captured = extractInterfaces(panelsBuffer.join(''));
      const baseOf = new Map(panelData.map((p) => [p.name, p.base]));
      const kept: string[] = [];
      let droppedCount = 0;
      for (const [name, body] of captured) {
        // A type whose flattened JS interface is identical to its nearest captured
        // ancestor's adds nothing — its script API is fully inherited.
        let ancestor = baseOf.get(name);
        while (ancestor && !captured.has(ancestor)) ancestor = baseOf.get(ancestor);
        if (ancestor && captured.get(ancestor)!.join('\n') === body.join('\n')) {
          droppedCount++;
          continue;
        }
        kept.push(`interface ${name}\n{\n${body.map((line) => `    ${line}`).join('\n')}\n}`);
      }

      if (kept.length > 0) {
        dumpStream.write(`\n$> panel_typescript_declarations\n${kept.join('\n')}\n`);
      }
      console.log(
        `Panel declarations captured: ${kept.length} unique interfaces (${droppedCount} fully inherited).`,
      );
      settle(true);
    }

    vConsole.onMessage(dota, (type, _channel, message) => {
      if (type !== 'PRNT') return;
      sawAnyMessage = true;
      messageCount++;
      lastActivity = Date.now();
      if (rawStream) rawStream.write(message);

      // Panel declarations capture (phase 2, after dump + modifier test)
      if (panelsCapturing && !panelsDone) {
        if (message.startsWith('===ENDOFPANELS')) {
          finishPanels();
        } else {
          panelsBuffer.push(message);
        }
        return;
      }

      // Dump capture
      if (!dumpDone) {
        if (message.startsWith('$>')) {
          dumpReading = true;
          currentSection = message.slice(2).trim();
        }
        if (message.startsWith('===ENDOFDUMP')) {
          dumpReading = false;
          dumpDone = true;
          console.log('Dump completed. Waiting for modifier test...');
          // The modifier test only runs once the game reaches GAME_IN_PROGRESS,
          // which can fail independently of the dump. Don't let it block forever:
          // proceed with the (essential) dump after a grace period.
          modifierGraceTimer = setTimeout(() => {
            if (!modifierDone) {
              console.warn('Modifier test did not finish in time — continuing without it.');
              modifierDone = true;
              void startPanelsPhase();
            }
          }, MODIFIER_GRACE_MS);
          checkDone();
        } else if (dumpReading) {
          dumpStream.write(message);
          if (currentSection === 'panorama_generate_layout_xsd') {
            xsdText += message;
          }
        }
      }

      // Modifier test capture
      if (message.startsWith('local previous_state')) {
        modifierReading = true;
      }
      if (message.startsWith('===ENDOFMODIFIERTEST')) {
        modifierReading = false;
        modifierDone = true;
        console.log('Modifier test completed.');
        checkDone();
      } else if (modifierReading) {
        modifierStream.write(message);
      }
    });
  });
}
