from typing import Any

from django.contrib.postgres.indexes import GinIndex, OpClass
from django.db import models
from django.db.models.functions import Upper

from api.models.author import Author
from api.models.event import Event
from api.models.launch import Launch
from api.models.news_site import NewsSite


class NewsItem(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    url = models.URLField(unique=True)
    image_url = models.URLField(max_length=500)
    news_site = models.ForeignKey(NewsSite, on_delete=models.CASCADE)
    summary = models.TextField()
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    launches = models.ManyToManyField(Launch, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    is_deleted = models.BooleanField(default=False)
    authors = models.ManyToManyField(Author, blank=True)
    audited = models.BooleanField(default=False)

    class Meta:
        abstract = True
        # Partial indexes matching the API's `exclude(is_deleted=True)` + `order_by(...)` list queries.
        indexes = [
            models.Index(fields=["-published_at"], name="%(class)s_published_idx", condition=models.Q(is_deleted=False)),
            models.Index(fields=["-updated_at"], name="%(class)s_updated_idx", condition=models.Q(is_deleted=False)),
            # Trigram indexes for `icontains` filters and search, which Django compiles to `UPPER(col) LIKE UPPER(...)`.
            GinIndex(OpClass(Upper("title"), name="gin_trgm_ops"), name="%(class)s_title_trgm_idx"),
            GinIndex(OpClass(Upper("summary"), name="gin_trgm_ops"), name="%(class)s_summary_trgm_idx"),
        ]

    def __str__(self) -> str:
        return self.title

    def delete(self, using: Any = ..., keep_parents: bool = ...) -> None:  # type: ignore
        """Mark the item as delete instead of actually deleting it."""
        self.is_deleted = True
        self.save()
