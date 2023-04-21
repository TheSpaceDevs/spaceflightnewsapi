import operator
from functools import reduce

from django.db.models import Q
from rest_framework import viewsets

from api.models import Article
from api.serializers import ArticleSerializer
from api.views.filters import DocsFilter


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        articles = Article.objects.all()

        # title_contains_all_filters = self.request.query_params.get("title_contains_all", None)
        # title_contains_one_filters = self.request.query_params.get("title_contains_one", None)
        # summary_contains_all_filters = self.request.query_params.get("summary_contains_all", None)
        # summary_contains_one_filters = self.request.query_params.get("summary_contains_one", None)

        # if title_contains_all_filters:
        #     title_contains_all_filters = title_contains_all_filters.split(",")
        #     query = reduce(operator.and_, (Q(title__icontains=item) for item in title_contains_all_filters))
        #     articles = articles.filter(query)
        # if title_contains_one_filters:
        #     title_contains_one_filters = title_contains_one_filters.split(",")
        #     query = reduce(operator.or_, (Q(title__icontains=item) for item in title_contains_one_filters))
        #     articles = articles.filter(query)
        # if summary_contains_all_filters:
        #     summary_contains_all_filters = summary_contains_all_filters.split(",")
        #     query = reduce(operator.and_, (Q(summary__icontains=item) for item in summary_contains_all_filters))
        #     articles = articles.filter(query)
        # if summary_contains_one_filters:
        #     summary_contains_one_filters = summary_contains_one_filters.split(",")
        #     query = reduce(operator.or_, (Q(summary__icontains=item) for item in summary_contains_one_filters))
        #     articles = articles.filter(query)

        return articles.order_by("-published_at")

    serializer_class = ArticleSerializer
    authentication_classes = []
    filterset_class = DocsFilter
