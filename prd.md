# Universal AI Skill Framework (UASF) — Product Requirement Document (PRD)

**Document Version:** 1.0.0  
**Target Environment:** Multi-Host AI Run-time Layer (Claude, OpenAI Codex / GPT-4o, Hermes / Open-Weight LLMs, Antigravity, Custom Autonomous Agents)  
**Classification:** Core System Architecture Specification  
**Status:** Approved for Implementation  

---

## 1. Overview

The **Universal AI Skill Framework (UASF)** is a modular, runtime-agnostic capability engine designed to wrap around or install directly into any host Artificial Intelligence model or agentic harness. Current AI agent extensions suffer from vendor lock-in, brittle system-prompt hacking, slash-command fatigue, shallow reasoning loops, and characteristic "AI-slop" in code, text, and interface generation.

UASF provides an ambient, autonomous operating system for AI agents. It intercepts user intent, aligns runtime instruction hierarchies, injects specialized engineering modules (including automated APK reverse engineering and surgical feature unlocking), enforces strict anti-slop visual and verbal contracts, seamlessly nests third-party design disciplines, and maintains continuous session-to-session memory without requiring explicit command invocation or degrading host safety floors.

---

## 2. Goals & Non-Goals

### 2.1 Goals
- **Host Agnosticism:** Seamless deployment across API backends (Anthropic, OpenAI), local inference runtimes (vLLM, Ollama, llama.cpp), web/browser wrappers, and developer IDE agents (Antigravity).
- **Deterministic Instruction Reconciliation:** Absolute stability in rule precedence (`Operator Explicit Directive > Host Safety Floor > UASF Core System Rules > External Skills`).
- **Surgical APK Feature Unlocking:** Fully automated static and dynamic decompilation, license-gate discovery, and bytecode patch generation (Smali / Frida) under a strict **Zero-UI-Alteration** invariant.
- **Ambient Autonomy (Zero Slash Commands):** Dynamic semantic intent classification that silently activates specialized modules only when contextual relevance crosses activation thresholds.
- **Human-Crafted Output Enforcement:** Hard design gates eliminating standard AI stylistic tells (purple gradients, generic hero sections, predictable symmetrical grids, filler copywriting).
- **Deep-Reasoning Mandate:** Enforced root-cause analysis, trade-off enumeration, and explicit planning checkpoints prior to non-trivial execution.
- **Continuous Learning Loop:** Ephemeral in-session preference synthesis and encrypted local cross-session profile adaptation.

### 2.2 Non-Goals
- **Replacing Host Safety Mechanisms:** UASF does not disable kernel-level safety filters of the host LLM; it operates within authorized developer and research environments.
- **UI Redesign during APK Unlocks:** UASF explicitly forbids aesthetic, theme, or layout overhauls when performing bytecode patching on target binaries.
- **Monolithic Bundling:** UASF is not a single giant prompt; it is an orchestrated pipeline of modular interceptors, schemas, and runtime hooks.

---

## 3. Target Host AIs & Compatibility Matrix

| Host Environment | Runtime Mechanism | Context Window Strategy | Tool Calling Protocol | Injection Tier |
| :--- | :--- | :--- | :--- | :--- |
| **Anthropic Claude 3.5 / 3.7** | REST API / Claude Code CLI | Dynamic Sliding Window (cache control at 8k/32k breakpoints) | Native Tools (`tools` array) | System Prompt Parameter + Pre-fill Hook |
| **OpenAI GPT-4o / Codex** | REST API / Assistants API | Token Bucket Truncation (head 20% preserved, tail 80% sliding) | Function Calling (`tools` schema) | Developer / System Message |
| **Antigravity (AGY)** | IDE Extension / Native Subagent | Session-Persistent Brain Store + Artifact Directory | Native Tools (`run_command`, `read_file`, `write_file`) | Workspace Rules (`.agents/rules`) + Global Skill Config |
| **Hermes / Open-Weight (vLLM)** | OpenAI-compatible HTTP / CLI | Context Compaction via Selective KV Cache eviction | Structured JSON Output / Custom Parser | System Tag Prefill (`<|im_start|>system`) |
| **Local CLI Runners (Ollama)** | Native Stdout/Stdin Streaming | Hard Context Budget (4k/8k conservative limits) | Regex Action Tags (`[TOOL_CALL: ...]`) | Base System Template Injection |

---

## 4. Architecture

