from typing import Dict, Any

from src.runtime.graph.graph import ExecutionGraph
from src.core_bridge.executor import CoreExecutor
from src.contracts.base import BasePayload
from src.runtime.state.manager import StateManager
from src.monitoring.logger import get_logger

# STEP 9
from src.runtime.signal.classifier import SignalClassifier
from src.runtime.signal.context import ContextBuilder

# STEP 10
from src.runtime.safety.guard import ExecutionGuard
from src.runtime.safety.fallback import FallbackHandler

# STEP 11
from src.runtime.hardware.profiler import HardwareProfile
from src.runtime.hardware.manager import HardwareManager

# STEP 12
from src.communication.fila.adapter import FILAAdapter


logger = get_logger(__name__)


class GraphExecutor:

    def __init__(self, core_executor: CoreExecutor, state: StateManager) -> None:
        self.core_executor = core_executor
        self.state = state

        # STEP 9 — Signal + Context
        self.classifier = SignalClassifier()
        self.context_builder = ContextBuilder()

        # STEP 10 — Safety
        self.guard = ExecutionGuard()
        self.fallback = FallbackHandler()

        # STEP 11 — Hardware
        self.hw_profiler = HardwareProfile()
        self.hw_manager = HardwareManager()

        # STEP 12 — Federation
        self.fila = FILAAdapter()

    def execute(self, graph: ExecutionGraph, initial_data: Dict[str, Any]) -> Dict[str, Any]:

        payload = BasePayload(data={
            **initial_data,
            "memory": self.state.snapshot()
        })

        current_node_name = graph.start

        while current_node_name:
            node = graph.get_node(current_node_name)

            logger.info(f"Executing node: {node.name} ({node.module})")

            # ---------------------------
            # STEP 9 — SIGNAL + CONTEXT
            # ---------------------------
            signal_type = self.classifier.classify(payload.data)
            context = self.context_builder.build(signal_type, payload.data)

            # ---------------------------
            # STEP 11 — HARDWARE
            # ---------------------------
            profile = self.hw_profiler.get()
            mode = self.hw_manager.decide_mode(profile)

            logger.info(
                f"[HW] Mode: {mode} | CPU: {profile['cpu_percent']}% | MEM: {profile['memory_percent']}%"
            )

            # ---------------------------
            # STEP 12 — FILA (metadata only)
            # ---------------------------
            self.fila.publish(node.name, context)
            global_meta = self.fila.fetch()

            # ---------------------------
            # BUILD EXECUTION INPUT
            # ---------------------------
            execution_input = {
                **payload.data,
                "context": context,
                "hardware": {
                    "mode": mode,
                    "profile": profile
                },
                "federation": {
                    "global_context": global_meta
                }
            }

            # ---------------------------
            # STEP 10 — SAFE EXECUTION
            # ---------------------------
            try:
                result = self.guard.run(
                    self.core_executor.execute,
                    node.module,
                    execution_input
                )
            except Exception as e:
                logger.error(f"Node failed: {node.name} → {str(e)}")
                result = self.fallback.handle(node.name, str(e))

            # ---------------------------
            # MEMORY UPDATE
            # ---------------------------
            self.state.update(node.name, result["data"])

            # ---------------------------
            # PAYLOAD PROPAGATION (CRITICAL)
            # ---------------------------
            payload = BasePayload(data={
                **payload.data,
                **result["data"],
                "memory": self.state.snapshot()
            })

            # ---------------------------
            # CONDITIONAL BRANCHING
            # ---------------------------
            if node.condition:
                condition_result = node.condition.evaluate(payload.data)
                current_node_name = node.next_true if condition_result else node.next_false
            else:
                current_node_name = None

        return payload.model_dump()