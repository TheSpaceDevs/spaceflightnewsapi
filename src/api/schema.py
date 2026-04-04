# type: ignore

from django.db.models import Prefetch
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from api.models import Article, Blog, Event, Launch, NewsSite, Report
from api.models.author import Author
from api.views.filters import BaseFilter, DocsFilter


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        exclude = ["is_deleted"]
        filterset_class = DocsFilter
        interfaces = (relay.Node,)

    @classmethod
    def get_queryset(cls, queryset, info):
        return (
            queryset.order_by("-published_at")
            .select_related("news_site")
            .prefetch_related(
                "launches",
                "events",
                Prefetch("authors", queryset=Author.objects.select_related("socials")),
            )
        )


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        exclude = ["is_deleted"]
        filterset_class = DocsFilter
        interfaces = (relay.Node,)

    @classmethod
    def get_queryset(cls, queryset, info):
        return (
            queryset.order_by("-published_at")
            .select_related("news_site")
            .prefetch_related(
                "launches",
                "events",
                Prefetch("authors", queryset=Author.objects.select_related("socials")),
            )
        )


class ReportType(DjangoObjectType):
    class Meta:
        model = Report
        exclude = ["is_deleted"]
        filterset_class = BaseFilter
        interfaces = (relay.Node,)

    @classmethod
    def get_queryset(cls, queryset, info):
        return (
            queryset.order_by("-published_at")
            .select_related("news_site")
            .prefetch_related(
                Prefetch("authors", queryset=Author.objects.select_related("socials")),
            )
        )


class LaunchType(DjangoObjectType):
    class Meta:
        model = Launch
        interfaces = (relay.Node,)


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        interfaces = (relay.Node,)


class NewsSiteType(DjangoObjectType):
    class Meta:
        model = NewsSite
        interfaces = (relay.Node,)


class Query(ObjectType):
    article = relay.Node.Field(ArticleType)
    all_articles = DjangoFilterConnectionField(ArticleType)

    blog = relay.Node.Field(BlogType)
    all_blogs = DjangoFilterConnectionField(BlogType)

    report = relay.Node.Field(ReportType)
    all_reports = DjangoFilterConnectionField(ReportType)
