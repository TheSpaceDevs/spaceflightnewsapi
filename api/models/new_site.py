from django.db import models


class NewsSite(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
