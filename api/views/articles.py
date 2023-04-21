from rest_framework import viewsets

from api.models import Article
from api.serializers import ArticleSerializer
from api.views.filters import DocsFilter


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        return Article.objects.all().order_by("-published_at")

    serializer_class = ArticleSerializer
    authentication_classes = []
    filterset_class = DocsFilter
