from src.runtime.edge_runtime import EdgeRuntime


def test_runtime_initialization():
    runtime = EdgeRuntime()
    runtime.initialize()

    assert runtime.initialized is True
    assert runtime.sbc_engine is not None