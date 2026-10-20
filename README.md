# Universal AI Skill Framework (UASF)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Platform: Windows | Linux | macOS](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-green)](#installation)

Modular, runtime-agnostic capability engine designed to wrap around or install directly into any host Artificial Intelligence model or agentic harness (Claude, Codex, Hermes, Antigravity, local LLM runtimes).

---

## Features

- **Multi-Host Normalization:** Adapters for Claude (Anthropic), OpenAI Codex / GPT-4o, Hermes / vLLM, Ollama, and Antigravity.
- **Deterministic Instruction Hierarchy:** Enforces `Operator Directive > Safety Floor > UASF Core System Rules > External Skills > Learned Profile`.
- **Surgical APK Analysis & Patching:** Bytecode patching (`.smali`) and Frida dynamic hook generation under strict **Zero-UI-Alteration** invariant.
- **App/Web Anti-Slop Design Review Gate:** Automated pre-delivery audit scoring typography, asymmetric whitespace, color restraint (no purple gradients), and authentic microcopy.
- **Ambient Autonomy (Zero Slash Commands):** Semantic intent classification with confidence activation threshold ($C \ge 0.72$).
- **Deep-Reasoning Step:** Mandatory problem formulation and trade-off matrices before non-trivial execution.
- **Continuous Learning Loop:** Ephemeral in-session memory and encrypted persistent local profile (`uasf_profile.json`).

---

## Installation

### Terminal (Windows / Linux / macOS)

#### Method 1: Direct Pip Install
```bash
# Clone the repository
git clone https://github.com/VannXD0/uasf.git
cd uasf

# Install in user mode (or virtualenv)
pip install .
```

#### Method 2: One-Liner Script Install
- **Linux / macOS:**
  ```bash
  chmod +x install.sh && ./install.sh
  ```
- **Windows (PowerShell):**
  ```powershell
  powershell -ExecutionPolicy Bypass -File .\install.ps1
  ```

---

## CLI Usage

Verify installation:
```bash
uasf modules
```

Run prompt through UASF state machine:
```bash
uasf run "Analyze APK license check and generate smali patch" --confirm
```

Audit frontend HTML/CSS against Anti-Slop criteria:
```bash
uasf audit-design preview.html
```

Inspect or add rules to persistent learning profile:
```bash
uasf profile
uasf profile --add-rule naming "Always use snake_case for Python functions"
```

Run test suite:
```bash
python -m unittest uasf.test_suite
```

---

## License

MIT License.
