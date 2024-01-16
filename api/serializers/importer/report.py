from typing import Any

from rest_framework import serializers

from api.models import NewsSite, Report


class ReportImportSerializer(serializers.Serializer[Report]):
    title = serializers.CharField()
    url = serializers.URLField()
    imageUrl = serializers.URLField()
    newsSite = serializers.IntegerField()
    summary = serializers.CharField(allow_blank=True)
    publishedAt = serializers.DateTimeField()

    def create(self, validated_data: dict[str, Any]) -> Report:
        news_site = NewsSite.objects.get(id=validated_data["newsSite"])

        report, _ = Report.objects.update_or_create(
            url=validated_data["url"],
            defaults={
                "title": validated_data["title"],
                "image_url": validated_data["imageUrl"],
                "news_site": news_site,
                "summary": validated_data["summary"],
                "published_at": validated_data["publishedAt"],
            },
        )

        return report
