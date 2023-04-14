from django_filters import CharFilter, FilterSet, ModelChoiceFilter, IsoDateTimeFilter, BooleanFilter

from api import models


class DocsFilter(FilterSet):
    title_contains = CharFilter(
        field_name="title",
        lookup_expr="icontains",
        label="Search for all documents with a specific phrase in the title.",
    )
    summary_contains = CharFilter(
        field_name="summary",
        lookup_expr="icontains",
        label="Search for all documents with a specific phrase in the summary.",
    )
    news_site = ModelChoiceFilter(
        queryset=models.NewsSite.objects.all(),
        to_field_name="name",
        label="Search for documents by a specific news site. Case sensitive.",
    )
    launch = ModelChoiceFilter(
        queryset=models.Launch.objects.all(),
        to_field_name="launch_id",
        field_name="launches",
        label="Get all documents related to a specific launch.",
    )
    event = ModelChoiceFilter(
        queryset=models.Event.objects.all(),
        to_field_name="event_id",
        field_name="events",
        label="Get all documents related to a specific event.",
    )
    published_at__gte = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="gte",
        label="Get all documents published after a given ISO8601 timestamp (included)."
    )
    published_at__lte = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="lte",
        label="Get all documents published before a given ISO8601 timestamp (included)."
    )
    published_at__gt = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="gt",
        label="Get all documents published after a given ISO8601 timestamp (excluded)."
    )
    published_at__lt = IsoDateTimeFilter(
        field_name="published_at",
        lookup_expr="lt",
        label="Get all documents published before a given ISO8601 timestamp (excluded)."
    )
    updated_at__gte = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="gte",
        label="Get all documents updated after a given ISO8601 timestamp (included)."
    )
    updated_at__lte = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="lte",
        label="Get all documents updated before a given ISO8601 timestamp (included)."
    )
    updated_at__gt = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="gt",
        label="Get all documents updated after a given ISO8601 timestamp (excluded)."
    )
    updated_at__lt = IsoDateTimeFilter(
        field_name="updated_at",
        lookup_expr="lt",
        label="Get all documents updated before a given ISO8601 timestamp (excluded)."
    )
    has_launch = BooleanFilter(
        field_name="launches",
        lookup_expr="isnull",
        exclude=True,
        label="Get all documents related to a launch."
    )
    has_event = BooleanFilter(
        field_name="events",
        lookup_expr="isnull",
        exclude=True,
        label="Get all documents related to an event."
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
