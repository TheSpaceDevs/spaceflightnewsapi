from typing import TypedDict

from rest_framework import serializers

from api.models import NewsSite, Report


class ValidatedReportDataDict(TypedDict):
    id: serializers.IntegerField
    title: serializers.CharField
    url: serializers.URLField
    imageUrl: serializers.URLField
    newsSite: serializers.CharField
    summary: serializers.CharField
    publishedAt: serializers.DateTimeField
    updatedAt: serializers.DateTimeField


class ReportV3Serializer(serializers.Serializer[Report]):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    imageUrl = serializers.URLField()
    newsSite = serializers.CharField()
    summary = serializers.CharField(allow_blank=True)
    publishedAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()

    def create(self, validated_data: ValidatedReportDataDict) -> Report:
        news_site = NewsSite.objects.get(name=validated_data["newsSite"])

        report, _ = Report.objects.update_or_create(
            id=validated_data.get("id"),
            defaults={
                "title": validated_data.get("title"),
                "url": validated_data.get("url"),
                "image_url": validated_data.get("imageUrl"),
                "news_site": news_site,
                "summary": validated_data.get("summary"),
                "published_at": validated_data.get("publishedAt"),
                "updated_at": validated_data.get("updatedAt"),
            },
        )

        return report
