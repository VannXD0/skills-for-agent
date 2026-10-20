---
name: uasf-anti-slop
description: Enforces human-authored verbal standards and pre-delivery design review gates scoring typography, contrast, and layout asymmetry.
triggers:
  - anti-slop
  - design review
  - clean copy
  - ui quality
---

# Style & Anti-Slop Contract

Eliminates characteristic AI verbal and visual artifacts across all generated outputs.

## Verbal Anti-Slop
- Banned phrases: *"Certainly!"*, *"Here is..."*, *"Hope this helps!"*, *"It is important to remember..."*, *"In today's fast-paced world..."*.
- Banned structures: Formulaic 3-bullet parallel summaries, repetitive em-dash pauses, empty concluding pleasantries.
- Zero restatement: Never repeat or paraphrase the user's prompt.

## App/Web Design Review Gate
Every generated frontend application or website must score >= 9/10 on the self-audit checklist:
1. **Typography Check:** Bespoke, characterful font scale (`JetBrains Mono`, `Inter Var`, `Geist`, `Fira Code`).
2. **Color Restraint:** High-contrast palette with at most one sharp accent. Strictly ban generic AI purple-blue gradients (`linear-gradient(#6366f1, #8b5cf6)`).
3. **Layout Asymmetry:** Intentional focal hierarchy and asymmetric cadence; avoid uniform 24px card grids.
4. **Copy Authenticity:** Purpose-written, concrete microcopy (e.g. "Delete 4 cached nodes" vs "Empower your workflow").
