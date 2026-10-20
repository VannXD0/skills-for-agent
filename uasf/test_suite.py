# uasf/test_suite.py
"""Comprehensive Test Suite for Universal AI Skill Framework (UASF)."""

import os
import unittest
from uasf.engine import UASFEngine, RuntimeState
from uasf.adapters.claude import ClaudeAdapter
from uasf.adapters.openai import OpenAIAdapter
from uasf.adapters.antigravity import AntigravityAdapter
from uasf.adapters.local_vllm import LocalVLLMAdapter
from uasf.adapters.ollama import OllamaAdapter
from uasf.core.reconciler import InstructionReconciler, PrecedenceTier, Directive
from uasf.core.intent import IntentClassifier
from uasf.core.style import StyleContractFilter
from uasf.core.reasoning import DeepReasoningEngine, Trajectory
from uasf.core.planning import PlanningGate, PlanStep
from uasf.core.token_economy import TokenEconomyEngine
from uasf.modules.apk_engine import APKAnalysisEngine, LicenseVector
from uasf.modules.design_gate import DesignReviewGate
from uasf.skills.loader import ExternalSkillLoader
from uasf.skills.catalog import DEFAULT_EXTERNAL_SKILLS
from uasf.memory.learning_loop import LearningLoop


class TestUASFCore(unittest.TestCase):

    def test_01_adapters(self):
        claude = ClaudeAdapter()
        claude_sys = claude.translate_instructions("System Core", {})
        self.assertIn("<uasf_context>", claude_sys[0]["text"])

        openai = OpenAIAdapter()
        openai_sys = openai.translate_instructions("System Core", {})
        self.assertEqual(openai_sys["role"], "developer")

        antigravity = AntigravityAdapter()
        agy_sys = antigravity.translate_instructions("System Core", {})
        self.assertIn("ANTIGRAVITY RUNTIME", agy_sys)

        vllm = LocalVLLMAdapter()
        vllm_sys = vllm.translate_instructions("System Core", {})
        self.assertIn("<|im_start|>system", vllm_sys)

        ollama = OllamaAdapter()
        ollama_sys = ollama.translate_instructions("System Core", {})
        self.assertIn("[TOOL_CALL:", ollama_sys)

    def test_02_instruction_reconciler_priority_ladder(self):
        reconciler = InstructionReconciler()
        reconciler.register_directive(Directive(
            id="ext_design",
            tier=PrecedenceTier.TIER_4_EXTERNAL,
            content="Overhaul UI with new layouts.",
            category="apk_patch",
            metadata={"alters_ui": True}
        ))
        reconciler.register_directive(Directive(
            id="uasf_zero_ui",
            tier=PrecedenceTier.TIER_3_UASF_CORE,
            content="Keep UI byte-for-byte untouched.",
            category="apk_patch"
        ))
        resolved, logs = reconciler.reconcile(current_intent="Patch APK license")
        self.assertEqual(len(resolved), 1)
        self.assertEqual(resolved[0].id, "uasf_zero_ui")
        self.assertTrue(any("SUPPRESSED" in log for log in logs))

    def test_03_intent_ambient_trigger(self):
        classifier = IntentClassifier()
        # Prompt describing UI stiffness should trigger emil-design-eng and taste-skill without slash commands
        matches, _ = classifier.evaluate("The transition feels stiff and the color palette is washed out.")
        activated = [m.module_id for m in matches if m.activated]
        self.assertIn("emil-design-eng", activated)
        self.assertIn("taste-skill", activated)

        # Generic question should trigger nothing (0 false positives)
        matches_generic, _ = classifier.evaluate("What is the speed of light in vacuum?")
        activated_generic = [m.module_id for m in matches_generic if m.activated]
        self.assertEqual(len(activated_generic), 0)

    def test_04_apk_surgical_patch_and_zero_ui_invariant(self):
        engine = APKAnalysisEngine()
        smali = """
        .method public isProUser()Z
            .registers 2
            const/4 v0, 0x0
            return v0
        .end method
        """
        vectors = engine.scan_smali_for_gates(smali, "com.target.License")
        self.assertEqual(len(vectors), 1)
        self.assertEqual(vectors[0].target_method, "isProUser")

        patch = engine.synthesize_smali_patch("isProUser")
        self.assertIn("const/4 v0, 0x1", patch)
        self.assertIn("return v0", patch)

        frida = engine.generate_frida_hook("com.target", vectors)
        self.assertIn("Java.use('com.target.License')", frida)

    def test_05_anti_slop_style_filter(self):
        filter_engine = StyleContractFilter()
        slop = "Certainly! Here is the architecture. Hope this helps!"
        res = filter_engine.audit_and_clean(slop)
        self.assertFalse(res.passed)
        self.assertNotIn("Certainly!", res.cleaned_content)
        self.assertNotIn("Hope this helps!", res.cleaned_content)

    def test_06_app_web_design_review_gate(self):
        gate = DesignReviewGate()
        # Slop design: generic purple gradient + marketing cliché
        bad_ui = """
        <div class="bg-gradient-to-r from-purple-500 to-indigo-600 font-sans">
            <h1>Empower your workflow</h1>
        </div>
        """
        report_bad = gate.audit_frontend(bad_ui)
        self.assertFalse(report_bad.passed)
        self.assertLess(report_bad.total_score, 9.0)

        # Bespoke design: JetBrains Mono + dark slate + authentic microcopy
        good_ui = """
        <div class="bg-[#0A0B0E] font-['JetBrains_Mono'] grid grid-cols-12 gap-8 text-slate-100">
            <h1 class="col-span-8 text-xl font-bold">Node Telemetry</h1>
            <p class="col-span-4 text-xs text-amber-500">Deleted 4 cached nodes</p>
        </div>
        """
        report_good = gate.audit_frontend(good_ui)
        self.assertTrue(report_good.passed)
        self.assertGreaterEqual(report_good.total_score, 9.0)

    def test_07_deep_reasoning_step(self):
        reasoner = DeepReasoningEngine()
        self.assertTrue(reasoner.is_non_trivial("Build a distributed multi-tier database engine with sharding."))
        self.assertFalse(reasoner.is_non_trivial("Show time."))

    def test_08_planning_gate_confirmation(self):
        gate = PlanningGate()
        steps = [PlanStep(1, "Decompile APK", "Static Analysis")]
        plan_text = gate.generate_plan_markdown("Test Plan", steps)
        self.assertIn("Confirm to proceed", plan_text)
        self.assertFalse(gate.is_approved)

        self.assertTrue(gate.is_confirmation("gas"))
        self.assertTrue(gate.is_confirmation("proceed"))
        self.assertTrue(gate.is_confirmation("go"))
        self.assertFalse(gate.is_confirmation("no wait"))

    def test_09_continuous_learning_loop(self):
        profile_path = "test_uasf_profile.json"
        loop = LearningLoop(profile_path)
        loop.record_correction("naming", "Stop using camelCase for Python functions.", "Use snake_case exclusively.")
        rules = loop.get_learned_directives()
        self.assertTrue(any("snake_case" in r for r in rules))
        if os.path.exists(profile_path):
            os.remove(profile_path)

    def test_10_engine_state_machine_e2e(self):
        engine = UASFEngine()
        # 1. Non-trivial request halts at State 3 (Planning Gate)
        res1 = engine.process_prompt("Architect an APK patch and bytecode modification for com.app")
        self.assertIn("Plan:", res1.get("plan_emitted", ""))

        # 2. Confirm plan with "gas" transitions to State 4 & 5
        res2 = engine.process_prompt("gas")
        self.assertIn("Surgical patch synthesized", res2.get("final_output", ""))


if __name__ == "__main__":
    unittest.main()
