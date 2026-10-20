# uasf/registry.py
"""Module Registry managing internal and external UASF modules."""

import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ModuleDefinition:
    id: str
    version: str
    type: str  # "kernel", "feature", "external_skill"
    entrypoint: Optional[str] = None
    source: Optional[str] = None
    triggers: List[str] = field(default_factory=list)


class ModuleRegistry:
    """Loads and inspects the UASF module registry."""

    DEFAULT_REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "uasf_registry.json")

    def __init__(self, path: Optional[str] = None):
        self.path = path or self.DEFAULT_REGISTRY_PATH
        self.modules: Dict[str, ModuleDefinition] = {}
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data.get("modules", []):
                    mod = ModuleDefinition(
                        id=item["id"],
                        version=item["version"],
                        type=item["type"],
                        entrypoint=item.get("entrypoint"),
                        source=item.get("source"),
                        triggers=item.get("triggers", [])
                    )
                    self.modules[mod.id] = mod

    def get(self, module_id: str) -> Optional[ModuleDefinition]:
        return self.modules.get(module_id)

    def list_modules(self) -> List[ModuleDefinition]:
        return list(self.modules.values())
