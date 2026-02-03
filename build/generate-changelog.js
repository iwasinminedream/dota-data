const fs = require('fs');
const path = require('path');

const filesDir = path.join(__dirname, '../files');
const changelogIndexPath = path.join(filesDir, 'changelog-index.json');
const changelogsDir = path.join(filesDir, 'changelogs');
const statesDir = path.join(filesDir, 'changelog-states');

// Ensure directories exist
[changelogsDir, statesDir].forEach(dir => {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
});

// Files to track
const trackedFiles = [
  { file: 'vscripts/api.json', type: 'api', name: 'Lua API' },
  { file: 'vscripts/api-types.json', type: 'types', name: 'Lua Types' },
  { file: 'vscripts/enums.json', type: 'enums', name: 'Lua Enums' },
  { file: 'vscripts/modifier_list.json', type: 'modifiers', name: 'Modifiers' },
  { file: 'events.json', type: 'events', name: 'Game Events' },
  { file: 'panorama/api.json', type: 'panorama_api', name: 'Panorama API' },
  { file: 'panorama/events.json', type: 'panorama_events', name: 'Panorama Events' },
  { file: 'panorama/enums.json', type: 'panorama_enums', name: 'Panorama Enums' },
  { file: 'convars.json', type: 'convars', name: 'Console Variables' },
  { file: 'engine-enums.json', type: 'engine_enums', name: 'Engine Enums' },
];

// Read the dump file to get version info
const dumpPath = path.join(__dirname, '../dumper/dump');
const dump = fs.readFileSync(dumpPath, 'utf8');

const versionMatch = dump.match(/ClientVersion=(\d+)/);
const dateMatch = dump.match(/VersionDate=(.+)/);
const timeMatch = dump.match(/VersionTime=(.+)/);

const currentVersion = {
  version: versionMatch ? versionMatch[1] : 'unknown',
  date: dateMatch ? dateMatch[1].trim() : new Date().toISOString().split('T')[0],
  time: timeMatch ? timeMatch[1].trim() : '',
};

console.log(`Processing version ${currentVersion.version}...`);

// Format function signature
function formatSignature(func) {
  if (!func.args || !func.args.length) return `${func.name}()`;
  const args = func.args.map(a => a.name).join(', ');
  return `${func.name}(${args})`;
}

// Extract items from API
function extractApiItems(content) {
  const items = [];
  if (!Array.isArray(content)) return items;
  
  for (const item of content) {
    if (item.kind === 'class') {
      items.push({ type: 'class', name: item.name });
      if (item.members) {
        for (const m of item.members) {
          if (m.kind === 'function') {
            items.push({ type: 'method', class: item.name, name: m.name, signature: formatSignature(m) });
          }
        }
      }
    } else if (item.kind === 'function') {
      items.push({ type: 'function', name: item.name, signature: formatSignature(item) });
    } else if (item.kind === 'constant') {
      items.push({ type: 'constant', name: item.name, value: item.value });
    }
  }
  return items;
}

// Extract enums with members
function extractEnums(content) {
  const items = [];
  if (!Array.isArray(content)) return items;
  
  for (const e of content) {
    items.push({ type: 'enum', name: e.name });
    if (e.members) {
      for (const m of e.members) {
        items.push({ type: 'enum_member', enum: e.name, name: m.name, value: m.value });
      }
    }
  }
  return items;
}

// Extract types
function extractTypes(content) {
  if (!Array.isArray(content)) return [];
  return content.map(t => ({ type: t.kind, name: t.name }));
}

// Extract modifiers
function extractModifiers(content) {
  const items = [];
  if (typeof content !== 'object') return items;
  for (const [cat, list] of Object.entries(content)) {
    if (Array.isArray(list)) {
      list.forEach(m => items.push({ type: 'modifier', category: cat, name: m }));
    }
  }
  return items;
}

// Extract events
function extractEvents(content) {
  if (typeof content !== 'object' || Array.isArray(content)) return [];
  return Object.keys(content).map(k => ({ type: 'event', name: k }));
}

// Extract convars
function extractConvars(content) {
  if (typeof content !== 'object' || Array.isArray(content)) return [];
  return Object.keys(content).map(k => ({ type: 'convar', name: k }));
}

