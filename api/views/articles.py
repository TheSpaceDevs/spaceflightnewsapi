from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import viewsets

from api.models import Article
from api.serializers import ArticleSerializer
from api.views.filters import DocsFilter
import operator
from django.db.models import Q
from functools import reduce

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

    def get_queryset(self):
        articles = Article.objects.all()

        news_sites_filters = self.request.query_params.get("news_sites", None)
        launches_filters = self.request.query_params.get("launches", None)
        events_filters = self.request.query_params.get("events", None)
        title_contains_all_filters = self.request.query_params.get("title_contains_all", None)
        title_contains_one_filters = self.request.query_params.get("title_contains_one", None)
        summary_contains_all_filters = self.request.query_params.get("summary_contains_all", None)
        summary_contains_one_filters = self.request.query_params.get("summary_contains_one", None)
        has_event_filter = self.request.query_params.get("has_event", None)
        has_launch_filter = self.request.query_params.get("has_launch", None)

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
        if has_event_filter:
            if has_event_filter == "true":
                articles = articles.filter(events__isnull=False)
            elif has_event_filter == "false":
                articles = articles.filter(events__isnull=True)
        if has_launch_filter:
            if has_launch_filter == "true":
                articles = articles.filter(launches__isnull=False)
            elif has_launch_filter == "false":
                articles = articles.filter(launches__isnull=True)

        return articles.order_by("-published_at")

    serializer_class = ArticleSerializer
    authentication_classes = []
    filterset_class = DocsFilter
    search_fields = (
        "title",
        "summary",
        "news_site__name",
        "launches__launch_id",
        "events__event_id",
        "launches__name",
        "events__name")
    ordering_fields = (
        "title",
        "summary",
        "news_site__name",
        "published_at",
        "updated_at")
