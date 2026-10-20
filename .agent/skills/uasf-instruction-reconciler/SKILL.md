---
name: uasf-instruction-reconciler
description: Enforces the 5-tier instruction priority ladder and resolves policy collisions deterministically.
triggers:
  - instruction precedence
  - rule conflict
  - priority ladder
  - override
---

# Instruction Reconciliation Engine

Enforces absolute stability in rule precedence across host environments, internal rules, and external plugins.

## Priority Ladder
1. **Tier 1 (Highest): Explicit Current Operator Directive** — Immediate prompt overrides all non-hard-wall behavior.
2. **Tier 2: Host Safety Floor** — Irrevocable system constraints (e.g. preventing catastrophic harm).
3. **Tier 3: UASF System Invariants** — Anti-slop constraints, zero-UI APK modification rule, planning gate integrity.
4. **Tier 4: Third-Party External Skills** — Directives from imported skills (`emil-design-eng`, `taste-skill`, etc.).
5. **Tier 5: Learned Profile Tendencies** — Historical cross-session learned preferences.

## Conflict Resolution Rules
- If an external skill demands visual redesign during an APK unlock, Tier 3 unconditionally suppresses Tier 4.
- If an explicit operator directive contradicts a historical learned tendency, Tier 1 overrides Tier 5.
