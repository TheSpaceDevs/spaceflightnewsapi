import pytest

from api.models import NewsSite


@pytest.fixture
def news_sites() -> list[NewsSite]:
    sites: list[NewsSite] = []
    for i in range(5):
        site = NewsSite.objects.create(name=f"News Site {i}")
        sites.append(site)

    return sites
