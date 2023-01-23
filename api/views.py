from rest_framework import viewsets

from api import serializers, models


# Create your views here.
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer
