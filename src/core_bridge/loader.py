import importlib
import sys
from typing import Any, Optional

from src.monitoring.logger import get_logger

logger = get_logger(__name__)


class CoreModuleLoader:
    """
    Dynamically loads modules from peachbot-core.
    """

    def __init__(self, core_path: Optional[str] = None) -> None:
        if core_path and core_path not in sys.path:
            sys.path.insert(0, core_path)
            logger.info(f"Added core path: {core_path}")

        self.base_path = "core.modules"

    def load(self, module_name: str) -> Any:
        try:
            module_path = f"{self.base_path}.{module_name}.module"
            logger.info(f"Loading core module: {module_path}")

            module = importlib.import_module(module_path)
            return module

        except Exception as e:
            logger.error(f"Failed to load module: {module_name}")
            raise e