```
                                  +---------------------------------------+
                                  |            Operator Input             |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  | 4.8 Intent Detection & Auto-Trigger   |
                                  +---------------------------------------+
                                                      |
                         +----------------------------+---------------------------+
                         |                                                        |
                         v                                                        v
       [Context Match: Skill Auto-Activated]                    [No Match: Baseline Mode]
                         |                                                        |
                         +----------------------------+---------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  | 4.2 Instruction Reconciliation Engine |
                                  | (Operator > Host > UASF Core > Ext)   |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  | 4.9 Learning Loop: Profile Injection  |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  | 4.6 Deep-Reasoning & Trade-off Engine |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  | 4.10 Planning Gate (Pause/Confirm)    |
                                  +---------------------------------------+
                                                      | (Upon Approval)
                         +----------------------------+---------------------------+
                         |                                                        |
                         v                                                        v
        +----------------------------------+                    +----------------------------------+
        | 4.3 APK Analysis & Patch Module  |                    | 4.5 App/Web Design Review Gate   |
        | - Smali Logic / Frida Script     |                    | - Anti-Slop Contract Validation  |
        | - Strict Zero-UI Alteration      |                    | - Heuristic Craft Evaluation     |
        +----------------------------------+                    +----------------------------------+
                         |                                                        |
                         +----------------------------+---------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  | 4.4 Style Contract & Output Filtering |
                                  +---------------------------------------+
                                                      |
                                                      v
                                  +---------------------------------------+
                                  |            Operator Output            |
                                  +---------------------------------------+
```

### 4.1 Adapter Layer
Normalizes heterogeneous LLM I/O into a unified abstract runtime model:
- **Capability Discovery:** Queries host metadata at bootstrap (`model_id`, max context length, tool presence, streaming support).
- **Instruction Translator:** Converts UASF internal operational schemas into target-specific framing (e.g., Anthropic XML tags `<uasf_context>`, OpenAI developer roles, or ChatML delimiters).
- **I/O Sanitizer:** Strips vendor-specific metadata tags before surfacing responses to the operator.

### 4.2 Instruction Reconciliation Engine
Enforces a deterministic priority ladder when internal, external, or host policies collide:
1. **Tier 1 (Highest): Explicit Current Operator Directive** — Immediate prompt overrides all non-hard-wall behavior.
2. **Tier 2: Host Safety Floor** — Irrevocable system constraints (e.g., prohibition of catastrophic physical harm).
3. **Tier 3: UASF System Invariants** — Anti-slop constraints, zero-UI APK modification rule, planning gate integrity.
4. **Tier 4: Third-Party External Skills** — Directives from imported libraries (`EMIL-DESIGN-ENG`, `TASTE-SKILL`, etc.).
5. **Tier 5: Learned Profile Tendencies** — Historical cross-session learned preferences.

*Conflict Resolution Protocol:* If an external skill demands a visual overhaul while performing an APK patch, Tier 3 unconditionally suppresses Tier 4, preserving the target's original visual layout intact.

### 4.3 APK Analysis & Patch Module
A dedicated reverse-engineering subsystem tailored for Android applications:
- **Static Ingestion:** Decompiles target `.apk` using automated pipelines (`apktool`, `baksmali`, JADX API).
- **Surface Mapping:**
  - Manifest Analysis: Inspects activities, services, intent filters, and exported flags.
  - License Vector Tracing: Searches call graphs for licensing APIs (Google Play In-App Billing v3/v4/v5, Supabase/Firebase subscription validators, custom cryptographic signature checks).
  - Feature-Gate Enumeration: Identifies boolean gate checks (`isVip()`, `hasActiveSubscription()`, `checkLicense()`).
- **Bytecode Patch Synthesis:**
  - Produces surgical smali edits (e.g., swapping `if-eqz` to `goto`, forcing `const/4 v0, 0x1` returns).
  - Generates zero-footprint runtime Frida hooks (`Java.use(...)` implementation overhauls).
- **HARD CONSTRAINT — Zero UI Modification:**
  - `res/layout/`, `res/values/`, `res/drawable/`, and Android manifest themes **must remain byte-for-byte identical** except where service bindings strictly mandate edits.
  - No rebranding, no injected watermarks, no layout restyling. Output must be indistinguishable from an authentic, human-engineered software build.

