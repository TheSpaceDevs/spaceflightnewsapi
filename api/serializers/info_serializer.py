from rest_framework import serializers


class InfoSerializer(serializers.Serializer):
    version = serializers.CharField()
    news_sites = serializers.ListField(child=serializers.CharField())
