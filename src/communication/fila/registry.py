from typing import List, Dict, Any


class FILARegistry:
    """
    Simulates shared metadata pool across nodes.
    """

    def __init__(self) -> None:
        self.messages: List[Dict[str, Any]] = []

    def publish(self, message: Dict[str, Any]) -> None:
        self.messages.append(message)

    def get_all(self) -> List[Dict[str, Any]]:
        return self.messages[-10:]  # last N messages