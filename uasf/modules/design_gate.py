# uasf/modules/design_gate.py
"""App/Web Design Review Gate enforcing Anti-Slop craft standards."""

import re
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class DesignAuditItem:
    rule_name: str
    passed: bool
    score_awarded: float  # out of 2.5
    notes: str


@dataclass
class DesignAuditReport:
    total_score: float  # out of 10.0
    passed: bool        # requires >= 9.0
    items: List[DesignAuditItem] = field(default_factory=list)
    rejection_reasons: List[str] = field(default_factory=list)


class DesignReviewGate:
    """Automated pre-delivery heuristic audit evaluating frontend code for AI slop."""

    PURPLE_GRADIENT_PATTERNS = [
        r"linear-gradient\(.*#?[689a-fA-F0-9]*\b(purple|indigo|violet|6366f1|8b5cf6|a855f7|7c3aed)\b",
        r"bg-gradient-to-r\s+from-purple",
        r"bg-gradient-to-r\s+from-indigo",
        r"bg-gradient-to-tr\s+from-violet"
    ]

    GENERIC_COPY_PATTERNS = [
        r"\bempower your workflow\b",
        r"\bunleash the power of\b",
        r"\bseamless integration\b",
        r"\ball-in-one solution\b",
        r"\bthe future of\b",
        r"\beffortlessly manage\b"
    ]

    DEFAULT_SANS_PATTERNS = [
        r"font-family:\s*(-apple-system|system-ui|sans-serif);",
        r"font-sans"
    ]

    def audit_frontend(self, markup_and_css: str) -> DesignAuditReport:
        items = []
        rejections = []
        content_lower = markup_and_css.lower()

        # 1. Typography Check
        has_generic_font = any(re.search(p, markup_and_css) for p in self.DEFAULT_SANS_PATTERNS)
        has_characterful_font = any(f in content_lower for f in ["jetbrains mono", "inter var", "cal sans", "geist", "fira code", "newsreader", "syne", "plus jakarta sans"])
        if has_characterful_font and not has_generic_font:
            items.append(DesignAuditItem("Typography Check", True, 2.5, "Bespoke characterful font scale detected."))
        elif not has_generic_font:
            items.append(DesignAuditItem("Typography Check", True, 2.3, "Acceptable custom font definitions."))
        else:
            items.append(DesignAuditItem("Typography Check", False, 1.5, "Default fallback sans-serif without distinct character."))
            rejections.append("Typography lacks personality or relies on generic browser default stack.")

        # 2. Color Restraint Check (Purple gradient ban)
        has_purple_grad = any(re.search(p, content_lower) for p in self.PURPLE_GRADIENT_PATTERNS)
        if has_purple_grad:
            items.append(DesignAuditItem("Color Restraint Check", False, 0.5, "Generic purple-blue AI gradient detected."))
            rejections.append("Detected cliché AI purple/indigo gradient; requires deliberate palette with high contrast.")
        else:
            items.append(DesignAuditItem("Color Restraint Check", True, 2.5, "Disciplined color palette without generic gradients."))

        # 3. Layout Asymmetry Check
        # Check if code has varied grid spans, asymmetric split, or intentional whitespace rhythm
        has_asymmetry = any(tok in content_lower for tok in ["col-span-2", "grid-cols-12", "flex-1", "gap-12", "gap-8", "sticky top-", "w-2/3"])
        if has_asymmetry:
            items.append(DesignAuditItem("Layout Asymmetry Check", True, 2.5, "Intentional focal hierarchy and asymmetric cadence."))
        else:
            items.append(DesignAuditItem("Layout Asymmetry Check", False, 1.8, "Rigid uniform card grid without visual tension."))
            rejections.append("Layout is rigidly symmetrical; needs deliberate visual tension.")

        # 4. Copy Authenticity Check
        has_generic_copy = any(re.search(p, content_lower) for p in self.GENERIC_COPY_PATTERNS)
        if has_generic_copy:
            items.append(DesignAuditItem("Copy Authenticity Check", False, 1.0, "Contains generic marketing filler copy."))
            rejections.append("Microcopy contains AI marketing clichés ('empower your workflow', 'all-in-one').")
        else:
            items.append(DesignAuditItem("Copy Authenticity Check", True, 2.5, "Authentic, concrete microcopy."))

        total = sum(item.score_awarded for item in items)
        total = round(total, 2)
        passed = total >= 9.0 and len(rejections) == 0

        return DesignAuditReport(
            total_score=total,
            passed=passed,
            items=items,
            rejection_reasons=rejections
        )
