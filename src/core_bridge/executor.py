from typing import Dict, Any, Optional

from src.core_bridge.loader import CoreModuleLoader
from src.contracts.core import CoreInput, CoreOutput


class CoreExecutor:

    def __init__(self, core_path: Optional[str] = None) -> None:
        self.loader = CoreModuleLoader(core_path=core_path)

    def execute(self, module_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        module = self.loader.load(module_name)

        # Validate input
        validated_input = CoreInput(data=data)

        if not hasattr(module, "run"):
            raise AttributeError(f"Module {module_name} missing 'run' method")

        result = module.run(validated_input.model_dump())

        # Validate output
        validated_output = CoreOutput(**result)

        return validated_output.model_dump()