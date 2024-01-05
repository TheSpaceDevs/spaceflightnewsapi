from typing import Any

from django.db.models import Q, QuerySet
from django_filters import (
    BaseInFilter,
    BooleanFilter,
    CharFilter,
    FilterSet,
    IsoDateTimeFilter,
    NumberFilter,
    UUIDFilter,
)
from rest_framework import filters


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
            label=f"Search for documents with a {self.field_name} "
            f"containing all keywords from comma-separated values.",
        )

    def filter_keywords(self, queryset: QuerySet[Any], name: str, value: str) -> Any:
        words = value.split(",")
        q = Q()
        for word in words:
            q &= Q(**{f"{name}__icontains": word.strip()})
        return queryset.filter(q)


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
        label="Get all documents published after a given "
        "ISO8601 timestamp (included).",
    )
    published_at_lte = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="lte",
        label="Get all documents published before a given ISO8601 "
        "timestamp (included).",
    )
    published_at_gt = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="gt",
        label="Get all documents published after a given ISO8601 "
        "timestamp (excluded).",
    )
    published_at_lt = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="lt",
        label="Get all documents published before a given ISO8601 "
        "timestamp (excluded).",
    )
    updated_at_gte = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="gte",
        label="Get all documents updated after a given ISO8601 "
        "timestamp (included).",
    )
    updated_at_lte = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="lte",
        label="Get all documents updated before a given ISO8601 "
        "timestamp (included).",
    )
    updated_at_gt = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="gt",
        label="Get all documents updated after a given ISO8601 "
        "timestamp (excluded).",
    )
    updated_at_lt = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="lt",
        label="Get all documents updated before a given ISO8601 "
        "timestamp (excluded).",
    )


class DocsFilter(BaseFilter):
    launch = UUIDInFilter(
        field_name="launches__launch_id",
        lookup_expr="in",
        help_text="Search for all documents related to a specific "
        "launch using its Launch Library 2 ID.",
    )
    event = NumberInFilter(
        field_name="events__event_id",
        lookup_expr="in",
        help_text="Search for all documents related to a specific "
        "event using its Launch Library 2 ID.",
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
    search_description = (
        "Search for documents with a specific phrase in the title or summary."
    )
