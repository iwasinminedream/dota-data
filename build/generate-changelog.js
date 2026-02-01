const fs = require('fs');
const path = require('path');

const filesDir = path.join(__dirname, '../files');
const changelogPath = path.join(filesDir, 'changelog.json');

// Files to track for changes
const trackedFiles = [
  { file: 'vscripts/api.json', type: 'api', name: 'Lua API' },
  { file: 'vscripts/api-types.json', type: 'types', name: 'Lua Types' },
  { file: 'vscripts/enums.json', type: 'enums', name: 'Lua Enums' },
  { file: 'vscripts/modifier_list.json', type: 'modifiers', name: 'Modifiers' },
  { file: 'events.json', type: 'events', name: 'Game Events' },
  { file: 'panorama/events.json', type: 'panorama_events', name: 'Panorama Events' },
  { file: 'panorama/enums.json', type: 'panorama_enums', name: 'Panorama Enums' },
  { file: 'convars.json', type: 'convars', name: 'Console Variables' },
  { file: 'engine-enums.json', type: 'engine_enums', name: 'Engine Enums' },
];

// Read the dump file to get version info
const dumpPath = path.join(__dirname, '../dumper/dump');
const dump = fs.readFileSync(dumpPath, 'utf8');

// Extract version information
const versionMatch = dump.match(/ClientVersion=(\d+)/);
const dateMatch = dump.match(/VersionDate=(.+)/);
const timeMatch = dump.match(/VersionTime=(.+)/);

const currentVersion = {
  clientVersion: versionMatch ? versionMatch[1] : 'unknown',
  date: dateMatch ? dateMatch[1].trim() : new Date().toISOString().split('T')[0],
  time: timeMatch ? timeMatch[1].trim() : '',
  timestamp: new Date().toISOString(),
};

// Load existing changelog or create new one
let changelog = {
  versions: [],
  states: {},
  changes: {},
};

if (fs.existsSync(changelogPath)) {
  try {
    changelog = JSON.parse(fs.readFileSync(changelogPath, 'utf8'));
  } catch (e) {
    console.log('Could not parse existing changelog, creating new one');
  }
}

// Check if this version already exists
const existingVersionIndex = changelog.versions.findIndex(
  (v) => v.clientVersion === currentVersion.clientVersion
);

if (existingVersionIndex !== -1) {
  console.log(`Version ${currentVersion.clientVersion} already in changelog, updating state...`);
  // Remove existing version to re-add with updated state
  changelog.versions.splice(existingVersionIndex, 1);
  delete changelog.states[currentVersion.clientVersion];
  delete changelog.changes[currentVersion.clientVersion];
}

// Helper to extract function signatures for comparison
function getFunctionSignature(func) {
  if (!func.args) return func.name;
  const args = func.args.map(a => `${a.name}:${Array.isArray(a.types) ? a.types.join('|') : a.types || 'any'}`).join(',');
  return `${func.name}(${args})`;
}

// Helper to extract detailed items from API
function extractApiItems(content) {
  const items = {
    classes: [],
    functions: [],
    constants: [],
    enums: [],
    methods: {},
  };
  
  if (!Array.isArray(content)) return items;
  
  for (const item of content) {
    if (item.kind === 'class') {
      items.classes.push(item.name);
      // Track methods with signatures
      if (item.members) {
        items.methods[item.name] = item.members
          .filter(m => m.kind === 'function')
          .map(m => getFunctionSignature(m));
      }
    } else if (item.kind === 'function') {
      items.functions.push(getFunctionSignature(item));
    } else if (item.kind === 'constant') {
      items.constants.push(`${item.name}=${item.value}`);
    } else if (item.kind === 'enum') {
      items.enums.push(item.name);
    }
  }
  
  return items;
}

// Helper to extract types from api-types
function extractTypes(content) {
  if (!Array.isArray(content)) return [];
  return content.map(t => `${t.kind}:${t.name}`);
}

// Store current state for comparison
const currentState = {};

