from rest_framework import serializers

from api.models.author import Author
from api.serializers.socials_serializer import SocialsSerializer


class AuthorSerializer(serializers.ModelSerializer[Author]):
    socials = SocialsSerializer(required=False)

    class Meta:
        model = Author
        fields = ["name", "socials"]
