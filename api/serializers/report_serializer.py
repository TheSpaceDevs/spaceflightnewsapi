from rest_framework import serializers

from api.models import Blog


class ReportSerializer(serializers.ModelSerializer):
    news_site = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = ["id", "title", "url", "image_url", "news_site", "summary", "published_at", "updated_at"]
