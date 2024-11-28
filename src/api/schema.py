# type: ignore

from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from api.models import Article, Blog, Event, Launch, NewsSite, Report
from api.views.filters import BaseFilter, DocsFilter


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        exclude = ["is_deleted"]
        filterset_class = DocsFilter
        interfaces = (relay.Node,)


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        exclude = ["is_deleted"]
        filterset_class = DocsFilter
        interfaces = (relay.Node,)


class ReportType(DjangoObjectType):
    class Meta:
        model = Report
        exclude = ["is_deleted"]
        filterset_class = BaseFilter
        interfaces = (relay.Node,)


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
