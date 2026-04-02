from typing import Any, Callable
from src.config import Config
import threading



class ExecutionGuard:

    def __init__(self, timeout: int = 2) -> None:
        self.timeout = timeout or Config.get("runtime.timeout", 2)

    def run(self, fn: Callable, *args, **kwargs) -> Any:
        result = {}
        exception = {}

        def target():
            try:
                result["value"] = fn(*args, **kwargs)
            except Exception as e:
                exception["error"] = e

        thread = threading.Thread(target=target)
        thread.start()
        thread.join(self.timeout)

        if thread.is_alive():
            raise RuntimeError("Execution timed out")

        if "error" in exception:
            raise RuntimeError(f"Execution failed: {exception['error']}")

        return result.get("value")