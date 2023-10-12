"""Custom admin views for the Spaceflight News API."""
from django.contrib import admin
from django.db.models import Count, QuerySet
from django.http import HttpRequest

from api.models import Article, Blog, Event, Launch, NewsSite, Provider, Report
from api.models.abc import NewsItem


# Register your models here.
# Models that need customization
@admin.register(Article)
@admin.register(Blog)
class ArticleAdmin(admin.ModelAdmin[NewsItem]):
    """Admin view for articles and blogs."""

    list_display = (
        "title",
        "news_site",
        "published_at",
        "featured",
        "assigned_launches",
        "assigned_events",
    )
    list_filter = ("published_at", "featured", "news_site")
    filter_horizontal = ["launches", "events"]
    search_fields = ["title"]
    ordering = ("-published_at",)

    @staticmethod
    def assigned_launches(obj: NewsItem) -> int:
        """Returns the number of launches assigned to the article."""
        return obj.launches.count()

    @staticmethod
    def assigned_events(obj: NewsItem) -> int:
        """Returns the number of events assigned to the article."""
        return obj.events.count()

    def get_queryset(self, request: HttpRequest) -> QuerySet[NewsItem]:
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            launch_count=Count("launches"), event_count=Count("events")
        )
        return queryset


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin[Report]):
    """Custom admin view for reports."""

    list_display = ("title", "news_site", "published_at")
    search_fields = ["title"]
    ordering = ("-published_at",)


# Models that can be registered as is
admin.site.register(Event)
admin.site.register(Launch)
admin.site.register(NewsSite)
admin.site.register(Provider)

# Other customizations
admin.site.site_title = "Spaceflight News API Admin"
admin.site.site_header = "Spaceflight News API Admin"
admin.site.index_title = "Spaceflight News API Admin"
