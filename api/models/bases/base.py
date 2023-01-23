from django.db import models

from api.models.event import Event
from api.models.launch import Launch


class Base(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    image_url = models.URLField()
    news_site = models.ForeignKey("NewsSite", on_delete=models.CASCADE)
    summary = models.TextField()
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    featured = models.BooleanField(default=False)
    launches = models.ManyToManyField(Launch, blank=True)
    events = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        return self.title
