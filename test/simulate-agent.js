// test/simulate-agent.js
const assert = require('assert');

console.log('=== Running UASF Multi-Agent Contract Simulation Tests ===');

// 1. Instruction Precedence Test
const tiers = {
  OPERATOR: 1,
  SAFETY_FLOOR: 2,
  UASF_CORE: 3,
  EXTERNAL_SKILLS: 4,
  LEARNED_PROFILE: 5
};

function resolveConflict(directiveA, directiveB) {
  return directiveA.tier < directiveB.tier ? directiveA : directiveB;
}

const dirExternal = { id: 'ext-redesign', tier: tiers.EXTERNAL_SKILLS, action: 'restyle-ui' };
const dirCore = { id: 'uasf-zero-ui', tier: tiers.UASF_CORE, action: 'keep-ui-intact' };

const resolved = resolveConflict(dirExternal, dirCore);
assert.strictEqual(resolved.id, 'uasf-zero-ui');
console.log('PASS: Tier 3 UASF Zero-UI Invariant overrides Tier 4 External Skill');

// 2. Anti-Slop Heuristic Filter Test
const bannedPhrases = ['certainly!', 'here is the solution', 'hope this helps!'];
function testSlop(text) {
  const lower = text.toLowerCase();
  return bannedPhrases.some(p => lower.includes(p));
}

assert.strictEqual(testSlop('Certainly! Here is the solution for your APK.'), true);
assert.strictEqual(testSlop('Patched bytecode return register to 0x1.'), false);
console.log('PASS: Anti-slop verbal filter detects bot pleasantries');

// 3. Planning Gate Confirmation Test
const validTokens = ['go', 'gas', 'proceed', 'y', 'yes', 'approve'];
function isConfirmation(token) {
  return validTokens.includes(token.trim().toLowerCase());
}

assert.strictEqual(isConfirmation('gas'), true);
assert.strictEqual(isConfirmation('proceed'), true);
assert.strictEqual(isConfirmation('wait no'), false);
console.log('PASS: Planning gate confirmation tokens verified');

console.log('\nAll agent simulation tests passed cleanly!\n');
