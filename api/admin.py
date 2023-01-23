from django.contrib import admin

from api.models import Article, Blog, Event, Launch, NewsSite, Provider, Report


# Register your models here.
@admin.register(Article)
@admin.register(Blog)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "news_site", "published_at", "featured")
    filter_horizontal = ["launches", "events"]
    search_fields = ["title"]


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "news_site", "published_at")
    search_fields = ["title"]


admin.site.register(Event)
admin.site.register(Launch)
admin.site.register(NewsSite)
admin.site.register(Provider)

# Other customizations
admin.site.site_title = "Spaceflight News API Admin"
admin.site.site_header = "Spaceflight News API Admin"
admin.site.index_title = "Spaceflight News API Admin"