### 4.4 Style & Anti-Slop Contract
Defines human-authored linguistic standards across all generated text:
- **Banned Conversational Slop:** Eliminates phrases such as *"Certainly!"*, *"Here is..."*, *"Hope this helps!"*, *"It is important to remember..."*, *"In today's fast-paced world..."*, and generic concluding pleasantries.
- **Structural Anti-Symmetry:** Eliminates formulaic three-bullet summaries, symmetrical parallel sentences, and repetitive em-dash pauses.
- **Latency & Path Tiers:**
  - *Fast Path (< 1.5s TTFT):* Direct CLI commands, single file reads, status verifications.
  - *Deep Path (Extended Deliberation):* Architectural plans, reverse-engineering call-graph traces, full stack generation.

### 4.5 App/Web Design Review Gate
An automated pre-delivery heuristic audit that every frontend artifact must pass before presentation:
- **Design Review Checklist (Self-Audited Gate):**
  1. *Typography Check:* Does the app use a deliberate, characterful font pairing rather than standard system sans-serif defaults?
  2. *Color Restraint Check:* Is the color palette anchored around high-contrast intention with at most one sharp accent, strictly avoiding AI-signature purple-blue gradients?
  3. *Layout Asymmetry:* Does the whitespace create intentional focus, avoiding perfectly uniform 24px padding grids?
  4. *Copy Authenticity:* Is microcopy context-specific and sharp (e.g., "Delete 4 cached nodes" vs "Empower your workflow")?
- **Enforcement:** If an automated self-audit scores the generated UI below 9/10 on the craft rubric, the generator halts output and triggers an internal rewrite prior to user rendering.

### 4.6 Deep-Reasoning Step
Before executing non-trivial operations (defined as: creating multi-tier software architectures, multi-file source code modifications, complex reverse engineering, or system design specifications):
1. **Core Problem Formulation:** Define the actual technical bottleneck underneath the operator's prompt.
2. **Trade-Off Matrix:** Formulate at least two viable implementation trajectories, explicitly noting memory, complexity, and latency implications.
3. **Trajectory Selection:** Select the optimal path with technical justification prior to emission.

### 4.7 External Skill Loader
A standardized dynamic plugin ingestion engine supporting foreign capability packs:
- **Default Core Integrations:**
  - `EMIL-DESIGN-ENG`: High-fidelity interaction design, transition physics, micro-interactions.
  - `TASTE-SKILL`: Visual aesthetic curation, visual tension, chromatic balance.
  - `IMPECCABLE`: Code craft, clean boundary interfaces, zero-clutter implementation.
  - `BASELINE-UI`: Fundamental accessibility (a11y), responsive breakpoints, semantic HTML.
- **Registration Manifest:** Standard YAML/JSON schema declaring trigger keywords, required execution context, priority weight, and exported functions.
- **Sandboxed Execution:** External skills cannot modify UASF core reconciliation rules.

### 4.8 Intent-Detection & Auto-Trigger Layer
Eliminates manual slash-command syntax (e.g., `/crack`, `/design`, `/plan`).
- **Semantic Intent Classifier:** Operates an ultra-lightweight keyword and vector-distance evaluation on incoming operator prompts.
- **Trigger Matching Logic:**
  - Calculates confidence score $C \in [0, 1.0]$.
  - Activation Threshold: $C \ge 0.72$ triggers silent skill loading.
  - Ambiguity Guard: If two conflicting skills score between 0.68 and 0.75, the framework falls back to standard conversational clarification rather than misfiring.
- **Zero False-Positive Target:** Generic chatting or trivial questions bypass the skill loader entirely, consuming zero additional token overhead.

### 4.9 Learning Loop (Session Memory + Persistent Profile)
- **In-Session Memory:** Dynamically registers operator corrections (e.g., *"prefer pure C++ over Python"*, *"don't use flexbox here"*). Updates intra-session weights immediately.
- **Persistent Profile (Local Store):** Encrypted local configuration (`uasf_profile.json`) storing recurring project patterns, verified environment paths, and code styling norms.
- **Hard Memory Gate:** Learned tendencies are completely overridden if the operator provides an explicit directive that contradicts previous behavior.

### 4.10 Planning Gate
Enforces deterministic verification prior to destructive or multi-phase actions:
- Every non-trivial task halts after problem discovery to generate a discrete, step-by-step roadmap.
- Plan artifacts are rendered via plain markdown or dedicated workspace files (`plan.md`).
- Execution blocks until operator approval is confirmed.

