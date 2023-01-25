from django_filters import rest_framework as filters
from rest_framework import viewsets

from api import models, serializers


class DocsFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
        label="Search for all documents with a specific phrase in the title.",
    )
    summary = filters.CharFilter(
        field_name="summary",
        lookup_expr="icontains",
        label="Search for all documents with a specific phrase in the summary.",
    )
    date = filters.CharFilter(
        field_name="published_at",
        lookup_expr="date",
        label="Search for all documents published on a specific date (YYYY-MM-DD).",
    )
    news_site = filters.ModelChoiceFilter(
        queryset=models.NewsSite.objects.all(),
        to_field_name="name",
        label="Search for documents by a specific news site. Case sensitive.",
    )
    launch = filters.ModelChoiceFilter(
        queryset=models.Launch.objects.all(),
        to_field_name="launch_id",
        field_name="launches",
        label="Get all documents related to a specific launch.",
    )
    event = filters.ModelChoiceFilter(
        queryset=models.Event.objects.all(),
        to_field_name="event_id",
        field_name="events",
        label="Get all documents related to a specific event.",
    )


# Create your views here.
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    filterset_class = DocsFilter


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    filterset_class = DocsFilter


class ReportsFilters(filters.FilterSet):
    date = filters.CharFilter(
        field_name="published_at",
        lookup_expr="date",
        label="Search for all reports published on a specific date (YYYY-MM-DD).",
    )
    summary = filters.CharFilter(
        field_name="summary",
        lookup_expr="icontains",
        label="Search for all reports with a specific phrase in the summary.",
    )


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    filterset_class = ReportsFilters
