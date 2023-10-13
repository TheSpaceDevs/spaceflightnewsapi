from django_filters import rest_framework
from rest_framework import filters, viewsets

from api.models import Blog
from api.serializers import BlogSerializer
from api.views.filters import DocsFilter, SearchFilter


class BlogViewSet(viewsets.ReadOnlyModelViewSet):  # type: ignore
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = []
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = DocsFilter
    search_fields = ["title", "summary", "news_site__name"]
    ordering = ["-published_at"]
    ordering_fields = ["published_at", " updated_at"]
