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

fs.writeFileSync(outputPath, JSON.stringify(sortedConvars, null, 2));
console.log('Generated convars.json with', Object.keys(sortedConvars).length, 'entries');
