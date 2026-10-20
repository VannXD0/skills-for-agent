# uasf/adapters/local_vllm.py
"""vLLM and Hermes Open-Weight model adapter utilizing ChatML formatting."""

from typing import Any, Dict, List
from uasf.adapters.base import BaseHostAdapter, HostCapabilities, NormalizedMessage, NormalizedResponse


class LocalVLLMAdapter(BaseHostAdapter):
    """Adapter for local vLLM and Hermes runtimes."""

    def __init__(self, model_id: str = "NousResearch/Hermes-3-Llama-3.1-8B"):
        caps = HostCapabilities(
            host_id="local_vllm",
            model_id=model_id,
            max_context_tokens=131072,
            supports_tools=True,
            supports_streaming=True,
            cache_breakpoint_tokens=2048,
            system_role_name="system"
        )
        super().__init__(caps)

    def translate_instructions(self, internal_system_prompt: str, tier_context: Dict[str, Any]) -> str:
        return (
            f"<|im_start|>system\n"
            f"[UASF RUNTIME LAYER - HERMES / VLLM]\n"
            f"{internal_system_prompt}\n"
            f"<|im_end|>"
        )

    def format_messages(self, messages: List[NormalizedMessage]) -> str:
        prompt_str = ""
        for msg in messages:
            prompt_str += f"<|im_start|>{msg.role}\n{msg.content}\n<|im_end|>\n"
        prompt_str += "<|im_start|>assistant\n"
        return prompt_str

    def sanitize_output(self, raw_output: Any) -> NormalizedResponse:
        content = ""
        if isinstance(raw_output, dict):
            content = raw_output.get("text", "") or raw_output.get("content", "")
        elif isinstance(raw_output, str):
            content = raw_output

        # Strip ChatML end tokens
        content = content.replace("<|im_end|>", "").replace("<|endoftext|>", "").strip()

        return NormalizedResponse(
            content=content,
            raw_response=raw_output
        )

    def build_tool_schema(self, tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return tools
