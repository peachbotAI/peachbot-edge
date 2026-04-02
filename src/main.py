from src.runtime.edge_runtime import EdgeRuntime
from src.monitoring.logger import get_logger
from src.monitoring.banner import show_banner

import os

logger = get_logger(__name__)


def main() -> None:
    show_banner()

    logger.info("Booting PeachBot Edge Runtime...")

    core_path = os.path.abspath("tests/mock_core")

    runtime = EdgeRuntime(core_path=core_path)
    runtime.initialize()

    logger.info("System ready. Starting execution cycle...")

    runtime.run_cycle()

    logger.info("Execution completed.\n")


if __name__ == "__main__":
    main()