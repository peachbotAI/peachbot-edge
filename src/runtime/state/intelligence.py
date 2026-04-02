from typing import Dict, Any

from src.runtime.state.memory_types import MemoryEntry
from src.runtime.state.priority import PriorityScorer


class MemoryIntelligence:

    def __init__(self) -> None:
        self.memory: Dict[str, MemoryEntry] = {}
        self.scorer = PriorityScorer()

    def update(self, key: str, value: Dict[str, Any]) -> None:
        priority = self.scorer.score(key, value)

        if key in self.memory:
            self.memory[key].reinforce(priority)
            self.memory[key].value = value
        else:
            self.memory[key] = MemoryEntry(value, priority)

    def decay_all(self) -> None:
        for key in list(self.memory.keys()):
            entry = self.memory[key]
            entry.decay()

            if entry.is_weak():
                del self.memory[key]

    def snapshot(self) -> Dict[str, Any]:
        return {
            key: entry.value for key, entry in self.memory.items()
        }