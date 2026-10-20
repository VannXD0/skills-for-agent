# uasf/core/planning.py
"""Planning Gate enforcing deterministic roadmap confirmation."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class PlanStep:
    step_number: int
    title: str
    action_type: str
    target_path: Optional[str] = None
    verification: str = ""


class PlanningGate:
    """Manages structured roadmaps and pauses execution for operator confirmation."""

    CONFIRMATION_TOKENS = {"go", "gas", "proceed", "y", "yes", "approve", "confirm", "ok"}

    def __init__(self):
        self.pending_plan: Optional[str] = None
        self.is_approved: bool = False

    def is_confirmation(self, response: str) -> bool:
        cleaned = response.strip().lower()
        return cleaned in self.CONFIRMATION_TOKENS or any(token in cleaned.split() for token in self.CONFIRMATION_TOKENS)

    def generate_plan_markdown(self, title: str, steps: List[PlanStep]) -> str:
        lines = [f"# Plan: {title}\n"]
        for s in steps:
            target = f" -> `{s.target_path}`" if s.target_path else ""
            lines.append(f"{s.step_number}. **{s.title}** ({s.action_type}){target}")
            if s.verification:
                lines.append(f"   - *Verification:* {s.verification}")
        lines.append("\nConfirm to proceed [Y/n]?")
        self.pending_plan = "\n".join(lines)
        self.is_approved = False
        return self.pending_plan

    def register_approval(self):
        self.is_approved = True
        self.pending_plan = None
