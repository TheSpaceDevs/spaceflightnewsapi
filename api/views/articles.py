from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from api import models, serializers
from api.filters import DocsFilter


@extend_schema(tags=["articles"])
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    filterset_class = DocsFilter
