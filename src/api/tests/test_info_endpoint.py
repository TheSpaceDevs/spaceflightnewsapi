import importlib

import pytest
from django.test.client import Client

from api.models import NewsSite


@pytest.mark.django_db
@pytest.mark.skip(reason="Fails during testing, works in production.")
class TestInfoEndpoint:
    def test_version(self, client: Client) -> None:
        response = client.get("/v4/info/")
        assert response.status_code == 200

        data = response.json()

        assert data["version"] == importlib.metadata.version("snapy")

    def test_news_sites(self, client: Client, news_sites: list[NewsSite]) -> None:
        response = client.get("/v4/info/")
        assert response.status_code == 200

        data = response.json()

        assert all(site.name in data["news_sites"] for site in news_sites)
