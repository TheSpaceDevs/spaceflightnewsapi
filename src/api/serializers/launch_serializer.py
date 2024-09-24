from rest_framework import serializers

from api.models import Launch, Provider


class LaunchSerializer(serializers.ModelSerializer[Launch]):
    provider: "serializers.StringRelatedField[Provider]" = serializers.StringRelatedField()

    class Meta:
        model = Launch
        fields = ["launch_id", "provider"]
