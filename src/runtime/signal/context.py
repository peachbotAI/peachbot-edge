from typing import Dict, Any


class ContextBuilder:
    """
    Builds execution context from signal + memory.
    """

    def build(self, signal_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        context = {
            "signal_type": signal_type,
            "priority": "high" if signal_type == "critical" else "medium"
        }

        if signal_type == "anomaly":
            context["priority"] = "elevated"

        return context