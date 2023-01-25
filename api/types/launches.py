from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class Launch(BaseModel):
    id: UUID
    url: str
    name: str


class LlResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Launch]
