from typing import Dict, Any
from src.config import Config


class PriorityScorer:

    def __init__(self) -> None:
        self.base = Config.get("priority.base", 1.0)
        self.weights = Config.get("priority.weights", {})

    def score(self, key: str, value: Dict[str, Any]) -> float:
        score = self.base

        if "anomaly" in value:
            score += self.weights.get("anomaly", 0)

        if value.get("memory_seen"):
            score += self.weights.get("memory_seen", 0)

        if len(value) > 3:
            score += self.weights.get("complexity", 0)

        return score