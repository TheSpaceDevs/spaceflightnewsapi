from django_filters import rest_framework
from rest_framework import viewsets

from api.models import Blog
from api.serializers import BlogSerializer
from api.views.filters import DocsFilter, SearchFilter


class BlogViewSet(viewsets.ReadOnlyModelViewSet):  # type: ignore
    queryset = (
        Blog.objects.exclude(is_deleted=True)
        .prefetch_related("launches", "events")
        .select_related("news_site")
        .order_by("-published_at")
    )
    serializer_class = BlogSerializer
    authentication_classes = []
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_class = DocsFilter
    search_fields = ["title", "summary", "news_site__name"]
