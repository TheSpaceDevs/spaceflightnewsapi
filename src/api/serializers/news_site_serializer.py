from rest_framework import serializers

from api.models import NewsSite


class NewsSiteSerializer(serializers.ModelSerializer):
    class Meta:  # pyrefly: ignore[bad-override]
        model = NewsSite
        fields = ["id", "name"]
