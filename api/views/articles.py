from django_filters import rest_framework
from rest_framework import filters, viewsets

from api.models import Article
from api.serializers import ArticleSerializer
from api.views.filters import DocsFilter


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = []
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = DocsFilter
    search_fields = ["title", "summary"]
