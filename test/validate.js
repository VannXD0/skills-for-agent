// test/validate.js
const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');

console.log('--- 1. Validating package.json & Manifests ---');
const pkgPath = path.join(rootDir, 'package.json');
if (!fs.existsSync(pkgPath)) {
  console.error('FAIL: package.json missing');
  process.exit(1);
}
JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
console.log('PASS: package.json is valid JSON');

console.log('--- 2. Validating Platform Entrypoints & Root Files ---');
const rootFiles = [
  'base-rules.md',
  'AGENTS.md',
  'CLAUDE.md',
  'CODEX.md',
  'GEMINI.md',
  'PI.md',
  '.cursorrules',
  '.windsurfrules',
  '.aider.conf.yml',
  '.aider/CONVENTIONS.md',
  '.github/copilot-instructions.md'
];

for (const rf of rootFiles) {
  const p = path.join(rootDir, rf);
  if (!fs.existsSync(p)) {
    console.error(`FAIL: Missing ${rf}`);
    process.exit(1);
  }
}
console.log('PASS: All platform rules and entrypoints exist');

console.log('--- 3. Validating Core Skills Structure & Frontmatter ---');
const skillsDir = path.join(rootDir, 'skills');
const skills = fs.readdirSync(skillsDir, { withFileTypes: true }).filter(d => d.isDirectory());
if (skills.length < 10) {
  console.error(`FAIL: Expected at least 10 skills, found ${skills.length}`);
  process.exit(1);
}

for (const s of skills) {
  const skillMd = path.join(skillsDir, s.name, 'SKILL.md');
  if (!fs.existsSync(skillMd)) {
    console.error(`FAIL: Missing SKILL.md in ${s.name}`);
    process.exit(1);
  }
  const content = fs.readFileSync(skillMd, 'utf8');
  if (!content.startsWith('---') || !content.includes('name:') || !content.includes('description:')) {
    console.error(`FAIL: Invalid YAML frontmatter in ${s.name}/SKILL.md`);
    process.exit(1);
  }
}
console.log(`PASS: All ${skills.length} skills verified with valid frontmatter`);

console.log('\nAll structural checks passed!\n');
