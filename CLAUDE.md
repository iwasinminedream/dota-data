# Dota Data – Copilot Instructions

## Quick Start (Read This First)

**Architecture in one sentence**: An npm package (`@moddota/dota-data`) that parses raw Dota 2 dump files into structured JSON + TypeScript declarations consumed by the ModDota API site.

**Essential dev commands**:
- `npm run build` – full rebuild: clean → generate from dumps → compile TS → modifiers → convars → changelog
- `npm run build:static` – only regenerate JSON/d.ts from dumps (via `tsx build`)
- `npm run build:tsc` – compile `src/` → `lib/` (runtime helpers + schemas)
- `npm run dev` – watch mode: `build:static` + `tsc --watch` in parallel
- `npm test` – Jest tests
- `npm run auto-dump` – launches Dota 2 to capture new dump data (Windows `-tools`; on Linux the Windows client under Wine or the Linux client: see "Capturing on Linux")

**Critical conventions**:
- **Dump parsing**: Raw data comes from the monolithic `dumper/dump` file, split by `$> <section_name>` markers → parsed by `readDump(name)` in `build/util/index.ts`
- **Type exports**: Every `types.ts` uses `// EXPORT START` / `// EXPORT END` markers → `exportNamespacedRoot()` generates `.d.ts` namespace declarations
- **Extension data**: Hand-maintained type overrides in `build/vscripts/api/data/index.ts` (1200+ lines) – merge with dump data, don't replace
- **Output files**: Generated JSON + `.d.ts` go to `files/`, compiled TS helpers go to `lib/`

---

## Project Architecture

### Build Pipeline Overview

```
Dota 2 Installation
├── VPK files (game events, engine enums)
└── dumper/dump (monolithic text file with $> section markers)
    ├── script_reload / cl_script_reload  → VScript API
    ├── cvarlist                          → Console variables
    ├── cl_panorama_typescript_declarations → Panorama JS API
    ├── dump_panorama_css_properties      → Panorama CSS
    ├── cl_panorama_script_help *         → Panorama Enums
    ├── dump_panorama_events             → Panorama Events
    ├── panorama_panels                  → Panorama Panels (digest of panorama_generate_layout_xsd:
    │                                      panel type → base type + own XML attributes; the raw XSD
    │                                      lands on the clipboard, the dumper reads it back and
    │                                      writes this compact JSON section instead)
    └── panel_typescript_declarations    → per-panel-type JS interfaces (dumper phase 2: panel type
                                           names come from the XSD; interfaces identical to their
                                           base type are omitted)
         ↓ (build/index.ts orchestrates all generators)
files/ (generated JSON + .d.ts)
         ↓ (tsc compiles src/ → lib/)
lib/ (runtime helpers, schemas, localization)
         ↓ (npm publish)
@moddota/dota-data package
```

### Folder Structure

