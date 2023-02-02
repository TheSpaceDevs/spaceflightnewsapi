from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from api import models, serializers
from api.filters import DocsFilter


@extend_schema(tags=["blogs"])
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    filterset_class = DocsFilter
