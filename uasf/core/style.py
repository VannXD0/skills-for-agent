# uasf/core/style.py
"""Style Contract & Anti-Slop Filter enforcing human-authored standards."""

import re
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class StyleAuditResult:
    passed: bool
    violations_found: List[str]
    cleaned_content: str


class StyleContractFilter:
    """Enforces human-authored linguistic standards and strips AI conversational clichés."""

    BANNED_PHRASES = [
        "certainly!", "certainly,", "here is", "here are", "hope this helps",
        "it is important to remember", "in today's fast-paced world",
        "let me know if you need anything else", "feel free to reach out",
        "as an ai", "i would be happy to", "delve into", "testament to",
        "beacon of", "tapestry of", "in conclusion", "without further ado"
    ]

    SYMMETRY_PATTERNS = [
        r"(\n-\s.*){3,}",  # Formulaic bullet runs
        r"(\b\w+\b,\s+\b\w+\b,\s+and\s+\b\w+\b)"  # Repetitive 3-item lists
    ]

    def audit_and_clean(self, text: str) -> StyleAuditResult:
        violations = []
        cleaned = text

        lower_text = text.lower()
        for phrase in self.BANNED_PHRASES:
            if phrase in lower_text:
                violations.append(f"Banned conversational filler: '{phrase}'")
                # Strip phrase case-insensitively
                pattern = re.compile(re.escape(phrase), re.IGNORECASE)
                cleaned = pattern.sub("", cleaned)

        # Eliminate empty pleasantry intros (e.g., "Certainly! Here is...")
        cleaned = re.sub(r"^\s*([A-Z][a-z]+!\s+)+", "", cleaned).strip()

        # Clean trailing polite boilerplate
        cleaned = re.sub(r"(?i)(hope this helps!|let me know if you have any questions\S*)\s*$", "", cleaned).strip()

        passed = len(violations) == 0
        return StyleAuditResult(
            passed=passed,
            violations_found=violations,
            cleaned_content=cleaned
        )

    def route_latency_tier(self, prompt: str) -> str:
        """Determines whether to execute on Fast Path (<1.5s TTFT) or Deep Path."""
        tokens = prompt.strip().split()
        if len(tokens) <= 8 and not any(k in prompt.lower() for k in ["build", "architect", "refactor", "patch", "apk"]):
            return "Fast Path"
        return "Deep Path"
