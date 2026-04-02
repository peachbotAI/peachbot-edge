from src.runtime.edge_runtime import EdgeRuntime


def test_priority_memory():
    runtime = EdgeRuntime(core_path="tests/mock_core")
    runtime.initialize()

    runtime.run_cycle()
    state1 = runtime.state.snapshot()

    runtime.run_cycle()
    state2 = runtime.state.snapshot()

    assert isinstance(state2, dict)