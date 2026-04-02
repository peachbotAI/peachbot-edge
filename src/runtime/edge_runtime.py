from typing import Optional, Dict, Any

from src.runtime.sbc_engine.engine import SBCEngine
from src.core_bridge.executor import CoreExecutor
from src.runtime.graph.graph import ExecutionGraph
from src.runtime.graph.node import ExecutionNode
from src.runtime.graph.executor import GraphExecutor
from src.runtime.graph.graph import ExecutionGraph
from src.runtime.graph.node import ExecutionNode
from src.runtime.graph.executor import GraphExecutor
from src.runtime.graph.conditional import Condition
from src.runtime.state.manager import StateManager
from src.monitoring.logger import get_logger

logger = get_logger(__name__)


class EdgeRuntime:

    def __init__(self, core_path: Optional[str] = None) -> None:
        self.sbc_engine: Optional[SBCEngine] = None
        self.core_executor: Optional[CoreExecutor] = None
        self.state = StateManager()
        self.core_path = core_path
        self.initialized: bool = False

    def initialize(self) -> None:
        logger.info("Initializing Edge Runtime...")

        self.sbc_engine = SBCEngine()
        self.sbc_engine.initialize()

        self.core_executor = CoreExecutor(core_path=self.core_path)

        self.initialized = True
        logger.info("Edge Runtime initialized successfully.")

    def run_cycle(self) -> Dict[str, Any]:
        if not self.initialized:
            raise RuntimeError("Runtime not initialized")

        logger.info("Running execution cycle (adaptive graph)...")

        # Define condition
        def check_signal(data):
            return "trigger" in data.get("signal", "")

        graph = ExecutionGraph(
            nodes={
                "start": ExecutionNode(
                    name="start",
                    module="medai",
                    condition=Condition(check_signal),
                    next_true="branch_a",
                    next_false="branch_b"
                ),
                "branch_a": ExecutionNode(
                    name="branch_a",
                    module="medai"
                ),
                "branch_b": ExecutionNode(
                    name="branch_b",
                    module="medai"
                )
            },
            start="start"
        )

        graph_executor = GraphExecutor(self.core_executor, self.state)

        core_result = graph_executor.execute(
            graph=graph,
            initial_data={"signal": "trigger_event"}
        )

        result = self.sbc_engine.process(core_result)

        logger.info(f"State Snapshot: {self.state.snapshot()}")

        logger.info("Execution cycle completed.")
        self.state.decay()
        return result