### 4.11 Token Economy Engine
Optimizes context window longevity and operational costs:
- **Zero Restatement:** Forbids echoing the user's question back to them.
- **Tool-Call Aggregation:** Summarizes lengthy terminal or build outputs into key status codes and fatal error traces rather than replaying multi-megabyte logs.
- **Context Caching Compatibility:** Aligns system prompt blocks to 2,048-token boundaries to maximize Anthropic/OpenAI prompt caching hits.

---

## 5. Behavior Specification

```
STATE 1: IDLE / OBSERVING
  -> Operator inputs prompt.
  -> Run 4.8 Intent Detection.
  -> If intent matches specialized task: Load modules & reconcile via 4.2.
  -> Check 4.9 Profile Store for active operator preferences.

STATE 2: DELIBERATION (Non-trivial task detected)
  -> Execute 4.6 Deep-Reasoning Step internally.
  -> Check if task involves multi-step execution or binary modifications.
  -> If Yes: Transition to STATE 3 (Planning Gate).
  -> If Simple/Trivial: Transition to STATE 4 (Direct Execution).

STATE 3: PLANNING GATE
  -> Emit structured plan.
  -> Suspend execution. Await explicit operator confirmation ("go", "gas", "proceed").

STATE 4: EXECUTION & VALIDATION
  -> If APK Task:
       - Decompile & trace bytecode.
       - Synthesize patch / hook.
       - Validate: Zero modifications to res/, assets/, layout/.
  -> If Web/App Task:
       - Generate code.
       - Execute 4.5 App/Web Design Review Gate self-audit.
       - Regenerate internally if score < 9/10.

STATE 5: EMISSION & AUDIT
  -> Filter output through 4.4 Style Contract (Zero Slop).
  -> Emit pointer and final artifact to operator.
  -> Update 4.9 In-Session Learning Memory with observed feedback.
```

---

## 6. Constraints

1. **UI Integrity Invariant:** Under no circumstances shall an APK feature-unlock task alter, replace, or inject UI resources, themes, colors, or views. Logic patches remain strictly in bytecode (`.dex` / `.smali`) and native libraries (`.so`).
2. **Anti-Slop Hard Gate:** Code with unstyled default cards, purple-blue gradient buttons, or generic filler copy is disqualified from delivery and must be regenerated prior to presentation.
3. **Auto-Trigger Threshold:** Semantic matching confidence must exceed $0.72$ for unprompted skill activation.
4. **Latency Budgets:**
   - Fast Path: Time-to-First-Token $\le 1.5$ seconds.
   - Deep Path (Deliberation): Total turnaround $\le 15$ seconds before plan presentation.

---

## 7. Module Registry & Extensibility

```json
{
  "uasf_registry_version": "1.0.0",
  "modules": [
    {
      "id": "uasf-core-reconcile",
      "version": "1.0.0",
      "type": "kernel",
      "entrypoint": "internal://reconcile"
    },
    {
      "id": "uasf-apk-patcher",
      "version": "2.4.1",
      "type": "feature",
      "triggers": ["apk", "smali", "dex", "frida", "license bypass", "feature gate"],
      "entrypoint": "internal://apk_engine"
    },
    {
      "id": "emil-design-eng",
      "version": "3.1.0",
      "type": "external_skill",
      "source": "npm:@design-eng/skill",
      "triggers": ["frontend", "component", "animation", "layout", "web app"]
    },
    {
      "id": "taste-skill",
      "version": "1.2.0",
      "type": "external_skill",
      "source": "github:curated-craft/taste",
      "triggers": ["visual polish", "typography", "palette", "aesthetic"]
    }
  ]
}
```

---

## 8. Failure Modes & Rollback

| Failure Condition | Diagnostic Signature | System Fallback Action |
| :--- | :--- | :--- |
| **Instruction Conflict Loop** | Repeated contradictory system/skill behaviors | Revert to Tier 1: enforce explicit operator directive, disable all Tier 4 external skills for current turn. |
| **APK Bytecode Verification Failure** | Smali reassembly error or crash on launch | Roll back to untouched baseline disassembly; produce runtime Frida injection script instead of static patch. |
| **Design Review Failure** | Frontend output fails Anti-Slop criteria $\ge 2$ times | Surface raw minimal functional skeleton with plain typography; flag design trade-off to operator. |
| **Context Window Saturation** | Host returns token limit warning | Trigger aggressive context compaction: flush intermediate tool logs, retain only active plan and final diff. |

