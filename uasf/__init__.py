# uasf/__init__.py
"""Universal AI Skill Framework (UASF)
Multi-Host AI Run-time Layer and Capability Engine.
"""

__version__ = "1.0.0"
__all__ = ["UASFEngine", "ModuleRegistry", "InstructionReconciler"]

from uasf.engine import UASFEngine
from uasf.registry import ModuleRegistry
from uasf.core.reconciler import InstructionReconciler
