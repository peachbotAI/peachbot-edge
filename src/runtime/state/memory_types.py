from typing import Dict, Any
from src.config import Config


class MemoryEntry:

    def __init__(self, value: Dict[str, Any], priority: float = 1.0) -> None:
        self.value = value
        self.strength = priority
        self.age = 0

        self.decay_weak = Config.get("memory.decay.weak", 0.9)
        self.decay_strong = Config.get("memory.decay.strong", 0.95)
        self.threshold = Config.get("memory.threshold.removal", 0.3)

    def reinforce(self, amount: float = 1.0):
        self.strength += amount

    def decay(self):
        self.age += 1

        decay_factor = self.decay_weak if self.strength < 2 else self.decay_strong
        self.strength *= decay_factor

    def is_weak(self) -> bool:
        return self.strength < self.threshold