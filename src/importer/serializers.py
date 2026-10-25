from datetime import datetime
from typing import TypedDict
from uuid import UUID

from rest_framework import serializers


class ValidatedLaunchDataDict(TypedDict):
    id: UUID
    name: str
    last_updated: datetime


class LaunchLibraryLaunchSerializer(serializers.Serializer[ValidatedLaunchDataDict]):
    id = serializers.UUIDField()
    name = serializers.CharField()
    last_updated = serializers.DateTimeField()


class ValidatedEventDataDict(TypedDict):
    id: int
    name: str
    last_updated: datetime


class LaunchLibraryEventSerializer(serializers.Serializer[ValidatedEventDataDict]):
    id = serializers.IntegerField()
    name = serializers.CharField()
    last_updated = serializers.DateTimeField()
