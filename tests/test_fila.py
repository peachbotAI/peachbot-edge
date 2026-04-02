from src.runtime.edge_runtime import EdgeRuntime


def test_fila_metadata_flow():
    runtime = EdgeRuntime(core_path="tests/mock_core")
    runtime.initialize()

    result = runtime.run_cycle()

    assert isinstance(result, dict)