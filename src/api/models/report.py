from typing import Any

from django.db import models

from api.models.author import Author


class Report(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    image_url = models.URLField()
    news_site = models.ForeignKey("NewsSite", on_delete=models.CASCADE)
    summary = models.TextField(blank=True)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    authors = models.ManyToManyField(Author, blank=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self) -> str:
        return self.title

    def delete(self, using: Any = ..., keep_parents: bool = ...) -> None:  # type: ignore
        """Mark the item as delete instead of actually deleting it."""
        self.is_deleted = True
        return self.save()
