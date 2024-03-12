from rest_framework import serializers

from api.models import Event, Provider


class EventSerializer(serializers.ModelSerializer[Event]):
    provider: "serializers.StringRelatedField[Provider]" = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ["event_id", "provider"]
