const fs = require('fs');
const path = require('path');

const dumpPath = path.join(__dirname, '../dumper/dump');
const outputPath = path.join(__dirname, '../files/convars.json');

const dump = fs.readFileSync(dumpPath, 'utf8');
const [, ...groups] = dump.split(/\$> (.+)/g);
let cvarlist = groups[groups.indexOf('cvarlist') + 1];
const lines = cvarlist.split(/\r?\n/);

const convars = {};

for (const line of lines) {
  if (!line.includes(':') || line.startsWith('cvar list') || line.startsWith('-----') || line.match(/^\d+ convars/)) {
    continue;
  }
  
  const parts = line.split(' : ');
  if (parts.length < 3) continue;
  
  const name = parts[0].trim();
  const value = parts[1].trim();
  const flagsPart = parts[2].trim();
  const desc = parts.slice(3).join(' : ').trim();
  
  const flags = flagsPart
    .split(',')
    .map(f => f.trim().replace(/^"|"$/g, ''))
    .filter(f => f);
  
  convars[name] = {
    default: value,
    flags,
    description: desc
  };
}

// Sort by name
const sortedConvars = {};
Object.keys(convars).sort().forEach(key => {
  sortedConvars[key] = convars[key];
});

// build:static already wrote convars.json moments ago; on Windows the file can
// still be briefly locked (AV/indexer scanning the fresh write), which surfaces
// as a transient EBUSY/EPERM/UNKNOWN error. Retry a few times before failing.
function writeFileSyncWithRetry(filePath, data, retries = 8) {
  for (let attempt = 0; ; attempt++) {
    try {
      fs.writeFileSync(filePath, data);
      return;
    } catch (err) {
      const transient = ['EBUSY', 'EPERM', 'EACCES', 'UNKNOWN'].includes(err.code);
      if (!transient || attempt >= retries) throw err;
      Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 200 * (attempt + 1));
    }
  }
}

writeFileSyncWithRetry(outputPath, JSON.stringify(sortedConvars, null, 2));
console.log('Generated convars.json with', Object.keys(sortedConvars).length, 'entries');
