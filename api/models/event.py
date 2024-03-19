from typing import Literal

from django.db import models


class Event(models.Model):
    event_id = models.IntegerField()
    name = models.CharField(max_length=250)
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def autocomplete_search_fields() -> tuple[Literal["name"], Literal["event_id"]]:
        return ("name", "event_id")
