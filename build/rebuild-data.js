/**
 * Script to rebuild data files from the dump
 * Run this after updating the dumper/dump file
 * 
 * Usage: node build/rebuild-data.js
 */

const { execSync } = require('child_process');
const path = require('path');

const rootDir = path.join(__dirname, '..');

console.log('=== Rebuilding Dota Data ===\n');

// Generate convars
console.log('1. Generating convars.json...');
try {
  require('./generate-convars.js');
} catch (e) {
  console.error('Error generating convars:', e.message);
}

// Generate changelog
console.log('\n2. Generating changelog.json...');
try {
  require('./generate-changelog.js');
} catch (e) {
  console.error('Error generating changelog:', e.message);
}

console.log('\n=== Data rebuild complete! ===');
console.log('If the dev server is running, changes should auto-reload.');
console.log('Otherwise, restart with: npm run dev');
