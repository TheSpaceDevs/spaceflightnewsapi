from rest_framework import serializers

from api.models import Blog, NewsSite
from api.serializers.author_serializer import AuthorSerializer
from api.serializers.event_serializer import EventSerializer
from api.serializers.launch_serializer import LaunchSerializer


class BlogSerializer(serializers.ModelSerializer[Blog]):
    news_site: "serializers.StringRelatedField[NewsSite]" = serializers.StringRelatedField()
    launches = LaunchSerializer(many=True)
    events = EventSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "authors",
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
