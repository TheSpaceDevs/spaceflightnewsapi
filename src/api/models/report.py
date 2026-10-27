from typing import Any

from django.contrib.postgres.indexes import GinIndex, OpClass
from django.db import models
from django.db.models.functions import Upper

from api.models.author import Author


class Report(models.Model):
    title = models.CharField(max_length=500, db_index=True)
    url = models.URLField(max_length=500, db_index=True)
    image_url = models.URLField(max_length=500)
    news_site = models.ForeignKey("NewsSite", on_delete=models.CASCADE)
    summary = models.TextField(blank=True)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    authors = models.ManyToManyField(Author, blank=True)

    class Meta:
        ordering = ["-published_at"]
        # Partial indexes matching the API's `exclude(is_deleted=True)` + `order_by(...)` list queries.
        indexes = [
            models.Index(fields=["-published_at"], name="report_published_idx", condition=models.Q(is_deleted=False)),
            models.Index(fields=["-updated_at"], name="report_updated_idx", condition=models.Q(is_deleted=False)),
            # Trigram indexes for `icontains` filters and search, which Django compiles to `UPPER(col) LIKE UPPER(...)`.
            GinIndex(OpClass(Upper("title"), name="gin_trgm_ops"), name="report_title_trgm_idx"),
            GinIndex(OpClass(Upper("summary"), name="gin_trgm_ops"), name="report_summary_trgm_idx"),
        ]

    def __str__(self) -> str:
        return self.title

    def delete(self, using: Any = ..., keep_parents: bool = ...) -> None:  # type: ignore
        """Mark the item as delete instead of actually deleting it."""
        self.is_deleted = True
        return self.save()
