# uasf/core/intent.py
"""Intent-Detection & Auto-Trigger Layer (Zero-Slash Command Ambient Activation)."""

import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple


@dataclass
class IntentMatch:
    module_id: str
    confidence: float
    matched_keywords: List[str]
    activated: bool
    ambiguous: bool = False


class IntentClassifier:
    """Classifies user intent using keyword density and n-gram overlap vectors."""

    ACTIVATION_THRESHOLD = 0.72
    AMBIGUITY_LOW = 0.68
    AMBIGUITY_HIGH = 0.75

    def __init__(self, registered_skill_triggers: Optional[Dict[str, List[str]]] = None):
        self.triggers: Dict[str, List[str]] = registered_skill_triggers or {
            "uasf-apk-patcher": [
                "apk", "smali", "dex", "frida", "license", "bypass", "unlock",
                "decompilation", "baksmali", "jadx", "in-app billing", "isvip"
            ],
            "emil-design-eng": [
                "frontend", "component", "animation", "layout", "web app",
                "transition", "stiff", "micro-interaction", "physics", "spring"
            ],
            "taste-skill": [
                "visual polish", "typography", "palette", "aesthetic", "washed out",
                "color palette", "contrast", "kerning", "hierarchy"
            ],
            "impeccable": [
                "code craft", "clean boundary", "interface", "refactor", "elegance",
                "modular", "zero-clutter"
            ],
            "baseline-ui": [
                "accessibility", "a11y", "responsive", "breakpoint", "semantic html",
                "wcag", "contrast ratio"
            ]
        }

    def register_triggers(self, module_id: str, triggers: List[str]):
        self.triggers[module_id] = [t.lower() for t in triggers]

    def _tokenize(self, text: str) -> Set[str]:
        words = "".join([c if c.isalnum() else " " for c in text.lower()]).split()
        return set(words)

    def evaluate(self, prompt: str) -> Tuple[List[IntentMatch], Optional[str]]:
        """Evaluates incoming prompt against skill trigger profiles."""
        tokens = self._tokenize(prompt)
        matches: List[IntentMatch] = []

        if not tokens:
            return [], None

        for module_id, trigger_list in self.triggers.items():
            matched = []
            score = 0.0
            for trig in trigger_list:
                trig_tokens = self._tokenize(trig)
                if trig_tokens.issubset(tokens):
                    matched.append(trig)
                    # Significant boost for full phrase match
                    score += 0.55 * len(trig_tokens)
                elif any(t in tokens for t in trig_tokens):
                    score += 0.25

            # Calibrated sigmoid to match PRD Section 4.8 & Appendix 10(e) (C >= 0.72 threshold)
            if score >= 1.0:
                confidence = 0.82 + min(0.16, (score - 1.0) * 0.1)
            elif score >= 0.5:
                confidence = 0.72 + (score - 0.5) * 0.2
            elif score > 0:
                confidence = score * 0.6
            else:
                confidence = 0.0

            confidence = min(1.0, max(0.0, confidence))

            is_active = confidence >= self.ACTIVATION_THRESHOLD
            matches.append(IntentMatch(
                module_id=module_id,
                confidence=round(confidence, 3),
                matched_keywords=matched,
                activated=is_active
            ))

        # Check for ambiguity guard: two conflicting skills between 0.68 and 0.75
        borderline = [m for m in matches if self.AMBIGUITY_LOW <= m.confidence <= self.AMBIGUITY_HIGH]
        ambiguity_prompt = None
        if len(borderline) >= 2:
            for b in borderline:
                b.ambiguous = True
                b.activated = False
            names = ", ".join([b.module_id for b in borderline])
            ambiguity_prompt = f"Ambiguity detected between skills [{names}]. Clarification requested."

        # Filter activated
        activated_matches = [m for m in matches if m.activated]
        activated_matches.sort(key=lambda m: m.confidence, reverse=True)

        return activated_matches, ambiguity_prompt
