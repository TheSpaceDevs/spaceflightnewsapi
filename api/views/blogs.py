from rest_framework import viewsets

from api.models import Blog
from api.serializers import BlogSerializer
from api.views.filters import DocsFilter


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = []
    filterset_class = DocsFilter
