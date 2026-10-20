# uasf/adapters/openai.py
"""OpenAI GPT-4o and Codex adapter supporting developer role and function schemas."""

import json
from typing import Any, Dict, List
from uasf.adapters.base import BaseHostAdapter, HostCapabilities, NormalizedMessage, NormalizedResponse


class OpenAIAdapter(BaseHostAdapter):
    """Adapter for OpenAI GPT-4o / Codex runtime."""

    def __init__(self, model_id: str = "gpt-4o"):
        caps = HostCapabilities(
            host_id="openai",
            model_id=model_id,
            max_context_tokens=128000,
            supports_tools=True,
            supports_streaming=True,
            cache_breakpoint_tokens=2048,
            system_role_name="developer"
        )
        super().__init__(caps)

    def translate_instructions(self, internal_system_prompt: str, tier_context: Dict[str, Any]) -> Dict[str, str]:
        content = (
            f"# UASF CORE SYSTEM DIRECTIVE\n"
            f"Precedence: Tier 1 Operator > Tier 2 Safety > Tier 3 System > Tier 4 Skills > Tier 5 Profile\n\n"
            f"{internal_system_prompt}"
        )
        return {
            "role": "developer",
            "content": content
        }

    def format_messages(self, messages: List[NormalizedMessage]) -> List[Dict[str, Any]]:
        formatted = []
        for msg in messages:
            item = {"role": msg.role, "content": msg.content}
            if msg.name:
                item["name"] = msg.name
            if msg.tool_call_id:
                item["tool_call_id"] = msg.tool_call_id
            formatted.append(item)
        return formatted

    def sanitize_output(self, raw_output: Any) -> NormalizedResponse:
        content = ""
        tool_calls = []
        if isinstance(raw_output, dict):
            choices = raw_output.get("choices", [])
            if choices:
                message = choices[0].get("message", {})
                content = message.get("content") or ""
                raw_tools = message.get("tool_calls", [])
                for tc in raw_tools:
                    func = tc.get("function", {})
                    args = func.get("arguments", "{}")
                    if isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except Exception:
                            args = {"raw": args}
                    tool_calls.append({
                        "id": tc.get("id"),
                        "name": func.get("name"),
                        "arguments": args
                    })
        elif isinstance(raw_output, str):
            content = raw_output

        return NormalizedResponse(
            content=content.strip(),
            tool_calls=tool_calls,
            raw_response=raw_output
        )

    def build_tool_schema(self, tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        openai_tools = []
        for tool in tools:
            openai_tools.append({
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool.get("description", ""),
                    "parameters": tool.get("parameters", {"type": "object", "properties": {}})
                }
            })
        return openai_tools
