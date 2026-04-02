from typing import Dict, Any


class SignalClassifier:
    """
    Classifies incoming signals into types.
    """

    def classify(self, data: Dict[str, Any]) -> str:
        signal = data.get("signal", "")

        if "critical" in signal:
            return "critical"

        if "anomaly" in signal:
            return "anomaly"

        return "normal"