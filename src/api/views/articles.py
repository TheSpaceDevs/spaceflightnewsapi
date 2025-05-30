from django_filters import rest_framework
from rest_framework import viewsets

from api.models import Article
from api.serializers import ArticleSerializer
from api.views.filters import DocsFilter, SearchFilter


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):  # type: ignore
    queryset = (
        Article.objects.exclude(is_deleted=True)
        .prefetch_related("launches", "events", "authors")
        .select_related("news_site")
        .order_by("-published_at")
    )
    serializer_class = ArticleSerializer
    authentication_classes = []
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_class = DocsFilter
    search_fields = ["title", "summary", "news_site__name"]
