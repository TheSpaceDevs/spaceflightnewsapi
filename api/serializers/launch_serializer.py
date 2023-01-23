from rest_framework import serializers

from api.models import Launch


class LaunchSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField()

    class Meta:
        model = Launch
        fields = ["launch_id", "provider"]
