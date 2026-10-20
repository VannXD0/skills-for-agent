# uasf/adapters/claude.py
"""Anthropic Claude adapter supporting sliding cache windows and XML tags."""

from typing import Any, Dict, List
from uasf.adapters.base import BaseHostAdapter, HostCapabilities, NormalizedMessage, NormalizedResponse


class ClaudeAdapter(BaseHostAdapter):
    """Adapter for Anthropic Claude 3.5 / 3.7 runtime."""

    def __init__(self, model_id: str = "claude-3-7-sonnet-20250219"):
        caps = HostCapabilities(
            host_id="anthropic",
            model_id=model_id,
            max_context_tokens=200000,
            supports_tools=True,
            supports_streaming=True,
            cache_breakpoint_tokens=2048,
            system_role_name="system"
        )
        super().__init__(caps)

    def translate_instructions(self, internal_system_prompt: str, tier_context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Compiles system instruction with cache control blocks."""
        formatted_prompt = (
            f"<uasf_context>\n"
            f"<priority_ladder>\n"
            f"Tier 1: Current Operator Directive\n"
            f"Tier 2: Host Safety Floor\n"
            f"Tier 3: UASF System Invariants\n"
            f"Tier 4: External Skills\n"
            f"Tier 5: Learned Profile\n"
            f"</priority_ladder>\n\n"
            f"{internal_system_prompt}\n"
            f"</uasf_context>"
        )
        return [
            {
                "type": "text",
                "text": formatted_prompt,
                "cache_control": {"type": "ephemeral"}
            }
        ]

    def format_messages(self, messages: List[NormalizedMessage]) -> List[Dict[str, Any]]:
        formatted = []
        for msg in messages:
            if msg.role == "system":
                continue  # Handled separately in Claude
            role = "assistant" if msg.role == "assistant" else "user"
            formatted.append({
                "role": role,
                "content": msg.content
            })
        return formatted

    def sanitize_output(self, raw_output: Any) -> NormalizedResponse:
        content = ""
        tool_calls = []
        if isinstance(raw_output, dict):
            content_blocks = raw_output.get("content", [])
            for block in content_blocks:
                if isinstance(block, dict):
                    if block.get("type") == "text":
                        content += block.get("text", "")
                    elif block.get("type") == "tool_use":
                        tool_calls.append({
                            "id": block.get("id"),
                            "name": block.get("name"),
                            "arguments": block.get("input", {})
                        })
        elif isinstance(raw_output, str):
            content = raw_output

        # Strip vendor internal tags
        content = content.replace("<antThinking>", "").replace("</antThinking>", "").strip()

        return NormalizedResponse(
            content=content,
            tool_calls=tool_calls,
            raw_response=raw_output
        )

    def build_tool_schema(self, tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        claude_tools = []
        for tool in tools:
            claude_tools.append({
                "name": tool["name"],
                "description": tool.get("description", ""),
                "input_schema": tool.get("parameters", {"type": "object", "properties": {}})
            })
        return claude_tools
