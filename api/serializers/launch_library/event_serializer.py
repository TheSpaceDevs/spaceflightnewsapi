from typing import TypedDict

from rest_framework import serializers

from api.models import Event


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
