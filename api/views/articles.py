from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import viewsets

from api.models import Article
from api.serializers import ArticleSerializer
from api.views.filters import DocsFilter


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                "news_site",
                OpenApiTypes.STR,
                description="Search for documents by a specific news site. Case sensitive.",
            ),
            OpenApiParameter(
                "launch",
                OpenApiTypes.UUID,
                description="Get all documents related to a specific launch.",
            ),
        ]
    ),
)
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = []
    filterset_class = DocsFilter
