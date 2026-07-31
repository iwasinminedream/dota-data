# Dota Data – Copilot Instructions

## Quick Start (Read This First)

**Architecture in one sentence**: An npm package (`@moddota/dota-data`) that parses raw Dota 2 dump files into structured JSON + TypeScript declarations consumed by the ModDota API site.

**Essential dev commands**:
- `npm run build` – full rebuild: clean → generate from dumps → compile TS → modifiers → convars → changelog
- `npm run build:static` – only regenerate JSON/d.ts from dumps (via `tsx build`)
- `npm run build:tsc` – compile `src/` → `lib/` (runtime helpers + schemas)
- `npm run dev` – watch mode: `build:static` + `tsc --watch` in parallel
- `npm test` – Jest tests
- `npm run auto-dump` – launches Dota 2 to capture new dump data

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
│   └── build-modifiers.ts      # Extracts modifier_list.json from dump
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
│       └── modifier_list.json  # Modifier names by category
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

The engine only exposes TypeScript declarations for panel types that have been *instantiated*, so the dumper installs a custom-game UI (`dumper/panorama/` → `content/dota_addons/dumper/panorama/layout/custom_game/`, compiled by the `-tools` launch) that `$.CreatePanel`s every known creatable panel type on load — this makes their JS classes visible to phase 2.

#### Modifier properties

`dumper/modifier_test_properties.lua` is a modifier that declares every modifier function and reports which of them the engine actually calls (`HasFunction`) → `dumper/modifier_test_output.txt` → `files/vscripts/modifier_properties.json` (`false` = the function is `broken` in the generated docs). The function list is read from the engine's own `MODIFIER_PROPERTY_*` / `MODIFIER_EVENT_*` globals at runtime — never hardcode it, because `modifierfunction` values are positional and a value inserted in the middle of the enum shifts every later result onto the previous name.

The `-- BASELINE START/END` block in that file holds the previous dump's state, used only to report what changed; `dumper/modifier-baseline.mts` rewrites it after every successful dump and, when the enum itself gained or lost members, prints a "REPEAT THE DUMP" notice at the end of `npm run auto-dump`. `build:modifier-properties` independently cross-checks the test output against the `modifierfunction` enum in `dumper/dump` and refuses to overwrite the JSON when they disagree.

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
2. Compares current `files/*.json` against previous snapshot in `files/changelog-states/<version>.json`
3. Diffs: added, removed, changed items across all data categories
4. Outputs `files/changelogs/<version>.json` + updates `files/changelog-index.json`

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
