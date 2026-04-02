from typing import Dict, Any, Callable


class Condition:
    """
    Represents a branching condition.
    """

    def __init__(self, fn: Callable[[Dict[str, Any]], bool]) -> None:
        self.fn = fn

    def evaluate(self, data: Dict[str, Any]) -> bool:
        return self.fn(data)