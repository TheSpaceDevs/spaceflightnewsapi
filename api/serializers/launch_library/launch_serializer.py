from typing import Dict

from rest_framework import serializers
from api.models import Launch
from api.utils.types.launch_response import LaunchResult


class LaunchLibraryLaunchSerializer(serializers.Serializer[LaunchResult]):
    id = serializers.UUIDField()
    name = serializers.CharField()

    def create(self, validated_data) -> LaunchResult:
        return LaunchResult(**validated_data)

    def create_launch(self) -> tuple[Launch, bool]:
        return Launch.objects.update_or_create(
            launch_id=self.validated_data.id,
            defaults={
                "name": self.validated_data.name,
                "provider": self.context["provider"],
            },
        )

