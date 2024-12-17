from pydantic import BaseModel
from typing import List

class NodeData(BaseModel):
    value: int

class UpdateNodeData(BaseModel):
    target_value: int
    new_value: int

class LinkedListResponse(BaseModel):
    nodes: List[int]
