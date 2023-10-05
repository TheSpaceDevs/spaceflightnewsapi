import pytest

from api.models import Article, Launch


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

    def test_get_all_articles_with_launches(
        self, client, articles: list[Article], launches: list[Launch]
    ):
        response = client.get("/v4/articles/?has_launch=true")
        assert response.status_code == 200

        data = response.json()

        assert len(data["results"]) == 2
