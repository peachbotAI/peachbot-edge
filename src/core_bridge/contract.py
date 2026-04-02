from typing import Protocol, Dict, Any


class CoreModuleContract(Protocol):
    """
    Defines how core modules must behave.
    This ensures edge can execute them safely.
    """

    def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        ...