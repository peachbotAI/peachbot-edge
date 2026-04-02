from src.runtime.edge_runtime import EdgeRuntime


def test_fault_tolerance():
    runtime = EdgeRuntime(core_path="tests/mock_core")
    runtime.initialize()

    result = runtime.run_cycle()

    assert isinstance(result, dict)