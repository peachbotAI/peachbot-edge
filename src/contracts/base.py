from pydantic import BaseModel, Field
from typing import Any, Dict


class BasePayload(BaseModel):
    """
    Base structure for all data flowing through the system.
    """

    metadata: Dict[str, Any] = Field(default_factory=dict)
    data: Dict[str, Any] = Field(default_factory=dict)