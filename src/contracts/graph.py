from pydantic import BaseModel
from typing import List


class GraphNodeSpec(BaseModel):
    name: str
    module: str


class GraphSpec(BaseModel):
    nodes: List[GraphNodeSpec]