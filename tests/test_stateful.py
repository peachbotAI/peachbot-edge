from src.runtime.edge_runtime import EdgeRuntime


def test_state_persistence():
    runtime = EdgeRuntime(core_path="tests/mock_core")
    runtime.initialize()

    runtime.run_cycle()
    state_after_first = runtime.state.snapshot()

    runtime.run_cycle()
    state_after_second = runtime.state.snapshot()

    assert len(state_after_second) >= len(state_after_first)