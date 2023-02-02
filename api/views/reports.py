from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from api import models, serializers
from api.filters import ReportsFilters


@extend_schema(tags=["reports"])
class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    filterset_class = ReportsFilters
