import operator
from functools import reduce

from django.db.models import Q
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
                "launch",
                OpenApiTypes.UUID,
                description="Get all documents related to a specific launch.",
            ),
            OpenApiParameter(
                "news_site",
                OpenApiTypes.STR,
                description="Search for articles from various news sites. Can be multiple comma-separated sites. Case "
                            "sensitive.",
            ),
        ]
    ),
)
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        articles = Article.objects.all()

        news_sites_filters = self.request.query_params.get("news_site", None)
        launches_filters = self.request.query_params.get("launches", None)
        events_filters = self.request.query_params.get("events", None)
        title_contains_all_filters = self.request.query_params.get("title_contains_all", None)
        title_contains_one_filters = self.request.query_params.get("title_contains_one", None)
        summary_contains_all_filters = self.request.query_params.get("summary_contains_all", None)
        summary_contains_one_filters = self.request.query_params.get("summary_contains_one", None)

        if news_sites_filters:
            news_sites_filters = news_sites_filters.split(",")
            articles = articles.filter(news_site__name__in=news_sites_filters)
        if launches_filters:
            launches_filters = launches_filters.split(",")
            articles = articles.filter(launches__launch_id__in=launches_filters)
        if events_filters:
            events_filters = events_filters.split(",")
            articles = articles.filter(events__event_id__in=events_filters)
        if title_contains_all_filters:
            title_contains_all_filters = title_contains_all_filters.split(",")
            query = reduce(operator.and_, (Q(title__icontains=item) for item in title_contains_all_filters))
            articles = articles.filter(query)
        if title_contains_one_filters:
            title_contains_one_filters = title_contains_one_filters.split(",")
            query = reduce(operator.or_, (Q(title__icontains=item) for item in title_contains_one_filters))
            articles = articles.filter(query)
        if summary_contains_all_filters:
            summary_contains_all_filters = summary_contains_all_filters.split(",")
            query = reduce(operator.and_, (Q(summary__icontains=item) for item in summary_contains_all_filters))
            articles = articles.filter(query)
        if summary_contains_one_filters:
            summary_contains_one_filters = summary_contains_one_filters.split(",")
            query = reduce(operator.or_, (Q(summary__icontains=item) for item in summary_contains_one_filters))
            articles = articles.filter(query)

        return articles.order_by("-published_at")

    serializer_class = ArticleSerializer
    authentication_classes = []
    filterset_class = DocsFilter
