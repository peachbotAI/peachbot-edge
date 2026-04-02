from src.runtime.sbc_engine.engine import SBCEngine


def test_sbc_engine_load():
    engine = SBCEngine()
    engine.initialize()

    assert engine.ready is True

