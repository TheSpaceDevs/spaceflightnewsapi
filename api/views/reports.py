from rest_framework import viewsets

from api import models, serializers
from api.views.filters import ReportsFilters


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
    authentication_classes = []
    filterset_class = ReportsFilters
