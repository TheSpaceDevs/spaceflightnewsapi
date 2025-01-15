from rest_framework import serializers

from api.models.socials import Socials


class SocialsSerializer(serializers.ModelSerializer[Socials]):
    class Meta:
        model = Socials
        fields = ["x", "youtube", "instagram", "linkedin", "mastodon", "bluesky"]
