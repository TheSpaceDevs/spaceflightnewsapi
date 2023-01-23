from rest_framework import serializers

from api.models import NewsSite


class NewsSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSite
        fields = ["id", "name"]