```
dota-data/
├── build/                      # Build-time generators (run via tsx)
│   ├── index.ts                # Main orchestrator: calls all generators + validators
│   ├── util/
│   │   ├── index.ts            # readDump(), outputFile(), outputJson()
│   │   ├── normalization.ts    # formatArgumentName(), formatDescription(), clearDescription()
│   │   └── export-types.ts     # exportNamespacedRoot() – generates .d.ts from markers
│   ├── events/
│   │   ├── index.ts            # generateEvents() – parses VPK gameevents
│   │   └── types.ts            # Event, EventField types
│   ├── vscripts/
│   │   ├── index.ts            # generateVScripts() entry
│   │   ├── dump.ts             # parseDump() – JSON parse of script_reload dumps
│   │   ├── validation.ts       # isCompatibleOverride(), checkTypes()
│   │   ├── api/
│   │   │   ├── index.ts        # joinMethods(), transformFunction(), apiDeclarations()
│   │   │   ├── types.ts        # Declaration, ClassDeclaration, FunctionDeclaration types
│   │   │   └── data/           # Hand-maintained extension data (1217 lines!)
│   │   │       ├── index.ts    # classExtensions, functionExtensions, extraDeclarations
│   │   │       ├── modifier-properties.ts
│   │   │       ├── moddota-dump.ts
│   │   │       └── utils.ts
│   │   ├── api-types/
│   │   │   └── index.ts        # Primitive types, nominal types, object types
│   │   └── enums/
│   │       └── index.ts        # Enum extraction from constants
│   ├── panorama/
│   │   ├── index.ts            # generatePanorama() → generates api, css, enums, events
│   │   ├── api/
│   │   │   ├── index.ts        # generatePanoramaApi() – parses TS interface declarations
│   │   │   └── types.ts        # PanoramaApiInterface, PanoramaApiFunction
│   │   ├── css/
│   │   │   └── index.ts        # generateCss() – parses CSS property dump
│   │   ├── enums/
│   │   │   └── index.ts        # Parses 'declare enum' blocks
│   │   └── events/
│   │       ├── index.ts        # generatePanoramaEvents() – parses wiki-table dump
│   │       └── data.ts         # Manual event overrides/additions
│   ├── engine-enums/
│   │   ├── index.ts            # generateEngineEnums() – scans server.dll binary
│   │   ├── types.ts            # EngineEnum, EngineEnumMember
│   │   └── data.ts             # Enum prefix definitions + additional enums
│   ├── convars/
│   │   └── index.ts            # generateConvars() – parses cvarlist
│   ├── generate-changelog.js   # Changelog diff: compares states, outputs per-version JSON
│   └── generate-convars.js     # Secondary convar generation
├── dumper/                     # Dump capture tooling
│   ├── dump                    # THE monolithic dump file (60K+ lines)
│   ├── addon_init.lua          # Lua script: introspects _G, captures function signatures
│   ├── addon_game_mode.lua     # Companion Lua file
│   ├── start-dumper.mts        # Launches Dota 2, captures console output
│   ├── vconsole.mts            # VConsole automation
│   ├── build-modifiers.ts      # Extracts modifier_list.json from dump
│   ├── native-modifiers/       # server.dll analysis: native modifiers' functions + formulas (Python)
│   ├── native-modifiers.mts    # Runs it after auto-dump → native_modifiers.json
│   └── build-native-modifiers.ts # native_modifiers.json → files/vscripts/native_modifiers.json
├── files/                      # Generated output (published in npm)
│   ├── convars.json
│   ├── engine-enums.json / .d.ts
│   ├── events.json / .d.ts
│   ├── changelog-index.json
│   ├── changelog-states/       # Per-version snapshots for diff
│   ├── changelogs/             # Per-version changelog JSON
│   ├── panorama/
│   │   ├── api.json / .d.ts    # Panorama JS interfaces
│   │   ├── css.json / .d.ts    # Panorama CSS properties
│   │   ├── enums.json / .d.ts  # Panorama enums
│   │   ├── events.json / .d.ts # Panorama events
│   │   └── panels.json / .d.ts # Panorama panel types + XML attributes (from layout XSD)
│   └── vscripts/
│       ├── api.json / .d.ts    # Lua API declarations
│       ├── api-types.json / .d.ts # Type definitions (Object, Nominal, Primitive)
│       ├── enums.json / .d.ts  # Enum + constant declarations
│       ├── modifier_list.json  # Modifier names by category
│       └── native_modifiers.json # Per native modifier: declared functions, property formulas
├── src/                        # Runtime library (compiled to lib/)
│   ├── helpers/
│   │   └── vscripts.ts         # allData, findTypeByName(), getDeepTypes(), getFuncDeepTypes()
│   ├── utils/
│   │   ├── cache.ts
│   │   ├── core.ts
│   │   └── github.ts
│   ├── localization/           # Localization utilities
│   ├── schema-builder/         # KV schema builder
│   └── schemas/                # Dota 2 KV schema definitions
│       ├── abilities/
│       ├── units/
│       └── common.ts, portraits.ts, resources.ts
├── lib/                        # Compiled output of src/ (published)
└── test/                       # Jest tests
```

### Key Data Types

**VScript declarations** (`build/vscripts/api/types.ts`):
- `Declaration = FunctionDeclaration | ClassDeclaration`
- `ClassDeclaration` has `name`, `clientName?`, `instance?`, `extend?`, `members[]`
- `FunctionDeclaration` has `name`, `available?` (server/client/both), `args[]`, `returns[]`
- `Type = string | LiteralType | TableType | ArrayType | FunctionType`
- `Availability = 'server' | 'client' | 'both'`

**Panorama API** (`build/panorama/api/types.ts`):
- `PanoramaApiInterface { name, description?, members: PanoramaApiFunction[] }`
- `PanoramaApiFunction { name, description?, args: PanoramaApiFunctionArg[], returns? }`

**Events** (`build/events/types.ts`):
- `Event { name, sourceFile, description, local, fields: EventField[] }`

---

## Development Workflows

### Full Rebuild (requires Dota 2 installed)

```bash
npm run build
```

