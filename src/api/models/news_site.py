from typing import Literal

from django.db import models


class NewsSite(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def autocomplete_search_fields() -> tuple[Literal["name"],]:
        return ("name",)
