from typing import Optional

from src.runtime.graph.conditional import Condition


class ExecutionNode:
    """
    Node with optional conditional branching.
    """

    def __init__(
        self,
        name: str,
        module: str,
        condition: Optional[Condition] = None,
        next_true: Optional[str] = None,
        next_false: Optional[str] = None
    ) -> None:
        self.name = name
        self.module = module
        self.condition = condition
        self.next_true = next_true
        self.next_false = next_false