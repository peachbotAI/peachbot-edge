import yaml
from pathlib import Path


class Config:
    _config = None

    @classmethod
    def load(cls, path: str = "configs/config.yaml"):
        if cls._config is None:
            with open(Path(path), "r") as f:
                cls._config = yaml.safe_load(f)
        return cls._config

    @classmethod
    def get(cls, key: str, default=None):
        config = cls.load()
        keys = key.split(".")
        value = config

        for k in keys:
            value = value.get(k, {})
        return value or default