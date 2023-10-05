"""
This module tests both articles and the blogs endpoints.
Most code is shared between the two.
"""

import pytest

from api.models import Article, Launch, NewsSite


@pytest.mark.django_db
class TestArticlesEndpoint:
    def test_get_articles(self, client, articles: list[Article]):
        response = client.get("/v4/articles/")
        assert response.status_code == 200

        data = response.json()

        assert all(
            article.title in [article["title"] for article in data["results"]]
            for article in articles
        )
        assert all(
            article.news_site.name
            in [json_article["news_site"] for json_article in data["results"]]
            for article in articles
        )
        assert len(data["results"]) == 10

    def test_get_single_article(self, client, articles: list[Article]):
        response = client.get(f"/v4/articles/{articles[0].id}/")
        assert response.status_code == 200

        data = response.json()

        assert data["title"] == articles[0].title
        assert data["news_site"] == articles[0].news_site.name

    def test_limit_articles(self, client, articles: list[Article]):
        response = client.get("/v4/articles/?limit=5")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 5

    def test_get_all_articles_with_launches(self, client, articles: list[Article]):
        response = client.get("/v4/articles/?has_launch=true")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 2

    def test_get_articles_with_launch(
        self, client, articles: list[Article], launches: list[Launch]
    ):
        response = client.get(f"/v4/articles/?launch={launches[0].launch_id}")
        assert response.status_code == 200

        data = response.json()
        assert data["results"][0]["title"] == articles[8].title
        assert data["results"][0]["launches"][0]["launch_id"] == str(
            launches[0].launch_id
        )
        assert (
            data["results"][0]["launches"][0]["provider"] == launches[0].provider.name
        )
        assert len(data["results"]) == 1

    def test_get_articles_by_news_site(
        self, client, articles: list[Article], news_sites: list[NewsSite]
    ):
        response = client.get(f"/v4/articles/?news_site={news_sites[0].name}")
        assert response.status_code == 200

        data = response.json()
        assert data["results"][0]["title"] == articles[0].title
        assert data["results"][0]["news_site"] == news_sites[0].name
        assert len(data["results"]) == 2
