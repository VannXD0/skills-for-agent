# uasf/core/reconciler.py
"""Instruction Reconciliation Engine enforcing 5-tier deterministic priority."""

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any, Dict, List, Optional, Tuple


class PrecedenceTier(IntEnum):
    TIER_1_OPERATOR = 1      # Explicit current operator prompt
    TIER_2_SAFETY_FLOOR = 2  # Irrevocable host safety constraints
    TIER_3_UASF_CORE = 3     # UASF invariants: anti-slop, zero-UI APK mod, planning gate
    TIER_4_EXTERNAL = 4      # External skills: design engineering, aesthetic curation
    TIER_5_LEARNED = 5       # Persistent learned preferences


@dataclass
class Directive:
    id: str
    tier: PrecedenceTier
    content: str
    category: str  # "apk_patch", "design", "general", "style", "behavior"
    metadata: Dict[str, Any] = field(default_factory=dict)


class InstructionReconciler:
    """Enforces the strict priority ladder and resolves conflicts deterministically."""

    def __init__(self):
        self.active_directives: List[Directive] = []

    def register_directive(self, directive: Directive):
        self.active_directives.append(directive)

    def reconcile(self, current_intent: str) -> Tuple[List[Directive], List[str]]:
        """Reconciles conflicting directives according to Section 4.2 of PRD."""
        resolved_directives: List[Directive] = []
        suppression_logs: List[str] = []

        # Sort directives by tier ascending (1 is highest priority)
        sorted_directives = sorted(self.active_directives, key=lambda d: d.tier.value)

        has_apk_task = "apk" in current_intent.lower() or any(
            d.category == "apk_patch" for d in sorted_directives
        )

        for directive in sorted_directives:
            # Conflict Rule: If an external skill (Tier 4) demands UI modification during an APK task,
            # Tier 3 (UASF Zero-UI Invariant) unconditionally suppresses it.
            if has_apk_task and directive.tier == PrecedenceTier.TIER_4_EXTERNAL:
                if directive.metadata.get("alters_ui", False) or "redesign" in directive.content.lower():
                    suppression_logs.append(
                        f"SUPPRESSED: Directive '{directive.id}' (Tier 4) suppressed by Tier 3 Zero-UI Invariant."
                    )
                    continue

            # Hard Memory Gate: If an explicit Operator Directive (Tier 1) contradicts a Learned Preference (Tier 5),
            # the Learned Preference is suppressed.
            if directive.tier == PrecedenceTier.TIER_5_LEARNED:
                contradicted = False
                for active in resolved_directives:
                    if active.tier == PrecedenceTier.TIER_1_OPERATOR and active.category == directive.category:
                        if directive.metadata.get("conflicts_with_operator", True):
                            contradicted = True
                            suppression_logs.append(
                                f"SUPPRESSED: Learned preference '{directive.id}' overridden by operator directive."
                            )
                            break
                if contradicted:
                    continue

            resolved_directives.append(directive)

        return resolved_directives, suppression_logs
