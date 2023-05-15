from django_filters import rest_framework
from rest_framework import filters, viewsets

from api import models, serializers
from api.views.filters import BaseFilter, SearchFilter


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    authentication_classes = []
    filterset_class = BaseFilter
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["title", "summary"]
    ordering = ["-published_at"]
    ordering_fields = ["published_at", " updated_at"]
