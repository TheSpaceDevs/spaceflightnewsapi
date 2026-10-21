import operator
from functools import reduce
from typing import Any

from django.db.models import Exists, OuterRef, Q, QuerySet
from django.db.models.constants import LOOKUP_SEP
from django_filters import (
    BaseInFilter,
    BooleanFilter,
    CharFilter,
    FilterSet,
    IsoDateTimeFilter,
    NumberFilter,
    OrderingFilter,
    UUIDFilter,
)
from rest_framework import filters
from rest_framework.request import Request
from rest_framework.views import APIView


class UUIDInFilter(BaseInFilter, UUIDFilter):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class NumberInFilter(BaseInFilter, NumberFilter):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)


class CharInFilter(CharFilter):
    def __init__(self, **kwargs: Any):
        self.field_name = kwargs.pop("field_name")
        super().__init__(
            field_name=self.field_name,
            method=self.filter_keywords,
            label=f"Search for documents with a {self.field_name} "
            f"present in a list of comma-separated values. Case "
            f"insensitive.",
        )

    def filter_keywords(self, queryset: QuerySet[Any], name: str, value: str) -> Any:
        words = value.split(",")
        q = Q()
        for word in words:
            q |= Q(**{f"{name}__iexact": word.strip()})
        return queryset.filter(q)


class CharNotInFilter(CharFilter):
    def __init__(self, **kwargs: Any):
        self.field_name = kwargs.pop("field_name")
        super().__init__(
            field_name=self.field_name,
            method=self.filter_keywords,
            label=f"Search for documents with a {self.field_name} "
            f"not present in a list of comma-separated values. "
            f"Case insensitive.",
        )

    def filter_keywords(self, queryset: QuerySet[Any], name: str, value: str) -> Any:
        words = value.split(",")
        q = Q()
        for word in words:
            q |= Q(**{f"{name}__iexact": word.strip()})
        return queryset.exclude(q)


class ContainsOneFilter(CharFilter):
    def __init__(self, **kwargs: Any):
        self.field_name = kwargs.pop("field_name")
        super().__init__(
            field_name=self.field_name,
            method=self.filter_keywords,
            label=f"Search for documents with a {self.field_name} "
            f"containing at least one keyword from "
            f"comma-separated values.",
        )

    def filter_keywords(self, queryset: QuerySet[Any], name: str, value: str) -> Any:
        words = value.split(",")
        q = Q()
        for word in words:
            q |= Q(**{f"{name}__icontains": word.strip()})
        return queryset.filter(q)


class ContainsAllFilter(CharFilter):
    def __init__(self, **kwargs: Any):
        self.field_name = kwargs.pop("field_name")
        super().__init__(
            field_name=self.field_name,
            method=self.filter_keywords,
            label=f"Search for documents with a {self.field_name} containing all keywords from comma-separated values.",
        )

    def filter_keywords(self, queryset: QuerySet[Any], name: str, value: str) -> Any:
        words = value.split(",")
        q = Q()
        for word in words:
            q &= Q(**{f"{name}__icontains": word.strip()})
        return queryset.filter(q)


class OrderingFilterWithLabel(OrderingFilter):
    def __init__(self, **kwargs: Any) -> None:
        self.fields = kwargs.get("fields")

        if not self.fields:
            raise AssertionError("The 'fields' argument is required.")

        # Itterate over the tupple, generating a string of all first elements, including negative ones.
        fields = ", ".join([f"{field[0]}, -{field[0]}" for field in self.fields])

        super().__init__(
            label=f"Order the result on `{fields}`.",
            **kwargs,
        )


