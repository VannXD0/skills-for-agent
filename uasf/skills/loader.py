# uasf/skills/loader.py
"""External Skill Loader supporting dynamic plugin ingestion and sandboxing."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ExternalSkillManifest:
    id: str
    version: str
    name: str
    source: str
    triggers: List[str]
    priority_weight: float = 1.0
    exported_directives: List[str] = field(default_factory=list)
    sandboxed: bool = True


class ExternalSkillLoader:
    """Manages the registration, sandboxing, and ingestion of third-party skills."""

    def __init__(self):
        self.registry: Dict[str, ExternalSkillManifest] = {}
        self.active_skills: Dict[str, ExternalSkillManifest] = {}

    def register(self, manifest: ExternalSkillManifest):
        self.registry[manifest.id] = manifest

    def load_skill(self, skill_id: str) -> Optional[ExternalSkillManifest]:
        if skill_id in self.registry:
            skill = self.registry[skill_id]
            self.active_skills[skill_id] = skill
            return skill
        return None

    def get_skill_directives(self, skill_id: str) -> List[str]:
        if skill_id in self.active_skills:
            return self.active_skills[skill_id].exported_directives
        return []

    def unload_all(self):
        self.active_skills.clear()
