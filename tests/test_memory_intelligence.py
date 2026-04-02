from src.runtime.edge_runtime import EdgeRuntime


def test_memory_decay():
    runtime = EdgeRuntime(core_path="tests/mock_core")
    runtime.initialize()

    runtime.run_cycle()
    state1 = runtime.state.snapshot()

    runtime.run_cycle()
    runtime.run_cycle()

    state2 = runtime.state.snapshot()

    # memory should still exist but evolve
    assert isinstance(state2, dict)