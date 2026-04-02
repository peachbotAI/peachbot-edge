from src.runtime.edge_runtime import EdgeRuntime


def test_signal_classification():
    runtime = EdgeRuntime(core_path="tests/mock_core")
    runtime.initialize()

    result = runtime.run_cycle()

    assert "input" in result