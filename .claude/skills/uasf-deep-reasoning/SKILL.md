---
name: uasf-deep-reasoning
description: Mandatory pre-execution analytical phase formulating root causes, trade-off matrices, and technical justifications.
triggers:
  - deep reasoning
  - architecture
  - trade-off matrix
  - non-trivial
---

# Deep-Reasoning Protocol

Enforces root-cause analysis and trade-off enumeration before executing non-trivial operations.

## Criteria for Non-Trivial Tasks
- Multi-tier software architecture or component restructuring.
- Multi-file source code modifications.
- Binary reverse engineering and decompilation.
- Complex system design or database schema migrations.

## Required Analytical Phases
1. **Core Problem Formulation:** Identify the actual technical bottleneck underneath the request.
2. **Trade-Off Matrix:** Formulate at least two viable implementation trajectories, explicitly evaluating:
   - Memory footprint implications.
   - Algorithmic and structural complexity.
   - Latency and throughput profiles.
3. **Trajectory Selection:** Select the optimal path with technical justification prior to emission.
