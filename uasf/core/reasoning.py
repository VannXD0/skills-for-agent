# uasf/core/reasoning.py
"""Deep-Reasoning Step executing problem formulation and tradeoff analysis."""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Trajectory:
    name: str
    description: str
    memory_impact: str
    complexity_level: str
    latency_profile: str
    pros: List[str]
    cons: List[str]


@dataclass
class ReasoningOutput:
    is_non_trivial: bool
    core_problem: str
    trajectories: List[Trajectory]
    selected_trajectory: str
    technical_justification: str


class DeepReasoningEngine:
    """Enforces root-cause analysis and trade-off matrices before non-trivial execution."""

    NON_TRIVIAL_KEYWORDS = [
        "architecture", "refactor", "reverse", "apk", "smali", "frida",
        "database", "pipeline", "schema", "multi-tier", "framework",
        "concurrency", "distributed", "compiler", "engine"
    ]

    def is_non_trivial(self, prompt: str) -> bool:
        lower = prompt.lower()
        word_count = len(lower.split())
        if word_count > 40:
            return True
        return any(keyword in lower for keyword in self.NON_TRIVIAL_KEYWORDS)

    def formulate_reasoning(
        self,
        prompt: str,
        problem_statement: str,
        trajectory_options: List[Trajectory],
        selected_index: int,
        justification: str
    ) -> ReasoningOutput:
        non_trivial = self.is_non_trivial(prompt)
        selected = trajectory_options[selected_index].name if trajectory_options else "Default Path"
        return ReasoningOutput(
            is_non_trivial=non_trivial,
            core_problem=problem_statement,
            trajectories=trajectory_options,
            selected_trajectory=selected,
            technical_justification=justification
        )
