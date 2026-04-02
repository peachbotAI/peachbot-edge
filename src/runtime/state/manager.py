from typing import Dict, Any

from src.runtime.state.intelligence import MemoryIntelligence


class StateManager:
    """
    Intelligent memory manager with decay + reinforcement.
    """

    def __init__(self) -> None:
        self.memory_engine = MemoryIntelligence()

    def update(self, key: str, value: Any) -> None:
        self.memory_engine.update(key, value)

    def get(self, key: str, default=None):
        return self.memory_engine.memory.get(key, default)

    def snapshot(self) -> Dict[str, Any]:
        return self.memory_engine.snapshot()

    def decay(self) -> None:
        self.memory_engine.decay_all()