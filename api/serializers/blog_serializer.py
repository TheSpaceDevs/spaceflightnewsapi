from rest_framework import serializers

from api.models import Blog
from api.serializers.event_serializer import EventSerializer
from api.serializers.launch_serializer import LaunchSerializer


class BlogSerializer(serializers.ModelSerializer):
    news_site = serializers.StringRelatedField()
    launches = LaunchSerializer(many=True)
    events = EventSerializer(many=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "url",
            "image_url",
            "news_site",
            "summary",
            "published_at",
            "updated_at",
            "featured",
            "launches",
            "events",
        ]
