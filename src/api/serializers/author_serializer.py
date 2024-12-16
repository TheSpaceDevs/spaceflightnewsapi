from rest_framework import serializers

from api.models.author import Author


class AuthorSerializer(serializers.ModelSerializer[Author]):
    class Meta:
        model = Author
        fields = ["name"]
