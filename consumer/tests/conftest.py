import pytest

from api.models import NewsSite

NUMBER_OF_NEWS_SITES = 20


@pytest.fixture
def news_sites() -> list[NewsSite]:
    sites: list[NewsSite] = []
    for i in range(NUMBER_OF_NEWS_SITES):
        site = NewsSite.objects.create(name=f"News Site {i}")
        sites.append(site)

    return sites
