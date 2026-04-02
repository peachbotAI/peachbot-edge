from pydantic import BaseModel
from typing import Dict, Any


class CoreInput(BaseModel):
    data: Dict[str, Any]


class CoreOutput(BaseModel):
    data: Dict[str, Any]
    status: str = "ok"