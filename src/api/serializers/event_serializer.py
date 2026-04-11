from rest_framework import serializers

from api.models import Event


class EventSerializer(serializers.ModelSerializer[Event]):
    provider = serializers.StringRelatedField()

    class Meta:  # pyrefly: ignore[bad-override]
        model = Event
        fields = ["event_id", "provider"]
