from typing import Dict, Any, List

from src.communication.fila.schema import FILAMessage
from src.communication.fila.registry import FILARegistry


class FILAAdapter:

    def __init__(self) -> None:
        self.registry = FILARegistry()

    def publish(self, node: str, context: Dict[str, Any]) -> None:
        message = FILAMessage(
            node=node,
            signal_type=context.get("signal_type"),
            priority=context.get("priority")
        )

        self.registry.publish(message.to_dict())

    def fetch(self) -> List[Dict[str, Any]]:
        return self.registry.get_all()