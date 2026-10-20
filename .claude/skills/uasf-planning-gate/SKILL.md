---
name: uasf-planning-gate
description: Generates step-by-step roadmap in plan.md and halts execution until explicit operator confirmation.
triggers:
  - planning gate
  - plan first
  - roadmap
  - confirmation
---

# Planning Gate & Execution Discipline

Enforces deterministic verification prior to destructive or multi-phase actions.

## Protocol
1. **Halts After Discovery:** Stop after problem analysis to generate a discrete, numbered roadmap.
2. **Plain Markdown Format:** Output plan to a plain `plan.md` file in the project folder. Never trigger native review popups or auto-approval loops.
3. **Confirmation Suspension:** Execution halts until the operator emits an explicit confirmation token:
   - Tokens: `go`, `gas`, `proceed`, `y`, `yes`, `approve`.
4. **Direct Execution:** Upon confirmation, execute tasks in order without conversational fluff.