This runs: clean → `tsx build` (finds Dota 2 via Steam, processes dumps + VPKs) → `tsc -p src` → modifiers → convars → changelog.

### Quick Iteration (data already generated)

```bash
npm run build:tsc    # Only recompile runtime library
npm run dev          # Watch mode for both static + tsc
```

### Capturing New Dumps

```bash
npm run auto-dump    # Launches Dota 2, captures console dumps → dumper/dump
```

The `dumper/dump` file is a monolithic text file with sections delimited by `$> section_name`. Each section contains the raw output of a Dota 2 console command, with two exceptions produced by the dumper itself: `panorama_panels` (compact JSON digest of the layout XSD that `panorama_generate_layout_xsd` puts on the clipboard) and `panel_typescript_declarations` (phase 2: after the main dump and modifier test, the dumper sends `cl_panorama_typescript_declarations <type>` over vConsole for every panel type found in the XSD and stores the interfaces that differ from their base type).

The engine only exposes TypeScript declarations for panel types that have been *instantiated*, so the dumper installs a custom-game UI (`dumper/panorama/` → `content/dota_addons/dumper/panorama/layout/custom_game/`, compiled by the `-tools` launch) that `$.CreatePanel`s every known creatable panel type on load — this makes their JS classes visible to phase 2. Every Windows run copies the compiled files back into `dumper/panorama/compiled/`, which is what Linux uses (there is no resource compiler on Linux; the dumper warns when the compiled JS no longer matches `dumper_panels.js`).

#### Modifier properties

`dumper/modifier_test_properties.lua` is a modifier that declares every modifier function and reports which of them the engine actually calls (`HasFunction`) → `dumper/modifier_test_output.txt` → `files/vscripts/modifier_properties.json` (`false` = the function is `broken` in the generated docs). The function list is read from the engine's own `MODIFIER_PROPERTY_*` / `MODIFIER_EVENT_*` globals at runtime — never hardcode it, because `modifierfunction` values are positional and a value inserted in the middle of the enum shifts every later result onto the previous name.

The `-- BASELINE START/END` block in that file holds the previous dump's state, used only to report what changed; `dumper/modifier-baseline.mts` rewrites it after every successful dump and, when the enum itself gained or lost members, prints a "REPEAT THE DUMP" notice at the end of `npm run auto-dump`. `build:modifier-properties` independently cross-checks the test output against the `modifierfunction` enum in `dumper/dump` and refuses to overwrite the JSON when they disagree.

#### Native modifiers

