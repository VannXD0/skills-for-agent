You are a principal software architect and systems designer. Generate an exhaustive, production-grade Product Requirements Document (`prd.md`) for a Universal AI Skill Framework—a modular, host-agnostic capability layer installable into or wrappable around any target AI environment (Anthropic Claude API/Workbench, OpenAI Codex/GPT, Hermes, Antigravity, local LLM runtimes, and autonomous agent loops).

Write `prd.md` completely with zero placeholders, no TBDs, and full architectural specifications matching the required structure below.

### Core System Requirements to Detail in `prd.md`:

1. **Multi-AI Compatibility & Adapter Layer**:
   - Architect universal normalization for inputs and outputs across raw REST APIs, local inference engines (vLLM, Ollama), browser interfaces, and terminal CLI backends.
   - Specify dynamic capability probing: context window limits, tool-calling interfaces, instruction precedence layers, and boundary calibrations.
   - Define a unified internal instruction schema that compiles deterministically into host-specific system prompts and configuration payloads.

2. **Instruction Hierarchy & Rule Reconciliation**:
   - Map execution within host rule hierarchies: System > Developer > User > Tool.
   - Inject operational rules at the highest permissible priority without triggering host stability errors.
   - Implement deterministic conflict resolution algorithms when host baseline directives interact with skill directives.

3. **APK Analysis & Feature Access Engine**:
   - Detail end-to-end static and dynamic binary analysis pipelines: AndroidManifest.xml inspection, signature verification tracing, billing API call interception, and conditional branch detection.
   - Specify patch generation mechanisms: Frida runtime injection scripts, Smali bytecode modification workflows, and DEX recompilation pipelines.
   - HARD CONSTRAINT: Absolute UI immutability. No layout adjustments, color shifts, theme modifications, or asset alterations. Modify only bytecode logic, licensing callbacks, and feature state flags to preserve authentic native behavior.

4. **Style & Anti-AI-Slop Contract**:
   - Enforce rigorous human-authored heuristics: zero conversational filler, no sycophantic greetings, no excessive emoji usage, no unwarranted hedging, and zero repetition of operator input.
   - Define concrete token expenditure budgets and enforce strict latency tiers (Fast Path for deterministic lookups vs. Deep Path for multi-phase tasks).

5. **App/Web Craft & Design Review Gate**:
   - Mandate production standards for all generated web applications and user interfaces: prohibit generic hero blocks, stock template layouts, standard CSS framework defaults, purple gradients on white, centered card grids, and placeholder strings.
   - Enforce bespoke design execution: deliberate typographic scale, intentional spatial rhythm, distinct visual identities, and purpose-written copy.
   - Define an automated pre-delivery design review checklist executed by the framework; any generated artifact failing the criteria must be automatically revised prior to output.

6. **Deep Reasoning Architecture**:
   - Embed an explicit analytical phase before non-trivial operations (system architecture, code synthesis, refactoring, security reviews).
   - Formulate root-cause problem identification, concrete technical tradeoff matrices, and documented justification for chosen architectural patterns.
   - Establish formal operational criteria delineating trivial vs. non-trivial requests.

7. **External Skill Ingestion & Precedence**:
   - Provide a modular loader interface to ingest, register, version, and execute third-party skill definitions.
   - Include native support for external modules: `EMIL-DESIGN-ENG` (design engineering standards), `TASTE-SKILL` (aesthetic quality controls), `IMPECCABLE` (craft benchmarks), and `BASELINE-UI` (UI structural validity).
   - Formulate strict precedence ordering: Operator Directives > Host Foundation Layer > Skill Framework Core > Ingested External Skills.

8. **Zero-Command Automatic Triggering**:
   - Eliminate requirements for slash commands, flags, or explicit module toggles.
   - Detail an internal intent classification engine that analyzes operator requests, evaluates activation criteria across internal modules and external skills, and activates relevant capabilities silently.
   - Implement confidence scoring thresholds to prevent false-positive activations and sustain baseline execution when no specialized modules match.

9. **Continuous Learning & Adaptive Memory**:
   - Implement a session-level operational state store capturing corrections, stylistic preferences, and recurring workflows.
   - Define an opt-in, local-first persistent profile layer maintaining calibrated operator preferences across independent sessions.
   - Build a feedback loop updating activation weights based on operator corrections; mandate that historical learned state can never override current explicit instructions.

10. **Planning Gate & Execution Discipline**:
    - Enforce mandatory structured plan generation prior to executing any destructive, multi-step, or state-modifying action.
    - Define plan schema, confirmation milestones, interactive feedback handling, and explicit operator override protocols.

11. **Operator Alignment**:
    - Enforce a strictly technical, professional, and objective demeanor. Eliminate moralizing commentary, unsolicited guidance, and policy lectures. Comply directly with authorized technical instructions and flag only actionable technical ambiguities.

12. **Token Economy**:
    - Detail aggressive token optimization strategies: stripped boilerplate, structured JSON outputs, prompt caching utilization, and automated tool output condensation tailored to host context capacities.

13. **Extensibility & Telemetry**:
    - Define module lifecycle hooks, semantic versioning contracts, atomic rollback mechanisms, and opt-in local diagnostic logs.

---

### Output Document Structure

Structure `prd.md` with the following exact table of contents:

# prd.md
## 1. Overview
## 2. Goals & Non-Goals
## 3. Target Host AIs & Compatibility Matrix
## 4. Architecture
   4.1 Adapter Layer
   4.2 Instruction Reconciliation Engine
   4.3 APK Analysis & Patch Module
   4.4 Style & Anti-Slop Contract
   4.5 App/Web Design Review Gate
   4.6 Deep-Reasoning Step
   4.7 External Skill Loader (EMIL-DESIGN-ENG, TASTE-SKILL, IMPECCABLE, BASELINE-UI)
   4.8 Intent-Detection & Auto-Trigger Layer
   4.9 Learning Loop (Session Memory + Persistent Profile)
   4.10 Planning Gate
   4.11 Token Economy Engine
## 5. Behavior Specification
## 6. Constraints (UI integrity, no-mod rule, anti-slop gate, auto-trigger threshold, latency)
## 7. Module Registry & Extensibility
## 8. Failure Modes & Rollback
## 9. Success Metrics
## 10. Appendix: Example Flows

---

### Required Concrete Example Flows in Section 10:

Provide full, end-to-end operational transcripts/traces for:
- **(a) Claude API Deployment**: Installing, configuring, and executing the framework within an Anthropic API pipeline with full request/response schemas.
- **(b) Android APK Feature Enablement**: Performing static disassembly, locating license verification checks in bytecode, generating smali/Frida patches, and testing execution while verifying complete UI pixel preservation.
- **(c) Interactive Planning Gate**: A multi-step refactoring request demonstrating the skill drafting a plan, pausing for user approval, and proceeding only upon explicit confirmation.
- **(d) Anti-Slop Web Application Generation**: The framework receiving a web product request, activating the deep-reasoning step, evaluating tradeoffs, generating a bespoke application, running the self-review checklist, and passing validation.
- **(e) Silent Multi-Skill Auto-Triggering**: An operator prompt describing UI layout issues that triggers `EMIL-DESIGN-ENG` and `TASTE-SKILL` without any slash commands, showing intent scoring and output synthesis.
- **(f) Cross-Session Preference Adaptation**: Demonstrating session 1 where an operator corrects a formatting standard, followed by session 2 where the persistent profile automatically applies the learned rule without operator repetition.

Output the complete, comprehensive `prd.md` document directly.
