from rest_framework import serializers

from api.models import Launch
from api.utils.types.launch_response import LaunchResult


class LaunchLibraryLaunchSerializer(serializers.Serializer[LaunchResult]):
    id = serializers.UUIDField()
    name = serializers.CharField()

    def create(self, validated_data: LaunchResult) -> Launch:
        launch, _ = Launch.objects.update_or_create(
            launch_id=validated_data.id,
            defaults={
                "name": validated_data.name,
                "provider": self.context["provider"],
            },
        )

        return launch
