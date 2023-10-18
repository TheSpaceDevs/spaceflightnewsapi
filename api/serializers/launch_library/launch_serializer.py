from typing import TypedDict
from uuid import UUID

from rest_framework import serializers

from api.models import Launch


class ValidatedLaunchDataDict(TypedDict):
    id: str | UUID
    name: str


class LaunchLibraryLaunchSerializer(serializers.Serializer[Launch]):
    id = serializers.UUIDField()
    name = serializers.CharField()

    def create(self, validated_data: ValidatedLaunchDataDict) -> Launch:
        launch, _ = Launch.objects.update_or_create(
            launch_id=validated_data["id"],
            defaults={
                "name": validated_data["name"],
                "provider": self.context["provider"],
            },
        )

        return launch
