from django_filters import CharFilter, FilterSet, ModelChoiceFilter, IsoDateTimeFilter, BooleanFilter, Filter

from api import models


class ListFilterField(Filter):
    """ This is a custom FilterField to enable a behavior like:
    ?id=1,2,3,4 ...
    """

    def filter(self, queryset, value):
        # If no value is passed, just return the
        # initial queryset
        if not value:
            return queryset

        self.lookup_expr = 'in'  # Setting the lookupexpression for all values
        list_values = value.split(',')  # Split the incoming querystring by comma

        return super().filter(queryset, list_values)


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
    news_site = ListFilterField(
        field_name="news_site__name",
        label="Search for documents by the specified news sites. Can be multiple comma-separated sites. Case sensitive.",
    )
    launch = ListFilterField(
        field_name="launches__launch_id",
        label="This label is overriden in the viewset.",
    )
    event = ListFilterField(
        field_name="events__event_id",
        label="This label is overriden in the viewset.",
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
