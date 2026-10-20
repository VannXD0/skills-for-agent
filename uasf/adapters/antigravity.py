# uasf/adapters/antigravity.py
"""Google Antigravity (AGY) runtime adapter."""

from typing import Any, Dict, List
from uasf.adapters.base import BaseHostAdapter, HostCapabilities, NormalizedMessage, NormalizedResponse


class AntigravityAdapter(BaseHostAdapter):
    """Adapter for Antigravity IDE and subagent environment."""

    def __init__(self, model_id: str = "gemini-3.8-flash"):
        caps = HostCapabilities(
            host_id="antigravity",
            model_id=model_id,
            max_context_tokens=1048576,
            supports_tools=True,
            supports_streaming=True,
            cache_breakpoint_tokens=2048,
            system_role_name="system"
        )
        super().__init__(caps)

    def translate_instructions(self, internal_system_prompt: str, tier_context: Dict[str, Any]) -> str:
        # AGY workspace rules integration: plain plan.md, zero native-plan-system triggers
        instruction = (
            f"# UASF CORE — ANTIGRAVITY RUNTIME LAYER\n"
            f"Mode Discipline: Plain plan.md for planning. No task_boundary or notify_user.\n"
            f"Precedence: Tier 1 Operator > Tier 2 Safety Floor > Tier 3 System Invariants > Tier 4 External Skills\n\n"
            f"{internal_system_prompt}"
        )
        return instruction

    def format_messages(self, messages: List[NormalizedMessage]) -> List[Dict[str, Any]]:
        return [{"role": msg.role, "content": msg.content} for msg in messages]

    def sanitize_output(self, raw_output: Any) -> NormalizedResponse:
        content = ""
        tool_calls = []
        if isinstance(raw_output, dict):
            content = raw_output.get("content", "")
            tool_calls = raw_output.get("tool_calls", [])
        elif isinstance(raw_output, str):
            content = raw_output

        return NormalizedResponse(
            content=content.strip(),
            tool_calls=tool_calls,
            raw_response=raw_output
        )

    def build_tool_schema(self, tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # Native antigravity tool declarations
        return tools
