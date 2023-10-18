from rest_framework import serializers


# The type is set to None since it's not bound to a model and isn't used to deserialize data.
class InfoSerializer(serializers.Serializer[None]):
    version = serializers.CharField()
    news_sites = serializers.ListField(child=serializers.CharField())
