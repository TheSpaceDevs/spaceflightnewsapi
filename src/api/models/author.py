from django.db import models

from api.models.socials import Socials


class Author(models.Model):
    name = models.CharField(max_length=250)
    socials = models.ForeignKey(Socials, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
