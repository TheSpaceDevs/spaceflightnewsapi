from rest_framework import serializers

from api.models import NewsSite, Report
from api.serializers.author_serializer import AuthorSerializer


class ReportSerializer(serializers.ModelSerializer[Report]):
    news_site: "serializers.StringRelatedField[NewsSite]" = serializers.StringRelatedField()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Report
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
        ]
