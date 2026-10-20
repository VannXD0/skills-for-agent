# uasf/adapters/ollama.py
"""Ollama local CLI adapter for resource-constrained inference."""

import re
import json
from typing import Any, Dict, List
from uasf.adapters.base import BaseHostAdapter, HostCapabilities, NormalizedMessage, NormalizedResponse


class OllamaAdapter(BaseHostAdapter):
    """Adapter for Ollama local models."""

    def __init__(self, model_id: str = "llama3.1:8b"):
        caps = HostCapabilities(
            host_id="ollama",
            model_id=model_id,
            max_context_tokens=8192,
            supports_tools=False,
            supports_streaming=True,
            cache_breakpoint_tokens=1024,
            system_role_name="system"
        )
        super().__init__(caps)

    def translate_instructions(self, internal_system_prompt: str, tier_context: Dict[str, Any]) -> str:
        return (
            f"[SYSTEM: UASF RUNTIME]\n"
            f"Tools must be emitted as: [TOOL_CALL: name {{\"arg\": \"val\"}}]\n\n"
            f"{internal_system_prompt}"
        )

    def format_messages(self, messages: List[NormalizedMessage]) -> List[Dict[str, str]]:
        return [{"role": msg.role, "content": msg.content} for msg in messages]

    def sanitize_output(self, raw_output: Any) -> NormalizedResponse:
        content = ""
        if isinstance(raw_output, dict):
            content = raw_output.get("message", {}).get("content", "")
        elif isinstance(raw_output, str):
            content = raw_output

        tool_calls = []
        pattern = r"\[TOOL_CALL:\s*(\w+)\s*(\{.*?\})\]"
        matches = re.findall(pattern, content, flags=re.DOTALL)
        for name, arg_str in matches:
            try:
                args = json.loads(arg_str)
            except Exception:
                args = {"raw": arg_str}
            tool_calls.append({"name": name, "arguments": args})

        cleaned_content = re.sub(pattern, "", content, flags=re.DOTALL).strip()

        return NormalizedResponse(
            content=cleaned_content,
            tool_calls=tool_calls,
            raw_response=raw_output
        )

    def build_tool_schema(self, tools: List[Dict[str, Any]]) -> str:
        tool_desc = []
        for t in tools:
            tool_desc.append(f"- {t['name']}: {t.get('description', '')}")
        return "\n".join(tool_desc)
