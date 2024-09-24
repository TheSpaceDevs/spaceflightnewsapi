from typing import Literal

from django.db import models


class Launch(models.Model):
    launch_id = models.UUIDField(unique=True)
    name = models.CharField(max_length=250)
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Launches"

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def autocomplete_search_fields() -> tuple[Literal["name"], Literal["launch_id"]]:
        return ("name", "launch_id")
