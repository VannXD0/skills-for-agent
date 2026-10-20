# uasf/memory/learning_loop.py
"""Continuous Learning Loop with in-session memory and persistent profile store."""

import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CorrectionRecord:
    timestamp: str
    target_category: str  # "naming", "architecture", "ui", "framework"
    operator_directive: str
    inferred_rule: str


class LearningLoop:
    """Manages ephemeral session corrections and persistent cross-session profiles."""

    DEFAULT_PROFILE_PATH = "uasf_profile.json"

    def __init__(self, profile_path: str = DEFAULT_PROFILE_PATH):
        self.profile_path = profile_path
        self.session_memory: List[CorrectionRecord] = []
        self.persistent_profile: Dict[str, Any] = self._load_profile()

    def _load_profile(self) -> Dict[str, Any]:
        if os.path.exists(self.profile_path):
            try:
                with open(self.profile_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "uasf_profile_version": "1.0.0",
            "coding_style": {
                "python": {"naming": "snake_case", "type_hints": True},
                "typescript": {"strict": True, "semicolons": True}
            },
            "design_preferences": {
                "color_palette": "high_contrast_slate",
                "typography": "jetbrains_mono"
            },
            "learned_rules": []
        }

    def save_profile(self):
        try:
            with open(self.profile_path, "w", encoding="utf-8") as f:
                json.dump(self.persistent_profile, f, indent=2)
        except Exception as e:
            print(f"[UASF MEMORY] Failed to persist profile: {e}")

    def record_correction(self, category: str, directive: str, inferred_rule: str):
        record = CorrectionRecord(
            timestamp="now",
            target_category=category,
            operator_directive=directive,
            inferred_rule=inferred_rule
        )
        self.session_memory.append(record)

        # Update persistent profile
        if "learned_rules" not in self.persistent_profile:
            self.persistent_profile["learned_rules"] = []

        self.persistent_profile["learned_rules"].append({
            "category": category,
            "rule": inferred_rule,
            "source_directive": directive
        })
        self.save_profile()

    def get_learned_directives(self) -> List[str]:
        rules = []
        for r in self.persistent_profile.get("learned_rules", []):
            rules.append(f"Learned preference [{r.get('category')}]: {r.get('rule')}")
        return rules
