from rest_framework import viewsets

from api.models import Article
from api.serializers import ArticleSerializer
from api.views.filters import DocsFilter


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = []
    filterset_class = DocsFilter
