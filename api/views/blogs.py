from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import viewsets

from api import models, serializers
from api.views.filters import DocsFilter


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                "launch",
                OpenApiTypes.STR,
                description="Get all documents related to a specific launch. Can be multiple comma-separated values (UUIDs)",
            ),
            OpenApiParameter(
                "event",
                OpenApiTypes.STR,
                description="Get all documents related to a specific event. Can be multiple comma-separated values (IDs)",
            ),
        ]
    ),
)
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    authentication_classes = []
    filterset_class = DocsFilter
