from rest_framework import serializers
from typing import TypedDict

from api.models import Blog, Event, Launch, NewsSite


class ValidatedBlogDataDict(TypedDict):
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    launches: list[dict[str, str]]
    events: list[dict[str, str | int]]


class BlogV3Serializer(serializers.Serializer[Blog]):
    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField()
    imageUrl = serializers.CharField()
    newsSite = serializers.CharField()
    summary = serializers.CharField(allow_blank=True)
    publishedAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()
    launches = serializers.ListField()
    events = serializers.ListField()

    def create(self, validated_data: ValidatedBlogDataDict) -> Blog:
        news_site = NewsSite.objects.get(name=validated_data["newsSite"])
        launches_list: list[Launch] = []
        events_list: list[Event] = []

        for launch in validated_data["launches"]:
            launches_list.append(Launch.objects.get(launch_id=launch["id"]))

        for event in validated_data["events"]:
            events_list.append(Event.objects.get(event_id=event["id"]))

        blog, _ = Blog.objects.update_or_create(
            id=validated_data["id"],
            defaults={
                "title": validated_data["title"],
                "url": validated_data["url"],
                "image_url": validated_data["imageUrl"],
                "news_site": news_site,
                "summary": validated_data["summary"],
                "published_at": validated_data["publishedAt"],
                "updated_at": validated_data["updatedAt"],
            },
        )

        blog.launches.set(launches_list)
        blog.events.set(events_list)

        return blog
