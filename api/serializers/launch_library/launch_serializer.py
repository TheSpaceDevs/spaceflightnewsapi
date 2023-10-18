from typing import TypedDict
from uuid import UUID

from rest_framework import serializers

from api.models import Launch


class ValidatedLaunchDataDict(TypedDict):
    id: serializers.UUIDField
    name: serializers.CharField


class LaunchLibraryLaunchSerializer(serializers.Serializer[Launch]):
    id = serializers.UUIDField()
    name = serializers.CharField()

    def create(self, validated_data: ValidatedLaunchDataDict) -> Launch:
        launch, _ = Launch.objects.update_or_create(
            launch_id=validated_data.get("id"),
            defaults={
                "name": validated_data.get("name"),
                "provider": self.context.get("provider"),
            },
        )

        return launch