for (const tracked of trackedFiles) {
  const filePath = path.join(filesDir, tracked.file);
  if (!fs.existsSync(filePath)) {
    console.log(`File not found: ${tracked.file}`);
    continue;
  }

  try {
    const content = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    const fileKey = tracked.type;

    if (tracked.type === 'api') {
      // Detailed API tracking
      const apiItems = extractApiItems(content);
      currentState[fileKey] = {
        type: 'api',
        name: tracked.name,
        items: [...apiItems.classes, ...apiItems.functions, ...apiItems.constants],
        details: apiItems,
      };
    } else if (tracked.type === 'types') {
      // Track type definitions
      currentState[fileKey] = {
        type: 'types',
        name: tracked.name,
        items: extractTypes(content),
      };
    } else if (tracked.type === 'modifiers') {
      // Flatten modifier list
      const allModifiers = [];
      Object.entries(content).forEach(([category, items]) => {
        if (Array.isArray(items)) {
          items.forEach(item => allModifiers.push(`${category}:${item}`));
        }
      });
      currentState[fileKey] = {
        type: 'modifiers',
        name: tracked.name,
        items: allModifiers,
      };
    } else if (Array.isArray(content)) {
      // Arrays (events, enums)
      currentState[fileKey] = {
        type: 'array',
        name: tracked.name,
        items: content.map((item) => {
          if (typeof item === 'string') return item;
          if (item.name) return item.name;
          return JSON.stringify(item);
        }),
      };
    } else if (typeof content === 'object') {
      // Objects (convars, panorama events)
      currentState[fileKey] = {
        type: 'object',
        name: tracked.name,
        items: Object.keys(content),
      };
    }
  } catch (e) {
    console.error(`Error processing ${tracked.file}:`, e.message);
  }
}

// Calculate changes from previous version
const changes = {
  added: {},
  removed: {},
  modified: {},
};

const previousVersion = changelog.versions[0];
if (previousVersion && changelog.states && changelog.states[previousVersion.clientVersion]) {
  const prevState = changelog.states[previousVersion.clientVersion];

  for (const [fileKey, current] of Object.entries(currentState)) {
    const prev = prevState[fileKey];
    if (!prev) {
      // Entire category is new
      changes.added[fileKey] = current.items;
      continue;
    }

    const prevSet = new Set(prev.items);
    const currSet = new Set(current.items);

    const added = current.items.filter((item) => !prevSet.has(item));
    const removed = prev.items.filter((item) => !currSet.has(item));

    if (added.length > 0) {
      changes.added[fileKey] = added;
    }
    if (removed.length > 0) {
      changes.removed[fileKey] = removed;
    }
  }
}

// Add new version to changelog
changelog.versions.unshift(currentVersion);

// Store current state for future comparisons
changelog.states[currentVersion.clientVersion] = currentState;

// Store changes for this version (empty for first version)
changelog.changes[currentVersion.clientVersion] = changes;

// Keep only last 50 versions
if (changelog.versions.length > 50) {
  const removedVersions = changelog.versions.splice(50);
  removedVersions.forEach((v) => {
    delete changelog.states[v.clientVersion];
    delete changelog.changes[v.clientVersion];
  });
}

// Write updated changelog
fs.writeFileSync(changelogPath, JSON.stringify(changelog, null, 2));

console.log(`Generated changelog for version ${currentVersion.clientVersion}`);
console.log(`Total versions tracked: ${changelog.versions.length}`);

// Summary of changes
const totalAdded = Object.values(changes.added).reduce((sum, arr) => sum + arr.length, 0);
const totalRemoved = Object.values(changes.removed).reduce((sum, arr) => sum + arr.length, 0);

if (totalAdded > 0 || totalRemoved > 0) {
  console.log(`Changes: +${totalAdded} added, -${totalRemoved} removed`);
  Object.entries(changes.added).forEach(([key, items]) => {
    if (items.length > 0) console.log(`  ${key}: +${items.length}`);
  });
  Object.entries(changes.removed).forEach(([key, items]) => {
    if (items.length > 0) console.log(`  ${key}: -${items.length}`);
  });
} else {
  console.log('No changes detected from previous version (or this is the first version)');
}