from typing import TypedDict
from uuid import UUID

from rest_framework import serializers

from api.models import Launch


class ValidatedDataDict(TypedDict):
    id: UUID
    name: str


class LaunchLibraryLaunchSerializer(serializers.Serializer[Launch]):
    id = serializers.UUIDField()
    name = serializers.CharField()

    def create(self, validated_data: ValidatedDataDict) -> Launch:
        result = Launch.objects.update_or_create(
            launch_id=validated_data.get("id"),
            defaults={
                "name": validated_data.get("name"),
                "provider": self.context.get("provider"),
            },
        )

        return result[0]
