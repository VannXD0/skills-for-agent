# uasf/cli.py
"""UASF Command-Line Interface."""

import argparse
import sys
import json
from uasf.engine import UASFEngine
from uasf.registry import ModuleRegistry
from uasf.memory.learning_loop import LearningLoop
from uasf.modules.design_gate import DesignReviewGate


def main():
    parser = argparse.ArgumentParser(description="Universal AI Skill Framework (UASF) CLI Engine")
    subparsers = parser.add_subparsers(dest="command")

    # Command: run
    run_parser = subparsers.add_parser("run", help="Process an operator prompt through UASF state machine")
    run_parser.add_argument("prompt", type=str, help="Prompt text")
    run_parser.add_argument("--confirm", action="store_true", help="Auto-confirm planning gates")

    # Command: modules
    subparsers.add_parser("modules", help="List all registered modules and external skills")

    # Command: audit-design
    audit_parser = subparsers.add_parser("audit-design", help="Audit an HTML/CSS file against Anti-Slop criteria")
    audit_parser.add_argument("file", type=str, help="Path to markup or CSS file")

    # Command: profile
    profile_parser = subparsers.add_parser("profile", help="Display or update persistent operator profile")
    profile_parser.add_argument("--add-rule", nargs=2, metavar=("CATEGORY", "RULE"), help="Add a learned rule")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "run":
        engine = UASFEngine()
        res = engine.process_prompt(args.prompt)
        if args.confirm and res.get("plan_emitted"):
            # Auto confirm
            print("[UASF] Plan emitted. Auto-confirming via --confirm flag...")
            res = engine.process_prompt("gas")
        print(f"--- UASF Response (Latency: {res.get('latency_ms')}ms) ---")
        print(res.get("final_output"))
        if res.get("activated_skills"):
            print(f"[Ambient Skills Activated: {', '.join(res.get('activated_skills'))}]")

    elif args.command == "modules":
        reg = ModuleRegistry()
        print("Registered UASF Modules & Skills:")
        for m in reg.list_modules():
            print(f"  - [{m.type}] {m.id} (v{m.version}) -> triggers: {', '.join(m.triggers)}")

    elif args.command == "audit-design":
        gate = DesignReviewGate()
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                content = f.read()
            report = gate.audit_frontend(content)
            print(f"Design Review Gate Result: {'PASSED' if report.passed else 'FAILED'}")
            print(f"Total Score: {report.total_score}/10.0")
            for item in report.items:
                status = "PASS" if item.passed else "FAIL"
                print(f"  [{status}] {item.rule_name}: {item.score_awarded}/2.5 — {item.notes}")
            if report.rejection_reasons:
                print("Rejection Reasons:")
                for r in report.rejection_reasons:
                    print(f"  * {r}")
        except Exception as e:
            print(f"Failed to read file: {e}")

    elif args.command == "profile":
        loop = LearningLoop()
        if args.add_rule:
            cat, rule = args.add_rule
            loop.record_correction(cat, "Manual CLI addition", rule)
            print(f"Recorded rule in category '{cat}': {rule}")
        else:
            print(json.dumps(loop.persistent_profile, indent=2))


if __name__ == "__main__":
    main()
