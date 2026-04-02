from src.runtime.edge_runtime import EdgeRuntime
from src.runtime.edge_runtime import EdgeRuntime


def test_runtime_cycle():
    runtime = EdgeRuntime()
    runtime.initialize()

    result = runtime.run_cycle()

    assert result["status"] == "processed"
    assert result["engine"] == "SBC"



def test_full_cycle_with_core():
    runtime = EdgeRuntime()
    runtime.initialize()

    result = runtime.run_cycle()

    assert result["engine"] == "SBC"
    assert "input" in result