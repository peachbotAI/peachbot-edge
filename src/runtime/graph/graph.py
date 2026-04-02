from typing import Dict

from src.runtime.graph.node import ExecutionNode


class ExecutionGraph:
    """
    Graph with named nodes (not just list).
    """

    def __init__(self, nodes: Dict[str, ExecutionNode], start: str) -> None:
        self.nodes = nodes
        self.start = start

    def get_node(self, name: str) -> ExecutionNode:
        return self.nodes[name]