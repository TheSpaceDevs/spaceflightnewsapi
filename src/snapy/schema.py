# type: ignore

from django.db.models.manager import BaseManager
from graphene import UUID, Int, List, ObjectType, Schema, String
from graphene_django import DjangoObjectType

from api.models import Article, Blog, Event, Launch, Report


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ("id", "title", "url", "news_site", "published_at", "summary", "image_url", "launches", "events")


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        fields = ("id", "title", "url", "news_site", "published_at", "summary", "image_url", "launches", "events")


class ReportType(DjangoObjectType):
    class Meta:
        model = Report
        fields = ("id", "title", "url", "news_site", "published_at", "summary", "image_url")


class LaunchType(DjangoObjectType):
    class Meta:
        model = Launch
        fields = ("id", "launch_id", "nane", "provider")


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = ("id", "event_id", "name", "provider")


class Query(ObjectType):
    all_articles = List(ArticleType)
    all_blogs = List(BlogType)
    all_reports = List(ReportType)

    articles_by_news_site = List(ArticleType, news_site=String(required=True))
    blogs_by_news_site = List(BlogType, news_site=String(required=True))
    reports_by_news_site = List(ReportType, news_site=String(required=True))

    articles_by_launch = List(ArticleType, launch_id=UUID(required=True))
    blogs_by_launch = List(BlogType, launch_id=UUID(required=True))

    articles_by_event = List(ArticleType, event_id=Int(required=True))
    blogs_by_event = List(ArticleType, event_id=Int(required=True))

    def resolve_all_articles(self, info) -> BaseManager[Article]:
        return Article.objects.all()

    def resolve_all_blogs(self, info) -> BaseManager[Blog]:
        return Blog.objects.all()

    def resolve_all_reports(self, info) -> BaseManager[Report]:
        return Report.objects.all()

    def resolve_articles_by_news_site(self, info, news_site: str) -> BaseManager[Article]:
        return Article.objects.filter(news_site__name=news_site)

    def resolve_blogs_by_news_site(self, info, news_site: str) -> BaseManager[Article]:
        return Article.objects.filter(news_site__name=news_site)

    def resolve_reports_by_news_site(self, info, news_site: str) -> BaseManager[Article]:
        return Article.objects.filter(news_site__name=news_site)

    def resolve_articles_by_launch(self, info, launch_id: UUID) -> BaseManager[Article]:
        return Article.objects.filter(launches__launch_id=launch_id)

    def resolve_blogs_by_launch(self, info, launch_id: UUID) -> BaseManager[Blog]:
        return Blog.objects.filter(launches__launch_id=launch_id)

    def resolve_articles_by_event(self, info, event_id: int) -> BaseManager[Article]:
        return Article.objects.filter(events__event_id=event_id)

    def resolve_blogs_by_event(self, info, event_id: int) -> BaseManager[Blog]:
        return Blog.objects.filter(events__event_id=event_id)


schema = Schema(query=Query)
