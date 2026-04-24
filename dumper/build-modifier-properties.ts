import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';

const inputPath = join('dumper', 'modifier_test_output.txt');
const outputPath = join('files', 'vscripts', 'modifier_properties.json');

if (!existsSync(inputPath)) {
  console.log('No modifier_test_output.txt found — skipping modifier properties.');
  process.exit(0);
}

const content = readFileSync(inputPath, 'utf8');
const result: Record<string, boolean> = {};

for (const line of content.split(/\r?\n/)) {
  const match = line.match(/\["(MODIFIER_\w+)"\]\s*=\s*(true|false)/);
  if (match) {
    result[match[1]] = match[2] === 'true';
  }
}

const count = Object.keys(result).length;
if (count === 0) {
  console.warn('No modifier properties parsed from output.');
  process.exit(0);
}

mkdirSync(dirname(outputPath), { recursive: true });
writeFileSync(outputPath, JSON.stringify(result, null, 2), 'utf8');
console.log(`Wrote ${count} modifier properties → ${outputPath}`);
