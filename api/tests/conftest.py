from uuid import uuid4

import pytest

from api.models import Article, Launch, NewsSite, Provider


@pytest.fixture
def news_sites() -> list[NewsSite]:
    sites: list[NewsSite] = []
    for i in range(20):
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
    for i in range(8):
        article = Article.objects.create(
            title=f"Article {i}",
            summary=f"Description {i}",
            url=f"https://example.com/{i}",
            image_url=f"https://example.com/{i}.png",
            news_site=news_sites[i],
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

    return articles
