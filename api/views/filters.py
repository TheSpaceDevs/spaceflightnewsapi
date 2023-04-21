from django.db.models import Q
from django_filters import (
    CharFilter,
    FilterSet,
    IsoDateTimeFilter,
    BooleanFilter,
    UUIDFilter,
    BaseInFilter,
    NumberFilter,
)
from drf_spectacular.utils import extend_schema, OpenApiParameter


class UUIDInFilter(BaseInFilter, UUIDFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NumberInFilter(BaseInFilter, NumberFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InFilterMixin:
    def get_filter_list(self, value):
        return [v.strip() for v in value.split(",") if v.strip()]


class CharInFilter(InFilterMixin, BaseInFilter, CharFilter):
    field_name = None  # set this to the name of the field to be filtered

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="my_field_contains_all",
                type=str,
                location=OpenApiParameter.QUERY,
                description=f"Search for documents by the specified {field_name}s. Can be comma-separated values.",
            )
        ]
    )
    def filter(self, qs, value):
        if not value:
            return qs
        values = self.get_filter_list(value)
        q = Q(**{f"{self.field_name}__icontains": values[0]})
        for v in values[1:]:
            q |= Q(**{f"{self.field_name}__icontains": v})
        return qs.filter(q)


class NewsSiteInFilter(CharInFilter):
    field_name = "news_site"


class FieldContainsOneFilter(FilterSet):
    field_name = None  # set this to the name of the field to be filtered
    keywords = CharFilter(method="filter_keywords")

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="keywords",
                type=str,
                location=OpenApiParameter.QUERY,
                description=f"A comma-separated list of keywords of which at least one must be in the {field_name}.",
                required=False,
            ),
        ]
    )
    def filter_keywords(self, queryset, value):
        words = value.split(",")
        q = Q()
        for word in words:
            q |= Q(**{f"{self.field_name}__icontains": word.strip()})
        return queryset.filter(q)


class TitleContainsOneFilter(FieldContainsOneFilter):
    field_name = "title"


class SummaryContainsOneFilter(FieldContainsOneFilter):
    field_name = "summary"


class FieldContainsAllFilter(FilterSet):
    field_name = None  # set this to the name of the field to be filtered

    keywords = CharFilter(method="filter_keywords")

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="keywords",
                type=str,
                location=OpenApiParameter.QUERY,
                description=f"A comma-separated list of keywords which must all be in the {field_name}.",
                required=False,
            ),
        ]
    )
    def filter_keywords(self, queryset, value):
        words = value.split(",")
        q = Q()
        for word in words:
            q &= Q(**{f"{self.field_name}__icontains": word.strip()})
        return queryset.filter(q)


class TitleContainsAllFilter(FieldContainsAllFilter):
    field_name = "title"


class SummaryContainsAllFilter(FieldContainsAllFilter):
    field_name = "summary"


class DocsFilter(FilterSet):
    title_contains = CharFilter(
        field_name="title",
        lookup_expr="icontains",
        label="Search for all documents with a specific phrase in the title.",
    )
    title_contains_one = TitleContainsOneFilter()
    title_contains_all = TitleContainsAllFilter()
    summary_contains_one = SummaryContainsOneFilter()
    summary_contains_all = SummaryContainsAllFilter()
    news_site = NewsSiteInFilter()
    summary_contains = CharFilter(
        field_name="summary",
        lookup_expr="icontains",
        label="Search for all documents with a specific phrase in the summary.",
    )
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
    published_at__gte = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="gte",
        label="Get all documents published after a given ISO8601 timestamp (included).",
    )
    published_at__lte = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="lte",
        label="Get all documents published before a given ISO8601 timestamp (included).",
    )
    published_at__gt = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="gt",
        label="Get all documents published after a given ISO8601 timestamp (excluded).",
    )
    published_at__lt = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="lt",
        label="Get all documents published before a given ISO8601 timestamp (excluded).",
    )
    updated_at__gte = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="gte",
        label="Get all documents updated after a given ISO8601 timestamp (included).",
    )
    updated_at__lte = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="lte",
        label="Get all documents updated before a given ISO8601 timestamp (included).",
    )
    updated_at__gt = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="gt",
        label="Get all documents updated after a given ISO8601 timestamp (excluded).",
    )
    updated_at__lt = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="lt",
        label="Get all documents updated before a given ISO8601 timestamp (excluded).",
    )
    has_launch = BooleanFilter(
        field_name="launches",
        lookup_expr="isnull",
        exclude=True,
        label="Get all documents related to a launch using its Launch Library 2 ID.",
    )
    has_event = BooleanFilter(
        field_name="events",
        lookup_expr="isnull",
        exclude=True,
        label="Get all documents related to an event using its Launch Library 2 ID.",
    )


class ReportsFilters(FilterSet):
    date = CharFilter(
        field_name="published_at",
        lookup_expr="date",
        label="Search for all reports published on a specific date (YYYY-MM-DD).",
    )
    summary = CharFilter(
        field_name="summary",
        lookup_expr="icontains",
        label="Search for all reports with a specific phrase in the summary.",
    )
