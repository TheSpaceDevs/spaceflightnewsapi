from rest_framework import serializers

from api.models import Event


class EventSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ["event_id", "provider"]