class BaseFilter(FilterSet):
    title_contains = CharFilter(
        field_name="title",
        lookup_expr="icontains",
        label="Search for all documents with a specific phrase in the title.",
    )
    title_contains_one = ContainsOneFilter(field_name="title")
    title_contains_all = ContainsAllFilter(field_name="title")
    summary_contains_one = ContainsOneFilter(field_name="summary")
    summary_contains_all = ContainsAllFilter(field_name="summary")
    news_site = CharInFilter(field_name="news_site__name")
    news_site_exclude = CharNotInFilter(field_name="news_site__name")
    summary_contains = CharFilter(
        field_name="summary",
        lookup_expr="icontains",
        label="Search for all documents with a specific phrase in the summary.",
    )
    published_at_gte = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="gte",
        label="Get all documents published after a given ISO8601 timestamp (included).",
    )
    published_at_lte = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="lte",
        label="Get all documents published before a given ISO8601 timestamp (included).",
    )
    published_at_gt = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="gt",
        label="Get all documents published after a given ISO8601 timestamp (excluded).",
    )
    published_at_lt = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="lt",
        label="Get all documents published before a given ISO8601 timestamp (excluded).",
    )
    updated_at_gte = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="gte",
        label="Get all documents updated after a given ISO8601 timestamp (included).",
    )
    updated_at_lte = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="lte",
        label="Get all documents updated before a given ISO8601 timestamp (included).",
    )
    updated_at_gt = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="gt",
        label="Get all documents updated after a given ISO8601 timestamp (excluded).",
    )
    updated_at_lt = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="lt",
        label="Get all documents updated before a given ISO8601 timestamp (excluded).",
    )

    ordering = OrderingFilterWithLabel(
        fields=(
            (
                "published_at",
                "published_at",
            ),
            ("updated_at", "updated_at"),
        ),
    )


class DocsFilter(BaseFilter):
    launch = UUIDInFilter(
        field_name="launches__launch_id",
        lookup_expr="in",
        help_text="Search for all documents related to a specific launch using its Launch Library 2 ID.",
    )
    event = NumberInFilter(
        field_name="events__event_id",
        lookup_expr="in",
        help_text="Search for all documents related to a specific event using its Launch Library 2 ID.",
    )
    has_launch = BooleanFilter(
        field_name="launches",
        lookup_expr="isnull",
        exclude=True,
        label="Get all documents that have a related launch.",
    )
    has_event = BooleanFilter(
        field_name="events",
        lookup_expr="isnull",
        exclude=True,
        label="Get all documents that have a related event.",
    )
    is_featured = BooleanFilter(
        field_name="featured",
        lookup_expr="exact",
        label="Get all documents that are featured.",
    )


class SearchFilter(filters.SearchFilter):
    """DRF's search filter, but fields behind a foreign key are matched up front.

    DRF ORs all search fields together. When one of them lives on a joined table (`news_site__name`), Postgres can't
    combine the trigram indexes on title and summary and scans the whole table instead. Looking up the matching
    related ids first turns that field into `news_site_id IN (...)`, which can be combined with the other indexes.
    """

    search_description = "Search for documents with a specific phrase in the title or summary."

    def filter_queryset(self, request: Request, queryset: QuerySet[Any], view: APIView) -> QuerySet[Any]:
        search_fields = self.get_search_fields(view, request)
        search_terms = self.get_search_terms(request)

        if not search_fields or not search_terms:
            return queryset

        conditions = (
            reduce(operator.or_, (self._search_condition(queryset, str(field), term) for field in search_fields))
            for term in search_terms
        )
        filtered = queryset.filter(reduce(operator.and_, conditions))

        # Remove duplicates caused by many-to-many search fields, same as DRF does.
        if self.must_call_distinct(filtered, search_fields):
            return queryset.filter(Exists(filtered.filter(pk=OuterRef("pk"))))
        return filtered

    def _search_condition(self, queryset: QuerySet[Any], search_field: str, term: str) -> Q:
        relation, _, related_field = search_field.partition(LOOKUP_SEP)
        if related_field and search_field[0] not in self.lookup_prefixes:
            field = queryset.model._meta.get_field(relation)
            if field.many_to_one and field.related_model:
                related = field.related_model._default_manager.all()
                lookup = self.construct_search(related_field, related)
                ids = list(related.filter(**{lookup: term}).values_list("pk", flat=True))
                return Q(**{f"{relation}__in": ids})

        return Q(**{self.construct_search(search_field, queryset): term})