// Build current state
function buildCurrentState() {
  const state = {};
  
  for (const tracked of trackedFiles) {
    const filePath = path.join(filesDir, tracked.file);
    if (!fs.existsSync(filePath)) continue;
    
    const content = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    let items = [];
    
    switch (tracked.type) {
      case 'api':
      case 'panorama_api':
        items = extractApiItems(content);
        break;
      case 'types':
        items = extractTypes(content);
        break;
      case 'enums':
      case 'panorama_enums':
      case 'engine_enums':
        items = extractEnums(content);
        break;
      case 'modifiers':
        items = extractModifiers(content);
        break;
      case 'events':
      case 'panorama_events':
        items = extractEvents(content);
        break;
      case 'convars':
        items = extractConvars(content);
        break;
    }
    
    state[tracked.type] = { name: tracked.name, items };
  }
  
  return state;
}

// Create item key for comparison
function itemKey(item) {
  if (item.type === 'method') return `method:${item.class}.${item.name}`;
  if (item.type === 'enum_member') return `enum_member:${item.enum}.${item.name}`;
  if (item.type === 'modifier') return `modifier:${item.category}:${item.name}`;
  return `${item.type}:${item.name}`;
}

// Compare states
function compareStates(prev, curr) {
  const changes = {};
  
  for (const [key, currData] of Object.entries(curr)) {
    const prevData = prev?.[key];
    const prevKeys = new Set((prevData?.items || []).map(itemKey));
    const currKeys = new Set(currData.items.map(itemKey));
    
    const added = currData.items.filter(i => !prevKeys.has(itemKey(i)));
    const removed = (prevData?.items || []).filter(i => !currKeys.has(itemKey(i)));
    
    if (added.length > 0 || removed.length > 0) {
      changes[currData.name] = { added, removed };
    }
  }
  
  if (prev) {
    for (const [key, prevData] of Object.entries(prev)) {
      if (!curr[key] && prevData.items.length > 0) {
        changes[prevData.name] = { added: [], removed: prevData.items };
      }
    }
  }
  
  return changes;
}

// Load previous state
function loadPreviousState(version) {
  const statePath = path.join(statesDir, `${version}.json`);
  if (fs.existsSync(statePath)) {
    return JSON.parse(fs.readFileSync(statePath, 'utf8'));
  }
  return null;
}

// Get previous version from index
function getPreviousVersion() {
  if (!fs.existsSync(changelogIndexPath)) return null;
  
  const index = JSON.parse(fs.readFileSync(changelogIndexPath, 'utf8'));
  for (const entry of index) {
    if (entry.version !== currentVersion.version) {
      return entry.version;
    }
  }
  return null;
}

// Main
const currState = buildCurrentState();

const prevVersion = getPreviousVersion();
console.log(`Previous version: ${prevVersion || 'none'}`);

const prevState = prevVersion ? loadPreviousState(prevVersion) : null;

if (!prevState && prevVersion) {
  console.log(`Warning: No state file for ${prevVersion}`);
}

const changes = compareStates(prevState, currState);

// Count changes
let addedCount = 0, removedCount = 0;
for (const cat of Object.values(changes)) {
  addedCount += cat.added?.length || 0;
  removedCount += cat.removed?.length || 0;
}

// Write changelog
const changelogEntry = {
  version: currentVersion.version,
  date: currentVersion.date,
  time: currentVersion.time,
  changes,
};

fs.writeFileSync(path.join(changelogsDir, `${currentVersion.version}.json`), JSON.stringify(changelogEntry, null, 2));

// Save state
fs.writeFileSync(path.join(statesDir, `${currentVersion.version}.json`), JSON.stringify(currState, null, 2));

// Update index
let index = [];
if (fs.existsSync(changelogIndexPath)) {
  index = JSON.parse(fs.readFileSync(changelogIndexPath, 'utf8'));
}

const existingIdx = index.findIndex(e => e.version === currentVersion.version);
const indexEntry = {
  version: currentVersion.version,
  date: currentVersion.date,
  time: currentVersion.time,
  addedCount,
  removedCount,
};

if (existingIdx !== -1) {
  index[existingIdx] = indexEntry;
} else {
  index.push(indexEntry);
}

index.sort((a, b) => parseInt(b.version) - parseInt(a.version));
fs.writeFileSync(changelogIndexPath, JSON.stringify(index, null, 2));

console.log(`\nGenerated changelog for version ${currentVersion.version}`);
console.log(`Changes: +${addedCount} added, -${removedCount} removed`);

if (addedCount > 0 || removedCount > 0) {
  for (const [cat, ch] of Object.entries(changes)) {
    const a = ch.added?.length || 0;
    const r = ch.removed?.length || 0;
    if (a > 0 || r > 0) console.log(`  ${cat}: +${a} -${r}`);
  }
}
