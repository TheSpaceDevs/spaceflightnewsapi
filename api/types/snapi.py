"""
Types to support the migration of old content into this Django project.
"""
from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel


class Launch(BaseModel):
    id: UUID
    provider: str


class Event(BaseModel):
    id: int
    provider: str


class Article(BaseModel):
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: datetime
    updatedAt: datetime
    featured: bool
    launches: List[Launch]
    events: List[Event]


class Blog(BaseModel):
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: datetime
    updatedAt: datetime
    launches: List[Launch]
    events: List[Event]


class Report(BaseModel):
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: datetime
    updatedAt: datetime
