from rest_framework import serializers

from api.models import NewsSite, Report


class ReportSerializer(serializers.ModelSerializer[Report]):
    news_site: "serializers.StringRelatedField[NewsSite]" = serializers.StringRelatedField()

    class Meta:
        model = Report
        fields = [
            "id",
            "title",
            "url",
            "image_url",
            "news_site",
            "summary",
            "published_at",
            "updated_at",
        ]
