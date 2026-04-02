from src.contracts.core import CoreInput, CoreOutput


def test_core_input_validation():
    payload = CoreInput(data={"a": 1})
    assert payload.data["a"] == 1


def test_core_output_validation():
    output = CoreOutput(data={"result": 42})
    assert output.status == "ok"