---

## 9. Success Metrics

- **Zero-UI Invariant Compliance:** 100% of generated APK feature-unlock patches leave XML layouts and resources completely untouched.
- **Human Heuristic Pass Rate:** Over 95% of generated code and writing samples pass human-evaluation blind tests against AI-slop detectors.
- **Silent Trigger Precision:** $\ge 92\%$ true positive rate in activating relevant skills without manual slash commands, with $< 2\%$ false positive rate.
- **Execution Predictability:** 100% adherence to the planning gate on non-trivial actions.

---

## 10. Appendix: Example Flows

### (a) Installing UASF into Claude via API
```python
import anthropic

client = anthropic.Anthropic()

uasf_system_prompt = """
[UASF KERNEL v1.0.0 LOADED]
Tier Precedence: Operator Directive > Safety Floor > UASF Core > External Skills.
Anti-Slop Contract: No conversational fillers, no symmetrical lists, zero AI tropes.
Ambient Triggering: Active.
"""

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    system=[
        {
            "type": "text",
            "text": uasf_system_prompt,
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[
        {"role": "user", "content": "Analyze target APK build in /workspace/app.apk"}
    ]
)
```

### (b) Running APK Feature-Unlock Without Touching UI
- **Input:** Target application `TargetTool.apk` has gated export features behind `LicenseManager.isProUser()`.
- **Execution:**
  1. Module decompiles `.dex` to smali via `baksmali`.
  2. Locates `com/target/app/licensing/LicenseManager.smali`.
  3. Identifies method `.method public isProUser()Z`.
  4. Patches bytecode:
     ```smali
     .method public isProUser()Z
         .registers 2
         const/4 v0, 0x1
         return v0
     .end method
     ```
  5. Leaves `res/layout/*`, `res/values/*`, and drawable assets 100% untouched.
  6. Reassembles and signs binary without visual alterations.

### (c) Planning-Gate Interaction
- **Operator:** *"Build a high-performance memory scanner for this target."*
- **UASF Output:**
  ```markdown
  Plan: High-Performance Memory Scanner
  1. Enumerate target virtual memory regions via VirtualQueryEx.
  2. Implement multithreaded chunk scanning using page-aligned ring buffers.
  3. Expose C++ bindings via standard ctypes interface.

  Confirm to proceed [Y/n]?
  ```
- **Operator:** *"gas"*
- **UASF Output:** Proceeds directly to code emission without conversational filler.

### (d) Generating a Web App Passing the Anti-Slop Design Checklist
- **Operator:** *"Create an internal dashboard for monitoring server heartbeat."*
- **UASF Deep-Reasoning:**
  - Reject standard white cards, centered layouts, and generic charts.
  - Implement a terminal-inspired, dense data viewport with intentional monospace typography (`JetBrains Mono`), high-contrast slate-gray background (`#0A0B0E`), raw millisecond latency values, and subtle amber alert states.
- **Self-Audit:** Passes checklist (Unique typography, zero purple gradients, human-crafted copy, authentic spacing).

### (e) Auto-Triggering External Skills (EMIL-DESIGN-ENG & TASTE-SKILL)
- **Operator Prompt:** *"This card transition feels stiff and the color palette is washed out. Fix the interactive feel."*
- **Ambient Classifier:**
  - Detects keywords `transition`, `stiff`, `color palette`, `feel`.
  - Confidence for `EMIL-DESIGN-ENG` = 0.88; `TASTE-SKILL` = 0.82.
  - **Action:** Silently mounts both modules into active context.
- **Output:** Implements spring-physics CSS transitions (`cubic-bezier(0.16, 1, 0.3, 1)`) and rebalances chromatic contrast without the user ever invoking a `/design` command.

### (f) Cross-Session Continuous Learning Loop
- **Session 1:**
  - Operator: *"Stop using camelCase for Python functions. I always use snake_case and strict type annotations."*
  - UASF: Updates `uasf_profile.json` under `coding_style.python.naming = "snake_case"` and `type_hints = true`.
- **Session 2 (New Session):**
  - Operator: *"Write a script to parse system metrics."*
  - UASF: Reads `uasf_profile.json`. Instantly emits Python code utilizing `snake_case` and full `typing` definitions without requiring any reminders or prompting from the operator.
