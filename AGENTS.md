# Universal AI Skill Framework (UASF) for Google Antigravity

This repository implements the Universal AI Skill Framework (UASF) specification. All agents operating within this workspace must adhere to the rules below.

## Antigravity Operating Rules

- **Instruction Hierarchy:** Follow the 5-tier priority ladder in [base-rules.md](base-rules.md).
- **Mode Discipline:** Multi-step plans must be written to a plain `plan.md` file. Do not use native plan system triggers (`task_boundary`, `notify_user`, `implementation_plan.md`).
- **Anti-Slop Discipline:** Eliminate conversational filler and generic purple-blue gradients. Every UI artifact must score >= 9/10 on the design review rubric.
- **Surgical APK Modifications:** Strictly preserve UI layouts, themes, and drawables byte-for-byte. Patches apply only to bytecode logic (`.smali` / `.dex`) and runtime hooks.
- **Ambient Autonomy:** Read user prompts and activate relevant skills silently when confidence >= 0.72. No slash commands required.

## Available Skills in Workspace
See `.agent/skills/` or `skills/` for:
- `uasf-apk-patcher`
- `uasf-instruction-reconciler`
- `uasf-anti-slop`
- `uasf-deep-reasoning`
- `uasf-planning-gate`
- `uasf-learning-loop`
- `emil-design-eng`
- `taste-skill`
- `impeccable`
- `baseline-ui`
