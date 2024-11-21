# type: ignore

from django.db.models.manager import BaseManager
from graphene import List, ObjectType, Schema, String
from graphene_django import DjangoObjectType

from api.models import Article, Blog, Report


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ("id", "title", "url", "news_site", "published_at", "summary", "image_url")


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        fields = ("id", "title", "url", "news_site", "published_at", "summary", "image_url")


class ReportType(DjangoObjectType):
    class Meta:
        model = Report
        fields = ("id", "title", "url", "news_site", "published_at", "summary", "image_url")


class Query(ObjectType):
    articles = List(ArticleType, news_site=String(required=False))
    blogs = List(BlogType)
    reports = List(ReportType)

    def resolve_articles(self, info, news_site: str | None = None) -> BaseManager[Article]:
        q = None
        if news_site:
            q = Article.objects.filter(news_site=news_site)

        if q:
            return Article.objects.filter(q)

        return Article.objects.all()

    def resolve_blogs(self, info) -> BaseManager[Blog]:
        return Blog.objects.all()

    def resolve_reports(self, info) -> BaseManager[Report]:
        return Report.objects.all()


schema = Schema(query=Query)
