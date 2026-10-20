# uasf/adapters/__init__.py
"""Host runtime adapters."""

from uasf.adapters.base import BaseHostAdapter, HostCapabilities, NormalizedMessage, NormalizedResponse
from uasf.adapters.claude import ClaudeAdapter
from uasf.adapters.openai import OpenAIAdapter
from uasf.adapters.antigravity import AntigravityAdapter
from uasf.adapters.local_vllm import LocalVLLMAdapter
from uasf.adapters.ollama import OllamaAdapter

__all__ = [
    "BaseHostAdapter",
    "HostCapabilities",
    "NormalizedMessage",
    "NormalizedResponse",
    "ClaudeAdapter",
    "OpenAIAdapter",
    "AntigravityAdapter",
    "LocalVLLMAdapter",
    "OllamaAdapter",
]
