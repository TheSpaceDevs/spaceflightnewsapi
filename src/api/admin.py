"""Custom admin views for the Spaceflight News API."""

from django import forms
from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import resolve_url
from django.utils.html import format_html
from django.utils.safestring import SafeString

# ignore the type error as it seems there's no package for it
from jet.filters import RelatedFieldAjaxListFilter  # type: ignore

from api.models import Article, Author, Blog, Event, Launch, NewsSite, Provider, Report, Socials
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
        "thumbnail",
        "published_at_formatted",
        "news_site_formatted",
        "authors_formatted",
        "assigned_launches",
        "assigned_events",
        "featured_formatted",
        "is_deleted_formatted",
    )
    list_filter = (
        ("news_site", RelatedFieldAjaxListFilter),
        ("launches", RelatedFieldAjaxListFilter),
        ("events", RelatedFieldAjaxListFilter),
        ("authors", RelatedFieldAjaxListFilter),
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
        "authors",
        "url",
        "image_url",
        "news_site",
        "summary",
        "published_at",
        "featured",
        "launches",
        "events",
        "is_deleted",
        "image_tag",
    ]

    def get_queryset(self, request: HttpRequest) -> QuerySet[NewsItem]:
        """Return the queryset with related fields prefetched."""
        qs = super().get_queryset(request).select_related("news_site").prefetch_related("launches", "events")
        return qs

    @staticmethod
    def thumbnail(obj: NewsItem) -> SafeString:
        """Returns the publication image as an interactive thumbnail."""
        return format_html('<img loading="lazy" src="{}" width=50px class="hover-image-list"/>', obj.image_url)

    @staticmethod
    @admin.display(
        ordering="-published_at",
        description="Published at",
    )
    def published_at_formatted(obj: NewsItem) -> str:
        """Returns the publication datetime as a formatted string."""
        return obj.published_at.strftime("%B %d, %Y – %H:%M")

    @staticmethod
    @admin.display(
        ordering="news_site",
        description="News site",
    )
    def news_site_formatted(obj: NewsItem) -> SafeString:
        """Returns the news site as a hyperlink to the article page."""
        return format_html('<a href="{}">{}</a>', obj.url, obj.news_site)

    @staticmethod
    @admin.display(
        description="Authors",
    )
    def authors_formatted(obj: NewsItem) -> SafeString:
        """Returns the authors as a list of hyperlinks."""
        authors_list = [
            f'<a href="{resolve_url(admin_urlname(Author._meta, format_html("change")), author.id)}">{author.name}</a>'
            for author in obj.authors.all()
        ]
        string = [authors_list[i : i + 3] for i in range(0, len(authors_list), 3)]  # Group into lines of up to 3 authors
        split_string = "<br>".join([", ".join(line) for line in string])  # Format each line and join with <br>
        return format_html(split_string)

    @staticmethod
    @admin.display(
        description=format_html(
            '<div  title="{}">{}</div >',
            "LL2 Launches",
            "L",
        ),
    )
    def assigned_launches(obj: NewsItem) -> SafeString:
        """Returns the number of launches assigned to the article."""
        count = obj.launches.count()
        if count == 0:
            return format_html("")
        return format_html(
            '<div  title="{}" style="text-align:center;background:LawnGreen;color:black">{}</div >',
            "\n".join([launch.name for launch in obj.launches.all()]),
            obj.launches.count(),
        )

    @staticmethod
    @admin.display(
        description=format_html(
            '<div  title="{}">{}</div >',
            "LL2 Events",
            "E",
        )
    )
    def assigned_events(obj: NewsItem) -> SafeString:
        """Returns the number of events assigned to the article."""
        count = obj.events.count()
        if count == 0:
            return format_html("")
        return format_html(
            '<div  title="{}" style="text-align:center;background:PaleTurquoise;color:black">{}</div >',
            "\n".join([event.name for event in obj.events.all()]),
            obj.events.count(),
        )

    @staticmethod
    @admin.display(
        boolean=True,
        ordering="featured",
        description=format_html(
            '<div  title="{}">{}</div >',
            "Featured",
            "F",
        ),
    )
    def featured_formatted(obj: NewsItem) -> bool:
        """Returns whether the article is featured."""
        return obj.featured

    @staticmethod
    @admin.display(
        boolean=True,
        ordering="is_deleted",
        description=format_html(
            '<div  title="{}">{}</div >',
            "Deleted",
            "D",
        ),
    )
    def is_deleted_formatted(obj: NewsItem) -> bool:
        """Returns whether the article is hidden from the API response."""
        return obj.is_deleted

    @staticmethod
    @admin.display(description="Image")
    def image_tag(obj: NewsItem) -> SafeString:
        """Returns the image of the article."""
        return format_html('<img loading="lazy" src="{}" width=50% class="hover-image-detail"/>', obj.image_url)

    def changelist_view(self, request: HttpRequest, extra_context: dict[str, str] | None = None) -> HttpResponse:
        """Customize the title of the article admin view."""
        extra_context = {"title": "News"}
        return super().changelist_view(request, extra_context)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin[Report]):
    """Custom admin view for reports."""

    list_display = ("title", "news_site", "published_at", "is_deleted")
    search_fields = ["title"]
    ordering = ("-published_at",)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Report]:
        """Return the queryset with related fields prefetched."""
        return super().get_queryset(request).select_related("news_site")


@admin.register(NewsSite)
class NewsSiteAdmin(admin.ModelAdmin[NewsSite]):
    list_display = ("name", "id")

    def changelist_view(self, request: HttpRequest, extra_context: dict[str, str] | None = None) -> HttpResponse:
        """Customize the title of the news site admin view."""
        extra_context = {"title": "News Sites"}
        return super().changelist_view(request, extra_context)


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
admin.site.register(Author)
admin.site.register(Socials)

# Other customizations
admin.site.site_title = "SNAPI Admin"
admin.site.site_header = "SNAPI Admin"
admin.site.index_title = "Home"
