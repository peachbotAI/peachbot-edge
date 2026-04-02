from typing import Dict, Any


class FILAMessage:
    """
    Metadata-only message (NO raw data).
    """

    def __init__(self, node: str, signal_type: str, priority: str):
        self.node = node
        self.signal_type = signal_type
        self.priority = priority

    def to_dict(self) -> Dict[str, Any]:
        return {
            "node": self.node,
            "signal_type": self.signal_type,
            "priority": self.priority
        }