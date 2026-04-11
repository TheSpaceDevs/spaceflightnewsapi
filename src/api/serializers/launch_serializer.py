from rest_framework import serializers

from api.models import Launch


class LaunchSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField()

    class Meta:  # pyrefly: ignore[bad-override]
        model = Launch
        fields = ["launch_id", "provider"]
