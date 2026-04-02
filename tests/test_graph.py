from src.runtime.edge_runtime import EdgeRuntime


def test_graph_execution():
    runtime = EdgeRuntime(core_path="tests/mock_core")
    runtime.initialize()

    result = runtime.run_cycle()

    assert result["engine"] == "SBC"
    assert "input" in result