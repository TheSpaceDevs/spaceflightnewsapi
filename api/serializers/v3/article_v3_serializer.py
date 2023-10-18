import datetime

from rest_framework import serializers
from typing import TypedDict

from api.models import Article, Event, Launch, NewsSite


class ValidatedArticleDataDict(TypedDict):
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: datetime.date
    updatedAt: datetime.date
    featured: bool
    launches: list[dict[str, str]]
    events: list[dict[str, str | str, int]]


class ArticleV3Serializer(serializers.Serializer[Article]):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    imageUrl = serializers.URLField()
    newsSite = serializers.CharField()
    summary = serializers.CharField(allow_blank=True)
    publishedAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()
    featured = serializers.BooleanField()
    launches = serializers.ListField()
    events = serializers.ListField()

    def create(self, validated_data: ValidatedArticleDataDict) -> Article:
        news_site = NewsSite.objects.get(name=validated_data["newsSite"])
        launches_list: list[Launch] = []
        events_list: list[Event] = []

        for launch in validated_data["launches"]:
            launches_list.append(Launch.objects.get(launch_id=launch["id"]))

        for event in validated_data["events"]:
            events_list.append(Event.objects.get(event_id=event["id"]))

        article, _ = Article.objects.update_or_create(
            id=validated_data["id"],
            defaults={
                "title": validated_data["title"],
                "url": validated_data["url"],
                "image_url": validated_data["imageUrl"],
                "news_site": news_site,
                "summary": validated_data["summary"],
                "published_at": validated_data["publishedAt"],
                "updated_at": validated_data["updatedAt"],
                "featured": validated_data["featured"],
            },
        )

        article.launches.set(launches_list)
        article.events.set(events_list)

        return article
