<div align="center">

# Universal AI Skill Framework (UASF)

**Standardized Multi-Agent Protocols & Skills for Autonomous AI Coding Agents**

[![CI & Skills Verification](https://img.shields.io/badge/Verification-Passing-brightgreen.svg)](#verification--testing)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)
[![Compatible With](https://img.shields.io/badge/Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor%20%7C%20Codex%20%7C%20Windsurf%20%7C%20Copilot-orange.svg)](#supported-agents)

*Zero external binaries. 100% portable markdown instructions, surgical APK reverse engineering, deterministic instruction reconciliation, and anti-slop design gates.*

---

[Quickstart](#quickstart) • [Why UASF?](#why-universal-ai-skill-framework) • [Architecture](#architecture) • [Core Skills](#core-skills) • [Supported Agents](#supported-agents) • [Verification](#verification--testing)

</div>

---

## Why Universal AI Skill Framework?

Autonomous coding agents (Claude Code, Cursor, Antigravity, OpenAI Codex, Windsurf) fail predictably due to four structural pitfalls:

| Failure Mode | Without UASF | With UASF Skills |
| :--- | :--- | :--- |
| **Instruction Collisions** | Ambiguous rule precedence; plugins hijack host rules and user directives randomly. | **Deterministic Hierarchy**: Strict 5-tier ladder (`Operator > Safety Floor > UASF Core > External Skills > Profile`). |
| **Destructive Reverse Engineering** | Overhauls XML themes and layouts when unlocking features, destroying app authenticity. | **Zero-UI Invariant**: Surgical `.smali` and Frida patches with byte-for-byte identical UI resources. |
| **AI Slop & Cliché UIs** | Symmetrical card grids, purple-blue gradients, and generic copy (*"Empower your workflow"*). | **Design Review Gate**: Enforces bespoke typography (JetBrains Mono/Inter), high-contrast slate palettes, and asymmetric layouts. |
| **Conversational Filler** | Starts every turn with *"Certainly!"*, *"Hope this helps!"*, and repetitive em-dash pauses. | **Anti-Slop Verbal Contract**: Hard heuristic filtering eliminating empty pleasantries and restatements. |
| **Shallow First Drafts** | Rushes into broken multi-file edits without analyzing memory or complexity trade-offs. | **Deep-Reasoning Mandate**: Pre-execution problem formulation and trade-off matrices before non-trivial action. |

---

## Quickstart

Install UASF into any existing project in 3 seconds:

### Via NPX (Direct from GitHub)

Run instantly without cloning or local installation:

```bash
# Run directly from GitHub repository
npx github:VannXD0/uasf

# Or install into current project
npx github:VannXD0/uasf install
```

### CLI Commands & Advanced Flags

The zero-dependency CLI auto-detects active agents in the project:

```bash
# Universal install into current project (auto-detects active agents)
npx github:VannXD0/uasf install

# Install into a specific directory
npx github:VannXD0/uasf install /path/to/project

# Filter installation to a specific AI agent:
# Options: antigravity, claude, cursor, codex, windsurf, omp, gemini, aider, copilot
npx github:VannXD0/uasf install ./my-project --client=antigravity

# Preview file operations without modifying disk
npx github:VannXD0/uasf install ./my-project --dry-run

# Audit project configuration and verify skill health
npx github:VannXD0/uasf doctor ./my-project

# Run multi-agent contract verification test suite
npx github:VannXD0/uasf verify

# List all core skills and supported AI agent platforms
npx github:VannXD0/uasf list

# Safely remove UASF skills without touching user code
npx github:VannXD0/uasf uninstall ./my-project
```

### One-Line Shell Installers

#### Linux / macOS:
```bash
curl -fsSL https://raw.githubusercontent.com/VannXD0/uasf/main/install.sh | bash
```

#### Windows (PowerShell):
```powershell
irm https://raw.githubusercontent.com/VannXD0/uasf/main/install.ps1 | iex
```

---

## Architecture

```
                                  +---------------------------------------+
                                  |            Operator Input             |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |   Intent Detection & Auto-Trigger     |
                                  |       (Confidence C >= 0.72)          |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  | Instruction Reconciliation Engine     |
                                  | (Operator > Host > UASF Core > Ext)   |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |  Deep-Reasoning & Trade-off Engine    |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |   Planning Gate (Pause & Confirm)     |
                                  +---------------------------------------+
                                                      | (Upon Approval)
                         +----------------------------+---------------------------+
                         |                                                        |
                         v                                                        v
        +----------------------------------+                    +----------------------------------+
        | APK Analysis & Patch Module      |                    | App/Web Design Review Gate       |
        | - Smali Logic / Frida Script     |                    | - Anti-Slop Contract Validation  |
        | - Strict Zero-UI Alteration      |                    | - Heuristic Craft Evaluation     |
        +----------------------------------+                    +----------------------------------+
                         |                                                        |
                         +----------------------------+---------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  | Style Contract & Output Filtering     |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |            Operator Output            |
                                  +---------------------------------------+
```

---

## Core Skills

| Skill | Category | Description |
| :--- | :--- | :--- |
| `uasf-apk-patcher` | Reverse Engineering | Decompiles APKs, discovers boolean gates (`isVip()`), synthesizes smali & Frida patches under strict **Zero-UI** invariant. |
| `uasf-instruction-reconciler` | Governance | Enforces deterministic 5-tier instruction hierarchy and resolves rule collisions. |
| `uasf-anti-slop` | Style & Design | Heuristic audit eliminating conversational bot filler and scoring UIs for typography, asymmetry, and color restraint. |
| `uasf-deep-reasoning` | Architecture | Mandatory problem formulation and trade-off matrices before executing non-trivial operations. |
| `uasf-planning-gate` | Execution | Emits roadmaps to `plan.md` and pauses for confirmation (`gas`, `go`, `proceed`). |
| `uasf-learning-loop` | Memory | Ephemeral in-session memory and encrypted persistent local profile (`uasf_profile.json`). |
| `emil-design-eng` | Design Engineering | Physics-based transition curves (`cubic-bezier(0.16, 1, 0.3, 1)`), micro-interactions, and state boundaries. |
| `taste-skill` | Aesthetics | Curated typography, chromatic restraint, and optical hierarchy. |
| `impeccable` | Craft | Clean module boundaries, single responsibility, and zero dead code. |
| `baseline-ui` | Accessibility | WCAG 2.1 AA contrast compliance, keyboard focus rings, and semantic HTML5. |

---

## Supported Agents

UASF automatically maps to every major coding agent:

| Agent / Client | Config Path | Integration Method |
| :--- | :--- | :--- |
| **Google Antigravity** | `AGENTS.md`, `.agent/skills/` | Native Antigravity skill system and agent rules |
| **Claude Code** | `CLAUDE.md`, `.claude/commands/`, `.claude/skills/` | Commands (`/uasf`) and workspace rules |
| **Cursor** | `.cursorrules`, `.cursor/rules/uasf.mdc` | Project rules and MDC always-apply instructions |
| **Windsurf** | `.windsurfrules` | Workspace rules and memory directives |
| **OpenAI Codex** | `CODEX.md` | System directives and instruction hierarchy |
| **Oh My Pi (omp)** | `PI.md`, `.omp/skills/`, `.omp/commands/` | Native CLI commands and skill engine |
| **Gemini CLI** | `GEMINI.md` | Context guidelines and operating rules |
| **Aider** | `.aider.conf.yml`, `.aider/CONVENTIONS.md` | Auto-loaded configuration and conventions |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Repository-wide custom instructions |

---

## Verification & Testing

Automated verification suite validating all manifests, platform entrypoints, frontmatter schemas, and agent contract simulations:

```bash
npm test
```

Expected output:
```
--- 1. Validating package.json & Manifests ---
PASS: package.json is valid JSON
--- 2. Validating Platform Entrypoints & Root Files ---
PASS: All platform rules and entrypoints exist
--- 3. Validating Core Skills Structure & Frontmatter ---
PASS: All 10 skills verified with valid frontmatter

All structural checks passed!

=== Running UASF Multi-Agent Contract Simulation Tests ===
PASS: Tier 3 UASF Zero-UI Invariant overrides Tier 4 External Skill
PASS: Anti-slop verbal filter detects bot pleasantries
PASS: Planning gate confirmation tokens verified

All agent simulation tests passed cleanly!
```

---

## License

[MIT](LICENSE) (c) [VannXD0](https://github.com/VannXD0)
