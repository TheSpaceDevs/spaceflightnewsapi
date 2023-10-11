from random import randrange
from uuid import uuid4

import pytest

from api.models import Article, Launch, NewsSite, Provider

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
def articles(news_sites: list[NewsSite], launches: list[Launch]) -> list[Article]:
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

    return articles
