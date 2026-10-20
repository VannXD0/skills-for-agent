# uasf/skills/catalog.py
"""Catalog of default third-party skills integrated out-of-the-box."""

from uasf.skills.loader import ExternalSkillManifest

DEFAULT_EXTERNAL_SKILLS = [
    ExternalSkillManifest(
        id="emil-design-eng",
        version="3.1.0",
        name="Emil Design Engineering Discipline",
        source="npm:@design-eng/skill",
        triggers=["frontend", "component", "animation", "layout", "web app", "transition", "spring"],
        priority_weight=0.9,
        exported_directives=[
            "Enforce fluid spring transitions using cubic-bezier(0.16, 1, 0.3, 1).",
            "Maintain physics-based interaction boundaries on drag and hover states.",
            "Eliminate linear transitions on primary navigation elements."
        ]
    ),
    ExternalSkillManifest(
        id="taste-skill",
        version="1.2.0",
        name="Taste Skill - Curated Aesthetic Judgment",
        source="github:curated-craft/taste",
        triggers=["visual polish", "typography", "palette", "aesthetic", "washed out", "kerning"],
        priority_weight=0.95,
        exported_directives=[
            "Anchor palettes around high-contrast intention with at most one sharp accent.",
            "Enforce typographic hierarchy with personality; eliminate generic browser defaults.",
            "Strictly avoid symmetrical 24px uniform card grids."
        ]
    ),
    ExternalSkillManifest(
        id="impeccable",
        version="2.0.1",
        name="Impeccable Code Craft Benchmark",
        source="internal://impeccable",
        triggers=["code craft", "clean boundary", "interface", "refactor", "zero-clutter"],
        priority_weight=0.85,
        exported_directives=[
            "Design clean, single-responsibility module boundaries.",
            "Preserve zero dead code and no unnecessary indirection.",
            "Every function signature must carry concrete type annotations."
        ]
    ),
    ExternalSkillManifest(
        id="baseline-ui",
        version="1.0.4",
        name="Baseline UI Correctness & Accessibility",
        source="internal://baseline-ui",
        triggers=["accessibility", "a11y", "responsive", "breakpoint", "semantic html", "wcag"],
        priority_weight=0.80,
        exported_directives=[
            "Ensure full WCAG 2.1 AA color contrast compliance (>= 4.5:1 for normal text).",
            "Every interactive element must provide visible keyboard focus rings.",
            "Use strictly semantic HTML5 markup (<main>, <nav>, <section>, <article>)."
        ]
    )
]
