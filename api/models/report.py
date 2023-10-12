from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    image_url = models.URLField()
    news_site = models.ForeignKey("NewsSite", on_delete=models.CASCADE)
    summary = models.TextField(blank=True)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-published_at"]