`dumper/native-modifiers/extract.py` (Python 3 + capstone, the same requirement as `automation/funcdiff.py`) reads server.dll without launching the game: every class derived from `CDOTA_Buff`, the modifier functions its `DeclareFunctions` registers, and for every property the value its handler returns as a formula over special values (`%name%`), creation parameters (`kv.name`), `params` fields, the stack count and named calls on caster / parent / ability (`parent:IsRangedAttacker()`, `state(parent, MODIFIER_STATE_X)`). A symbolic executor follows every path of the x86-64 code; names come from the Lua bindings of the same DLL (each method's native code becomes a template), so nothing is hard-coded per build. Status per function: `constant`, `formula`, `partial` (some part shown as `?`), `unresolved`, `event` (events are listed without a formula). `CheckState` is read the same way: per modifier the `MODIFIER_STATE_*` it sets true / false and the condition (`states`). Details, the formula syntax and the output schema: `dumper/native-modifiers/README.md`.

It runs at the end of every successful `npm run auto-dump`, or alone with `npm run dump:native-modifiers` (it only needs the installed server.dll; `DOTA_SERVER_BINARY` on Linux, as for engine enums; with only libserver.so or without Python/capstone the previous file is kept), and writes `dumper/native_modifiers.json` with the game version from steam.inf. `build:native-modifiers` checks it against the dump (version, `modifierfunction` names), adds the ability whose special values the formulas read (`ability`, or `abilities` when several define all of them) and writes `files/vscripts/native_modifiers.json`. The changelog tracks every modifier function with its formula as the value and every state with its value and condition (`modifier_state`) (a changed formula is a game change; never part of the Documentation block).

### Capturing on Linux

`npm run auto-dump` also runs on Linux, two ways. Everything Linux-only is in `dumper/linux/`.

**Windows client + Workshop Tools under Wine (preferred, `DUMPER_WINE_LAUNCH=dumper/linux/wine-launch.sh`)**: a real `-tools` dump, identical in content to a Windows one. `start-dumper.mts` then takes the Windows path (vConsole on port 29000, the same arguments) and only launches/stops the Linux way.

- Files: steamcmd `+@sSteamCmdForcePlatformType windows +download_depot 570 373302 / 373303 / 381450` (DX11 shaders, binaries, Workshop Tools) and `+download_depot 1007 1004` (Steamworks redist: `steamclient64.dll`, without which the listen server's Steamworks init is fatal). The launcher lays the depots over the Linux install in an overlay (`DUMPER_WIN_DEPOTS`, upper dir = `dirname DUMPER_GAME_DIR`), so the shared VPKs are not downloaded twice.
- Wine prefix (`WINEPREFIX`), prepared by the launcher: `winsqlite3.c` stands in for Windows 10's `winsqlite3.dll` (the tools import it, Wine lacks it), the Steamworks DLLs go to `C:\Program Files (x86)\Steam` with `HKCU\Software\Valve\Steam\ActiveProcess\SteamClientDll64`. Rendering: `-vulkan` through winevulkan to the host driver (lavapipe works). `-language` from `DUMPER_LANGUAGE`.
- The layout XSD is read from the Wine clipboard by `getclip.c` (instead of PowerShell). The tools' "Stall detected." message, frequent under Wine, is dropped from the capture. `DOTA_SERVER_BINARY` points `build/engine-enums` at the depot's `server.dll`.

**Linux client** (fallback): `dumper/start-dumper.mts` branches on `process.platform`:

- **Launch**: `DUMPER_LAUNCH` (default `game/dota.sh`) gets `-dumper_client -novid -nosound -console -condebug -addon dumper +sv_cheats 1 +dota_launch_custom_game dumper dota`, a listen server with the forced hero. `DOTA2_DIR` names the install (`build/util/dota-dir.ts`, also used by the build). `dumper/linux/headless-launch.sh` is a launcher for servers without a display or GPU: Xvfb (`DUMPER_XVFB_DISPLAY`), the Steam Runtime (`STEAM_RUNTIME_ENTRY`) and an overlay over `game/` whose upper dir is `DUMPER_GAME_DIR` (the install stays untouched, `gameinfo.gi` without Metamod). The dumper writes the addon, reads the console log and writes the panel cfgs under `DUMPER_GAME_DIR` (default: `game/` of the install).
- **`dumper_hook.so`** (`dumper_hook.c`, built with gcc on first use into `dumper/linux/.build/`, LD_PRELOAD). Outside tools mode `libvscript.so` never creates the `FDesc`/`CDesc`/`EDesc` tables `addon_init.lua` reads; the hook patches the "tools mode?" checks guarding them in memory when the engine loads the library (`vscript-patch.mts` finds them by pattern: the `VApplication001` interface slot followed by `call [rax+0xd0]`). It also makes `SDL_SetClipboardText` write the layout XSD to a file: SDL3 on X11 cannot hand 22 MB over the clipboard and the client dies.
- **Output**: no vConsole on Linux. `console-log.mts` follows the `-condebug` console.log (Dota recreates it at start) and strips the `MM/DD HH:MM:SS ` and `[Channel] ` prefixes of message-start lines. The addon SCRIPT starts with `log_flags Console -ConsoleOnly`, without which console commands' output (cvarlist, panorama help/declarations) is not written to the file.
- **Panel phase**: the addon execs `cfg/dumper_panels.cfg` until the dumper has written `dumper_panels_begin <n>` there, then one `dumper_panels_<i>.cfg` chunk per think (one exec of ~1600 commands overflows the command buffer). The cfgs are created empty before launch and rewritten in place (an overlay hides files added to or renamed in the upper dir from outside).
- **Carry-forward** (`carry-forward.mts`): a retail client registers only ~2600 of the ~5200 convars; the missing (development) entries of `cvarlist` are copied from the previous dump, which only a Windows `-tools` dump can refresh. 64-bit integer arguments come without a TS type on Linux (`SetDialogVariableTime`); those lines are taken from the previous dump when it has the same member with types.
- The client renders in software at 1-3 fps: a run takes about 10 minutes and game time runs ~5x slower than real time; the timeouts are longer on Linux. Attempts write `dumper/dump.partial`; `dumper/dump` is replaced only by a complete dump.

`automation/` keeps a Linux server's clone in step with the installed Dota build (Wine dump with the Linux client as fallback, a control dump of the same build to expose dumper noise → `dump-checks/<version>.md`, build, test, commit, push, plus an update report → `reports/<version>.md`: API changes from the dump and `.so` changes: a Claude Haiku draft over everything, checked and finished by Claude Opus as a read-only agent); see `automation/README.md`. `automation/dump-diff.py A B` compares two raw dumps section by section.

### Testing

```bash
npm test             # Jest: validates files match dump data
```

---

## Key Patterns & Conventions

### Dump File Structure

The `dumper/dump` file uses `$> ` as section markers:
```
$> script_reload
{ ... raw JSON from Lua introspection ... }
$> cl_script_reload
{ ... client-side Lua dump ... }
$> cl_panorama_typescript_declarations
interface CPanoramaScript_GameEvents { ... }
interface $ { ... }
$> dump_panorama_events
| Event name | ... |
```

Access via `readDump('section_name')` which splits and extracts the section text.

### Type Export Pattern

Every types file in `build/` uses markers:

```typescript
// EXPORT START
export interface MyType {
  name: string;
}
// EXPORT END
```

`exportNamespacedRoot(fileName, namespace, root)` reads these markers and generates:
```typescript
declare namespace myNamespace {
  export interface MyType { name: string; }
}
declare const myNamespace: myNamespace.Root[];
export = myNamespace;
```

### Extension Data Pattern

VScript types are enhanced via hand-maintained overrides in `build/vscripts/api/data/index.ts`:

```typescript
export const classExtensions: Record<string, ClassExtension> = {
  CDOTA_BaseNPC: {
    members: {
      GetAbsOrigin: { returns: ["Vector"] },  // Override dump's "handle"
      // Add methods not in dump:
      SetForceAttackTarget: { args: [["target", "CDOTA_BaseNPC | nil"]] },
    },
  },
};
```

### Normalization

All descriptions and argument names go through normalization:
- `formatArgumentName(name, index)` strips Hungarian notation (e.g., `pszAbilityName` → `abilityName`)
- `formatDescription(desc)` ensures proper capitalization + trailing punctuation
- `clearDescription(funcName, desc)` removes embedded argument type info from descriptions

### Changelog Generation

`build/generate-changelog.js`:
1. Reads version info from `dumper/dump` header
2. Baseline: the files of the newest commit whose dump is a different version (read with `git show`, not the `files/changelog-states/` snapshots)
3. `changes` (game changes): that baseline → the commit that committed this version's dump (the working tree while the dump is not committed yet)
4. `documentation`: this version's dump commit → working tree, i.e. hand-made fixes after the dump. It also compares descriptions, argument descriptions, the abstract modifier handlers and the fields of object types (`type_field` items). The site shows it as a separate "Documentation" block; the index gets `documentationCount`. Rerun `npm run build:changelog` after such fixes
5. Outputs `files/changelogs/<version>.json`, `files/changelog-states/<version>.json` + updates `files/changelog-index.json`

---

## Adding Features Checklist

1. **New dump section** → Add section handling in `build/index.ts` + create parser in `build/<name>/`
2. **New VScript type override** → Add to `classExtensions` or `functionExtensions` in `build/vscripts/api/data/index.ts`
3. **New panorama dump section** → Parse in `build/panorama/<type>/index.ts`, add to `generatePanorama()` in `build/panorama/index.ts`
4. **New output file** → Use `outputJson(name, data)` from `build/util/`, add `.d.ts` via `exportNamespacedRoot()`
5. **New runtime helper** → Add to `src/`, it compiles to `lib/` and is published
6. **Track in changelog** → Add file reader in `build/generate-changelog.js` `trackedFiles` array
7. **New schema** → Add to `src/schemas/`, export from `src/schemas/index.ts`

---

## Integration with ModDota Site

The ModDota API site (`moddota.github.io-1/api/`) consumes this package:

| Site imports | Package path |
|---|---|
| Lua API declarations | `@moddota/dota-data/lib/helpers/vscripts` |
| Game events | `@moddota/dota-data/files/events` |
| Panorama API | `@moddota/dota-data/files/panorama/api` |
| Panorama CSS | `@moddota/dota-data/files/panorama/css` |
| Panorama enums | `@moddota/dota-data/files/panorama/enums` |
| Panorama events | `@moddota/dota-data/files/panorama/events` |
| API type definitions | `@moddota/dota-data/files/vscripts/api-types` |
| Modifiers list | `@moddota/dota-data/files/vscripts/modifier_list.json` |
| Console variables | `@moddota/dota-data/files/convars.json` |

In dev mode, the site's webpack config aliases these directly to `../../dota-data/` for live editing without `npm link`.
