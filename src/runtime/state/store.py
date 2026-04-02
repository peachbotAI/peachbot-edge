from typing import Dict, Any


class StateStore:
    """
    Simple in-memory state store.
    Future: persistent / edge storage
    """

    def __init__(self) -> None:
        self._store: Dict[str, Any] = {}

    def get(self, key: str, default=None):
        return self._store.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._store[key] = value

    def dump(self) -> Dict[str, Any]:
        return self._store.copy()