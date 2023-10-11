from random import randrange
from uuid import uuid4

import pytest

from api.models import Article, Event, Launch, NewsSite, Provider

NUMBER_OF_NEWS_SITES = 20


@pytest.fixture
def news_sites() -> list[NewsSite]:
    sites: list[NewsSite] = []
    for i in range(NUMBER_OF_NEWS_SITES):
        site = NewsSite.objects.create(name=f"News Site {i}")
        sites.append(site)

    return sites


@pytest.fixture
def provider() -> Provider:
    return Provider.objects.create(name="Launch Library 2")


@pytest.fixture
def launches(provider: Provider) -> list[Launch]:
    launches: list[Launch] = []
    for i in range(10):
        launch = Launch.objects.create(
            launch_id=uuid4(),
            name=f"Launch {i}",
            provider=provider,
        )
        launches.append(launch)

    return launches


@pytest.fixture
def events(provider: Provider) -> list[Event]:
    events: list[Event] = []
    for i in range(10):
        event = Event.objects.create(
            event_id=i,
            name=f"Event {i}",
            provider=provider,
        )
        events.append(event)

    return events


@pytest.fixture
def articles(
    news_sites: list[NewsSite], launches: list[Launch], events: list[Event]
) -> list[Article]:
    articles: list[Article] = []
    for i in range(100):
        article = Article.objects.create(
            title=f"Article {i}",
            summary=f"Description {i}",
            url=f"https://example.com/{i}",
            image_url=f"https://example.com/{i}.png",
            news_site=news_sites[randrange(NUMBER_OF_NEWS_SITES)],
            published_at="2021-01-01T00:00:00Z",
            updated_at="2021-01-01T00:00:00Z",
        )
        articles.append(article)

    article_with_launch_1 = Article.objects.create(
        title="Article with Launch 1",
        summary="Description of an article with a launch 1",
        url="https://example.com/launch_1",
        image_url="https://example.com/launch_1.png",
        news_site=news_sites[0],
        published_at="2021-01-01T00:00:00Z",
        updated_at="2021-01-01T00:00:00Z",
    )
    article_with_launch_1.launches.add(launches[0])
    articles.append(article_with_launch_1)

    article_with_launch_2 = Article.objects.create(
        title="Article with Launch 2",
        summary="Description of an article with a launch 2",
        url="https://example.com/launch_2",
        image_url="https://example.com/launch_2.png",
        news_site=news_sites[1],
        published_at="2021-01-01T00:00:00Z",
        updated_at="2021-01-01T00:00:00Z",
    )
    article_with_launch_2.launches.add(launches[1])
    articles.append(article_with_launch_2)

    article_with_event_1 = Article.objects.create(
        title="Article with Event 1",
        summary="Description of an article with an event 1",
        url="https://example.com/event_1",
        image_url="https://example.com/event_1.png",
        news_site=news_sites[0],
        published_at="2021-01-01T00:00:00Z",
        updated_at="2021-01-01T00:00:00Z",
    )
    article_with_event_1.events.add(events[0])
    articles.append(article_with_event_1)

    article_with_event_2 = Article.objects.create(
        title="Article with Event 2",
        summary="Description of an article with an event 2",
        url="https://example.com/event_2",
        image_url="https://example.com/event_2.png",
        news_site=news_sites[1],
        published_at="2021-01-01T00:00:00Z",
        updated_at="2021-01-01T00:00:00Z",
    )
    article_with_event_2.events.add(events[1])
    articles.append(article_with_event_2)

    article_in_the_future_1 = Article.objects.create(
        title="Article in the future 1",
        summary="Description of an article in the future 1",
        url="https://example.com/future1",
        image_url="https://example.com/future1.png",
        news_site=news_sites[2],
        published_at="2042-01-01T00:00:00Z",
        updated_at="2042-01-01T00:00:00Z",
    )
    articles.append(article_in_the_future_1)

    article_in_the_future_2 = Article.objects.create(
        title="Article in the future 2",
        summary="Description of an article in the future 2",
        url="https://example.com/future2",
        image_url="https://example.com/future2.png",
        news_site=news_sites[3],
        published_at="2041-01-01T00:00:00Z",
        updated_at="2041-01-01T00:00:00Z",
    )
    articles.append(article_in_the_future_2)

    article_in_the_past_1 = Article.objects.create(
        title="Article in the past 1",
        summary="Description of an article in the past 1",
        url="https://example.com/past1",
        image_url="https://example.com/past1.png",
        news_site=news_sites[4],
        published_at="1999-01-01T00:00:00Z",
        updated_at="1999-01-01T00:00:00Z",
    )
    articles.append(article_in_the_past_1)

    article_in_the_past_2 = Article.objects.create(
        title="Article in the past 2",
        summary="Description of an article in the past 2",
        url="https://example.com/past2",
        image_url="https://example.com/past2.png",
        news_site=news_sites[5],
        published_at="2000-01-01T00:00:00Z",
        updated_at="2000-01-01T00:00:00Z",
    )
    articles.append(article_in_the_past_2)

    article_with_specific_title = Article.objects.create(
        title="Article with specific title",
        summary="Description of an article with a specific title",
        url="https://example.com/specific",
        image_url="https://example.com/specific.png",
        news_site=news_sites[6],
        published_at="2021-01-01T00:00:00Z",
        updated_at="2021-01-01T00:00:00Z",
    )
    articles.append(article_with_specific_title)

    article_with_spacex = Article.objects.create(
        title="Article with SpaceX",
        summary="Description of an article with SpaceX",
        url="https://example.com/spacex",
        image_url="https://example.com/spacex.png",
        news_site=news_sites[7],
        published_at="2021-01-01T00:00:00Z",
        updated_at="2021-01-01T00:00:00Z",
    )
    articles.append(article_with_spacex)

    return articles
