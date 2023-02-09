from rest_framework import viewsets

from api import models, serializers
from api.filters import DocsFilter


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    authentication_classes = []
    filterset_class = DocsFilter
