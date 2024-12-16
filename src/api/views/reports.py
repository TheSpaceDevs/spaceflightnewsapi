from django_filters import rest_framework
from rest_framework import viewsets

from api.models.report import Report
from api.serializers.report_serializer import ReportSerializer
from api.views.filters import BaseFilter, SearchFilter


class ReportViewSet(viewsets.ReadOnlyModelViewSet):  # type: ignore
    queryset = (
        Report.objects.exclude(is_deleted=True)
        .select_related("news_site")
        .prefetch_related("authors")
        .order_by("-published_at")
    )
    serializer_class = ReportSerializer
    authentication_classes = []
    filterset_class = BaseFilter
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["title", "summary", "news_site__name"]
