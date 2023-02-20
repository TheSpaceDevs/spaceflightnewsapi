from rest_framework import serializers

from api.models import NewsSite, Report


class ReportV3Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    imageUrl = serializers.URLField()
    newsSite = serializers.CharField()
    summary = serializers.CharField(allow_blank=True)
    publishedAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()

    def create(self, validated_data):
        news_site = NewsSite.objects.get(name=validated_data["newsSite"])

        return Report.objects.update_or_create(
            id=validated_data["id"],
            title=validated_data["title"],
            url=validated_data["url"],
            image_url=validated_data["imageUrl"],
            news_site=news_site,
            summary=validated_data["summary"],
            published_at=validated_data["publishedAt"],
            updated_at=validated_data["updatedAt"],
        )
