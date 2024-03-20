"""Custom admin views for the Spaceflight News API."""

from django import forms
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.utils.html import format_html
from django.utils.safestring import SafeString
from jet.filters import RelatedFieldAjaxListFilter

from api.models import Article, Blog, Event, Launch, NewsSite, Provider, Report
from api.models.abc import NewsItem


class ArticleForm(forms.ModelForm[NewsItem]):
    title = forms.CharField(widget=forms.TextInput(attrs={"size": 70}), required=True)


# Register your models here.
# Models that need customization
@admin.register(Article)
@admin.register(Blog)
class ArticleAdmin(admin.ModelAdmin[NewsItem]):
    """Admin view for articles and blogs."""

    list_per_page = 30
    form = ArticleForm
    list_display = (
        "title",
        "published_at_formatted",
        "news_site_formatted",
        "assigned_launches",
        "assigned_events",
        "featured_formatted",
        "is_deleted_formatted",
    )
    list_filter = (
        ("news_site", RelatedFieldAjaxListFilter),
        ("launches", RelatedFieldAjaxListFilter),
        ("events", RelatedFieldAjaxListFilter),
        "published_at",
        "featured",
        "is_deleted",
    )
    search_fields = ["title"]
    ordering = ("-published_at",)
    readonly_fields = [
        "image_tag",
    ]
    fields = [
        "title",
        "url",
        "news_site",
        "summary",
        "published_at",
        "featured",
        "launches",
        "events",
        "is_deleted",
        "image_tag",
    ]

    @staticmethod
    def published_at_formatted(obj: NewsItem) -> str:
        """Returns the publication datetime as a formatted string."""
        return obj.published_at.strftime("%B %d, %Y – %H:%M")

    published_at_formatted.short_description = "Published at"
    published_at_formatted.admin_order_field = "published_at"

    @staticmethod
    def news_site_formatted(obj: NewsItem) -> SafeString:
        """Returns the news site as a hyperlink to the article page."""
        return format_html('<a href="{}">{}</a>', obj.url, obj.news_site)

    news_site_formatted.short_description = "News site"
    news_site_formatted.admin_order_field = "news_site"

    @staticmethod
    def assigned_launches(obj: NewsItem) -> SafeString:
        """Returns the number of launches assigned to the article."""
        count = obj.launches.count()
        if count == 0:
            return format_html("")
        return format_html(
            '<div  title="{}" style="text-align:center;background:LawnGreen;color:black">{}</div >',
            "\n".join(obj.launches.values_list("name", flat=True)),
            obj.launches.count(),
        )

    assigned_launches.short_description = format_html(
        '<div  title="{}">{}</div >',
        "LL2 Launches",
        "L",
    )

    @staticmethod
    def assigned_events(obj: NewsItem) -> SafeString:
        """Returns the number of events assigned to the article."""
        count = obj.events.count()
        if count == 0:
            return format_html("")
        return format_html(
            '<div  title="{}" style="text-align:center;background:PaleTurquoise;color:black">{}</div >',
            "\n".join(obj.events.values_list("name", flat=True)),
            obj.events.count(),
        )

    assigned_events.short_description = format_html(
        '<div  title="{}">{}</div >',
        "LL2 Events",
        "E",
    )

    @staticmethod
    def featured_formatted(obj: NewsItem) -> bool:
        """Returns whether the article is featured."""
        return obj.featured

    featured_formatted.boolean = True
    featured_formatted.admin_order_field = "featured"
    featured_formatted.short_description = format_html(
        '<div  title="{}">{}</div >',
        "Featured",
        "F",
    )

    @staticmethod
    def is_deleted_formatted(obj: NewsItem) -> bool:
        """Returns whether the article is hidden from the API response."""
        return obj.is_deleted

    featured_formatted.boolean = True
    featured_formatted.admin_order_field = "is_deleted"
    featured_formatted.short_description = format_html(
        '<div  title="{}">{}</div >',
        "Deleted",
        "D",
    )

    @staticmethod
    def image_tag(obj: NewsItem) -> SafeString:
        """Returns the image of the article."""
        return format_html('<img src="{}" width=50%/>', obj.image_url)

    image_tag.short_description = "Image"

    def changelist_view(self: "ArticleAdmin", request: HttpRequest, extra_context=None) -> HttpResponse:
        extra_context = {"title": "News"}
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin[Report]):
    """Custom admin view for reports."""

    list_display = ("title", "news_site", "published_at", "is_deleted")
    search_fields = ["title"]
    ordering = ("-published_at",)


@admin.register(NewsSite)
class NewsSiteAdmin(admin.ModelAdmin[NewsSite]):
    list_display = ("name", "id")

    def changelist_view(self: "NewsSiteAdmin", request: HttpRequest, extra_context=None) -> HttpResponse:
        extra_context = {"title": "News Sites"}
        return super().changelist_view(request, extra_context=extra_context)


# Models that can be registered as is
@admin.register(Event)
class EventAdmin(admin.ModelAdmin[Event]):
    list_display = ("name",)
    search_fields = ["name", "event_id"]


@admin.register(Launch)
class LaunchAdmin(admin.ModelAdmin[Launch]):
    list_display = ("name",)
    search_fields = ["name", "launch_id"]


admin.site.register(Provider)

# Other customizations
admin.site.site_title = "SNAPI Admin"
admin.site.site_header = "SNAPI Admin"
admin.site.index_title = "Home"
