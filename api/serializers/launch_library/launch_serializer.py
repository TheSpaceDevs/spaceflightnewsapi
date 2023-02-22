from rest_framework import serializers

from api.models import Launch


class LaunchLibraryLaunchSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()

    def create(self, validated_data) -> Launch:
        launch, _ = Launch.objects.update_or_create(
            launch_id=validated_data["id"],
            defaults={
                "name": validated_data["name"],
                "provider": self.context["provider"],
            },
        )

        return launch
