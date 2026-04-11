from rest_framework import serializers

from api.models.socials import Socials


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:  # pyrefly: ignore[bad-override]
        model = Socials
        fields = ["x", "youtube", "instagram", "linkedin", "mastodon", "bluesky"]
