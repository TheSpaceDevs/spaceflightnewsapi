from rest_framework import serializers

from api.models import Event
from api.utils.types.event_response import EventResult


class LaunchLibraryEventSerializer(serializers.Serializer[EventResult]):
    id = serializers.IntegerField()
    name = serializers.CharField()

    def create(self, validated_data: EventResult) -> Event:
        event, _ = Event.objects.update_or_create(
            event_id=validated_data.id,
            defaults={
                "name": validated_data.name,
                "provider": self.context["provider"],
            },
        )

        return event
