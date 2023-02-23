from rest_framework import viewsets

from api import models, serializers
from api.views.filters import DocsFilter


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    authentication_classes = []
    filterset_class = DocsFilter
