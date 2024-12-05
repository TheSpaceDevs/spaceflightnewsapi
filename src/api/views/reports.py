from django_filters import rest_framework
from rest_framework import viewsets

from api import serializers
from api.models.report import Report
from api.views.filters import BaseFilter, SearchFilter


class ReportViewSet(viewsets.ReadOnlyModelViewSet):  # type: ignore
    queryset = Report.objects.exclude(is_deleted=True).select_related("news_site").order_by("-published_at")
    serializer_class = serializers.ReportSerializer
    authentication_classes = []
    filterset_class = BaseFilter
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["title", "summary", "news_site__name"]
