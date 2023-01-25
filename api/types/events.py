from typing import List

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    url: str
    name: str


class LlResponse(BaseModel):
    count: int
    next: str
    previous: None
    results: List[Event]
