# uasf/adapters/base.py
"""Abstract base adapter normalizing heterogeneous LLM runtime I/O."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class HostCapabilities:
    """Metadata describing host capabilities probed at bootstrap."""
    host_id: str
    model_id: str
    max_context_tokens: int
    supports_tools: bool
    supports_streaming: bool
    cache_breakpoint_tokens: int = 2048
    system_role_name: str = "system"


@dataclass
class NormalizedMessage:
    """Normalized internal message schema."""
    role: str  # "system", "developer", "user", "assistant", "tool"
    content: str
    name: Optional[str] = None
    tool_call_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class NormalizedResponse:
    """Normalized internal response schema."""
    content: str
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)
    latency_ms: float = 0.0
    tokens_consumed: int = 0
    raw_response: Any = None


class BaseHostAdapter(ABC):
    """Abstract host adapter for multi-AI runtimes."""

    def __init__(self, capabilities: HostCapabilities):
        self.capabilities = capabilities

    @abstractmethod
    def translate_instructions(self, internal_system_prompt: str, tier_context: Dict[str, Any]) -> Any:
        """Translates internal system instructions into host-specific structure."""
        pass

    @abstractmethod
    def format_messages(self, messages: List[NormalizedMessage]) -> Any:
        """Formats normalized messages into host-native payload."""
        pass

    @abstractmethod
    def sanitize_output(self, raw_output: Any) -> NormalizedResponse:
        """Strips host-specific tokens and returns normalized response."""
        pass

    @abstractmethod
    def build_tool_schema(self, tools: List[Dict[str, Any]]) -> Any:
        """Builds host-compatible tool schemas."""
        pass
