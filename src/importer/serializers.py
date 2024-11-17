from typing import TypedDict

from rest_framework import serializers

from api.models import Event, Launch


class ValidatedLaunchDataDict(TypedDict):
    id: str
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


class ValidatedEventDataDict(TypedDict):
    id: int
    name: str


class LaunchLibraryEventSerializer(serializers.Serializer[Event]):
    id = serializers.IntegerField()
    name = serializers.CharField()

    def create(self, validated_data: ValidatedEventDataDict) -> Event:
        event, _ = Event.objects.update_or_create(
            event_id=validated_data["id"],
            defaults={
                "name": validated_data["name"],
                "provider": self.context["provider"],
            },
        )

        return event
