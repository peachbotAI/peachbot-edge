from typing import Dict


class HardwareManager:
    """
    Decides execution mode based on hardware state.
    """

    def decide_mode(self, profile: Dict) -> str:
        cpu = profile["cpu_percent"]
        memory = profile["memory_percent"]

        if cpu > 80 or memory > 80:
            return "safe"

        if cpu > 50:
            return "balanced"

        return "performance"