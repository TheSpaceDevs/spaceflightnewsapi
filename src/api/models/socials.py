from django.db import models


class Socials(models.Model):
    x = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    bluesky = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    mastodon = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Socials"

    def __str__(self) -> str:
        return self.x
