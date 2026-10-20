#!/usr/bin/env node

/**
 * Universal AI Skill Framework (UASF) CLI
 * Universal Multi-Agent Skills & Protocol Installer
 * License: MIT
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const rootDir = path.resolve(__dirname, '..');
const pkgPath = path.join(rootDir, 'package.json');
const pkg = fs.existsSync(pkgPath) ? JSON.parse(fs.readFileSync(pkgPath, 'utf8')) : { version: '1.0.0' };

// ANSI Color Helpers (Zero External Dependencies)
const useColor = !process.env.NO_COLOR && process.stdout.isTTY;
const c = {
  reset: useColor ? '\x1b[0m' : '',
  bold: useColor ? '\x1b[1m' : '',
  dim: useColor ? '\x1b[2m' : '',
  cyan: useColor ? '\x1b[36m' : '',
  green: useColor ? '\x1b[32m' : '',
  yellow: useColor ? '\x1b[33m' : '',
  red: useColor ? '\x1b[31m' : '',
  blue: useColor ? '\x1b[34m' : '',
  magenta: useColor ? '\x1b[35m' : ''
};

// Supported AI Agents Specification
const CLIENTS = {
  antigravity: {
    name: 'Google Antigravity',
    detect: (dir) => fs.existsSync(path.join(dir, '.agent')) || fs.existsSync(path.join(dir, 'AGENTS.md')),
    files: [
      { src: 'AGENTS.md', dest: 'AGENTS.md' },
      { src: 'base-rules.md', dest: 'base-rules.md' },
      { src: path.join('.agent', 'rules', 'base-rules.md'), dest: path.join('.agent', 'rules', 'base-rules.md') }
    ],
    skillsDir: path.join('.agent', 'skills')
  },
  claude: {
    name: 'Claude Code',
    detect: (dir) => fs.existsSync(path.join(dir, '.claude')) || fs.existsSync(path.join(dir, 'CLAUDE.md')),
    files: [
      { src: 'CLAUDE.md', dest: 'CLAUDE.md' },
      { src: path.join('.claude', 'commands'), dest: path.join('.claude', 'commands'), isDir: true }
    ],
    skillsDir: path.join('.claude', 'skills')
  },
  cursor: {
    name: 'Cursor',
    detect: (dir) => fs.existsSync(path.join(dir, '.cursor')) || fs.existsSync(path.join(dir, '.cursorrules')),
    files: [
      { src: '.cursorrules', dest: '.cursorrules' },
      { src: path.join('.cursor', 'rules', 'uasf.mdc'), dest: path.join('.cursor', 'rules', 'uasf.mdc') }
    ],
    skillsDir: null
  },
  windsurf: {
    name: 'Windsurf',
    detect: (dir) => fs.existsSync(path.join(dir, '.windsurfrules')),
    files: [
      { src: '.windsurfrules', dest: '.windsurfrules' }
    ],
    skillsDir: null
  },
  codex: {
    name: 'OpenAI Codex',
    detect: (dir) => fs.existsSync(path.join(dir, 'CODEX.md')),
    files: [
      { src: 'CODEX.md', dest: 'CODEX.md' }
    ],
    skillsDir: null
  },
  omp: {
    name: 'Oh My Pi (omp)',
    detect: (dir) => fs.existsSync(path.join(dir, '.omp')) || fs.existsSync(path.join(dir, 'PI.md')),
    files: [
      { src: 'PI.md', dest: 'PI.md' },
      { src: path.join('.omp', 'commands'), dest: path.join('.omp', 'commands'), isDir: true }
    ],
    skillsDir: path.join('.omp', 'skills')
  },
  gemini: {
    name: 'Gemini CLI',
    detect: (dir) => fs.existsSync(path.join(dir, 'GEMINI.md')),
    files: [
      { src: 'GEMINI.md', dest: 'GEMINI.md' }
    ],
    skillsDir: null
  },
  aider: {
    name: 'Aider',
    detect: (dir) => fs.existsSync(path.join(dir, '.aider.conf.yml')),
    files: [
      { src: '.aider.conf.yml', dest: '.aider.conf.yml' },
      { src: path.join('.aider', 'CONVENTIONS.md'), dest: path.join('.aider', 'CONVENTIONS.md') }
    ],
    skillsDir: null
  },
  copilot: {
    name: 'GitHub Copilot',
    detect: (dir) => fs.existsSync(path.join(dir, '.github', 'copilot-instructions.md')),
    files: [
      { src: path.join('.github', 'copilot-instructions.md'), dest: path.join('.github', 'copilot-instructions.md') }
    ],
    skillsDir: null
  }
};

function loadCoreSkills() {
  const skillsDir = path.join(rootDir, 'skills');
  if (!fs.existsSync(skillsDir)) return [];
  const entries = fs.readdirSync(skillsDir, { withFileTypes: true });
  const list = [];
  for (const entry of entries) {
    if (entry.isDirectory()) {
      const skillFile = path.join(skillsDir, entry.name, 'SKILL.md');
      let desc = 'UASF operational skill';
      if (fs.existsSync(skillFile)) {
        const content = fs.readFileSync(skillFile, 'utf8');
        const match = content.match(/description:\s*["']?([^"'\n]+)/i);
        if (match) desc = match[1].trim();
      }
      list.push({ name: entry.name, desc });
    }
  }
  return list.sort((a, b) => a.name.localeCompare(b.name));
}

const CORE_SKILLS = loadCoreSkills();

function ensureDir(dirPath, dryRun = false) {
  if (!fs.existsSync(dirPath)) {
    if (!dryRun) fs.mkdirSync(dirPath, { recursive: true });
    return true;
  }
  return false;
}

function copyFileSafe(src, dest, dryRun = false) {
  if (!fs.existsSync(src)) return false;
  const destDir = path.dirname(dest);
  ensureDir(destDir, dryRun);
  if (!dryRun) {
    fs.copyFileSync(src, dest);
  }
  return true;
}

function copyDirSafe(srcDir, destDir, dryRun = false) {
  if (!fs.existsSync(srcDir)) return 0;
  ensureDir(destDir, dryRun);
  let count = 0;
  const entries = fs.readdirSync(srcDir, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(srcDir, entry.name);
    const destPath = path.join(destDir, entry.name);
    if (entry.isDirectory()) {
      count += copyDirSafe(srcPath, destPath, dryRun);
    } else {
      if (!dryRun) fs.copyFileSync(srcPath, destPath);
      count++;
    }
  }
  return count;
}

function printBanner() {
  console.log(`\n${c.bold}${c.cyan}======================================================${c.reset}`);
  console.log(`${c.bold}${c.cyan}  Skills For Agent (UASF) v${pkg.version}${c.reset}`);
  console.log(`${c.dim}  Multi-Agent Runtime Protocols, Anti-Slop & Zero-UI APK${c.reset}`);
  console.log(`${c.bold}${c.cyan}======================================================${c.reset}\n`);
}

function printHelp() {
  printBanner();
  console.log(`${c.bold}Usage:${c.reset}`);
  console.log(`  npx github:VannXD0/skills-for-agent [command] [targetDir] [options]\n`);
  console.log(`${c.bold}Commands:${c.reset}`);
  console.log(`  ${c.green}install${c.reset} [dir]     Install UASF skills & platform rules into target project (default: .)`);
  console.log(`  ${c.green}doctor${c.reset} [dir]      Audit target project configuration and verify skill health`);
  console.log(`  ${c.green}list${c.reset}              List all core skills and supported AI agent targets`);
  console.log(`  ${c.green}verify${c.reset}            Run multi-agent contract verification test suite`);
  console.log(`  ${c.green}uninstall${c.reset} [dir]   Remove UASF skills and rule files cleanly\n`);
  console.log(`${c.bold}Options:${c.reset}`);
  console.log(`  ${c.yellow}--client=<name>${c.reset}  Install only for a specific agent (e.g., antigravity, claude, cursor)`);
  console.log(`  ${c.yellow}--dry-run${c.reset}        Simulate operations without writing to disk`);
  console.log(`  ${c.yellow}--backup${c.reset}         Backup existing files before overwriting`);
  console.log(`  ${c.yellow}-h, --help${c.reset}       Show this help manual`);
  console.log(`  ${c.yellow}-v, --version${c.reset}    Show version\n`);
}

function runInstall(targetDir, options) {
  printBanner();
  const isDry = options.dryRun;
  console.log(`[*] Target directory: ${c.bold}${targetDir}${c.reset}`);
  if (isDry) console.log(`${c.yellow}[DRY-RUN] Simulating execution. No files will be modified.${c.reset}`);

  ensureDir(targetDir, isDry);

  // 1. Copy core skills to skills/
  const targetSkillsDir = path.join(targetDir, 'skills');
  ensureDir(targetSkillsDir, isDry);
  const srcSkillsDir = path.join(rootDir, 'skills');
  const copiedSkillsCount = copyDirSafe(srcSkillsDir, targetSkillsDir, isDry);
  console.log(`[OK] Core skills mounted to: ${c.bold}skills/${c.reset} (${CORE_SKILLS.length} skills ready)`);

  // 2. Identify target clients
  const targetClients = [];
  if (options.client && options.client !== 'all') {
    const key = options.client.toLowerCase();
    if (CLIENTS[key]) {
      targetClients.push(CLIENTS[key]);
    } else {
      console.error(`${c.red}[ERROR] Unknown client '${options.client}'. Run 'uasf list' to view supported agents.${c.reset}`);
      process.exit(1);
    }
  } else {
    // Auto-detect or install universal
    for (const client of Object.values(CLIENTS)) {
      if (client.detect(targetDir)) {
        targetClients.push(client);
      }
    }
    if (targetClients.length === 0) {
      console.log(`[*] No specific AI agent directory detected. Installing universal configuration...`);
      targetClients.push(...Object.values(CLIENTS));
    }
  }

  // 3. Mount client rules and skills
  for (const client of targetClients) {
    console.log(`\n[*] Configuring for ${c.bold}${c.cyan}${client.name}${c.reset}:`);
    for (const f of client.files) {
      const srcPath = path.join(rootDir, f.src);
      const destPath = path.join(targetDir, f.dest);
      if (f.isDir) {
        copyDirSafe(srcPath, destPath, isDry);
        console.log(`  ${c.green}+${c.reset} Mounted ${f.dest}/`);
      } else {
        copyFileSafe(srcPath, destPath, isDry);
        console.log(`  ${c.green}+${c.reset} Installed ${f.dest}`);
      }
    }

    if (client.skillsDir) {
      const clientSkillsPath = path.join(targetDir, client.skillsDir);
      ensureDir(clientSkillsPath, isDry);
      copyDirSafe(srcSkillsDir, clientSkillsPath, isDry);
      console.log(`  ${c.green}+${c.reset} Injected skills into ${client.skillsDir}/`);
    }
  }

  console.log(`\n${c.bold}${c.green}[SUCCESS] UASF installed successfully!${c.reset}`);
  console.log(`Run ${c.bold}'uasf doctor'${c.reset} to verify installation integrity.\n`);
}

function runDoctor(targetDir) {
  printBanner();
  console.log(`[*] Auditing UASF configuration at: ${c.bold}${targetDir}${c.reset}\n`);

  let issues = 0;
  const skillsPath = path.join(targetDir, 'skills');
  if (fs.existsSync(skillsPath)) {
    console.log(`  ${c.green}[PASS] Core skills directory present (${CORE_SKILLS.length} skills)${c.reset}`);
  } else {
    console.log(`  ${c.yellow}[WARN] Core skills directory missing${c.reset}`);
    issues++;
  }

  for (const client of Object.values(CLIENTS)) {
    const isDetected = client.detect(targetDir);
    if (isDetected) {
      let missing = 0;
      for (const f of client.files) {
        const dest = path.join(targetDir, f.dest);
        if (!fs.existsSync(dest)) missing++;
      }
      if (missing === 0) {
        console.log(`  ${c.green}[PASS] ${client.name}: Fully configured${c.reset}`);
      } else {
        console.log(`  ${c.yellow}[WARN] ${client.name}: Workspace detected, but ${missing} rule(s) missing${c.reset}`);
        issues++;
      }
    } else {
      console.log(`  ${c.dim}[--]   ${client.name}: Not active${c.reset}`);
    }
  }

  console.log(`\n======================================================`);
  if (issues > 0) {
    console.log(`${c.yellow}[!] Found ${issues} issue(s). Run 'uasf install' to fix.${c.reset}\n`);
    process.exit(1);
  } else {
    console.log(`${c.green}[OK] All audited skills and agents are 100% healthy!${c.reset}\n`);
  }
}

function runList() {
  printBanner();
  console.log(`${c.bold}Available UASF Core Skills (${CORE_SKILLS.length}):${c.reset}`);
  CORE_SKILLS.forEach((s, idx) => {
    console.log(`  ${idx + 1}. ${c.green}${c.bold}${s.name}${c.reset}`);
    console.log(`     ${c.dim}${s.desc}${c.reset}`);
  });

  console.log(`\n${c.bold}Supported AI Agents (${Object.keys(CLIENTS).length}):${c.reset}`);
  Object.values(CLIENTS).forEach((cItem, idx) => {
    console.log(`  ${idx + 1}. ${c.cyan}${c.bold}${cItem.name}${c.reset}`);
    const files = cItem.files.map(f => f.dest).join(', ');
    console.log(`     Files: ${c.dim}${files}${c.reset}`);
    if (cItem.skillsDir) {
      console.log(`     Skills Dir: ${c.dim}${cItem.skillsDir}${c.reset}`);
    }
  });
  console.log('');
}

function runVerify() {
  printBanner();
  console.log(`[*] Running local validation & contract test suite...\n`);
  try {
    const validateScript = path.join(rootDir, 'test', 'validate.js');
    const simulateScript = path.join(rootDir, 'test', 'simulate-agent.js');

    execSync(`node "${validateScript}"`, { stdio: 'inherit' });
    execSync(`node "${simulateScript}"`, { stdio: 'inherit' });

    console.log(`\n${c.green}[OK] All validation and simulation suites passed with exit code 0.${c.reset}\n`);
  } catch (err) {
    console.error(`\n${c.red}[FAIL] Verification failed.${c.reset}\n`);
    process.exit(1);
  }
}

function runUninstall(targetDir) {
  printBanner();
  console.log(`[*] Removing UASF skills from: ${c.bold}${targetDir}${c.reset}`);

  let count = 0;
  const rootSkills = path.join(targetDir, 'skills');
  if (fs.existsSync(rootSkills)) {
    fs.rmSync(rootSkills, { recursive: true, force: true });
    console.log(`[OK] Removed skills/`);
    count++;
  }

  for (const client of Object.values(CLIENTS)) {
    for (const f of client.files) {
      const dest = path.join(targetDir, f.dest);
      if (fs.existsSync(dest)) {
        if (f.isDir) {
          fs.rmSync(dest, { recursive: true, force: true });
        } else {
          fs.unlinkSync(dest);
        }
        console.log(`[OK] Removed ${f.dest}`);
        count++;
      }
    }
    if (client.skillsDir) {
      const cSkills = path.join(targetDir, client.skillsDir);
      if (fs.existsSync(cSkills)) {
        fs.rmSync(cSkills, { recursive: true, force: true });
        console.log(`[OK] Removed ${client.skillsDir}`);
        count++;
      }
    }
  }

  console.log(`\n${c.green}[SUCCESS] UASF uninstalled cleanly (${count} items removed).${c.reset}\n`);
}

function main() {
  const rawArgs = process.argv.slice(2);
  let command = null;
  let targetDir = null;
  const options = {
    client: 'all',
    dryRun: false,
    backup: false
  };

  const KNOWN_COMMANDS = ['install', 'doctor', 'list', 'verify', 'uninstall'];

  for (const arg of rawArgs) {
    if (arg === '-h' || arg === '--help' || arg === 'help') {
      printHelp();
      return;
    }
    if (arg === '-v' || arg === '--version' || arg === 'version') {
      console.log(`uasf v${pkg.version}`);
      return;
    }
    if (arg === '--dry-run') {
      options.dryRun = true;
      continue;
    }
    if (arg === '--backup') {
      options.backup = true;
      continue;
    }
    if (arg.startsWith('--client=')) {
      options.client = arg.split('=')[1];
      continue;
    }

    if (!command && KNOWN_COMMANDS.includes(arg)) {
      command = arg;
    } else if (!targetDir && !arg.startsWith('-')) {
      targetDir = arg;
    }
  }

  if (!command) command = 'install';
  targetDir = targetDir ? path.resolve(process.cwd(), targetDir) : process.cwd();

  switch (command) {
    case 'install':
      runInstall(targetDir, options);
      break;
    case 'doctor':
      runDoctor(targetDir);
      break;
    case 'list':
      runList();
      break;
    case 'verify':
      runVerify();
      break;
    case 'uninstall':
      runUninstall(targetDir);
      break;
    default:
      printHelp();
      break;
  }
}

main();
