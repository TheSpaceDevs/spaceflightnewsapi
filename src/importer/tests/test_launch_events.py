"""Tests importing launches and events from Launch Library 2."""

from collections.abc import Callable
from datetime import UTC, datetime
from typing import Any
from uuid import UUID

import httpx
import pytest

from api.models import Event, Launch, Provider
from importer.management.commands._launch_events import fetch_events, fetch_launches

LL2_URL = "https://ll.example.com/2.3.0"


class FakeLaunchLibrary:
    """Serves the given pages in order and records the requests made."""

    def __init__(self, pages: list[list[dict[str, Any]]]) -> None:
        self.pages = pages
        self.requests: list[httpx.Request] = []

    def handler(self, request: httpx.Request) -> httpx.Response:
        index = len(self.requests)
        self.requests.append(request)
        next_url = f"{LL2_URL}{request.url.path}?offset={index + 1}" if index + 1 < len(self.pages) else None
        return httpx.Response(200, json={"count": 0, "next": next_url, "previous": None, "results": self.pages[index]})

    def client(self) -> httpx.Client:
        return httpx.Client(base_url=LL2_URL, transport=httpx.MockTransport(self.handler))


def _launch(i: int, name: str, last_updated: str) -> dict[str, Any]:
    return {"id": str(UUID(int=i)), "name": name, "last_updated": last_updated}


def _event(i: int, name: str, last_updated: str) -> dict[str, Any]:
    return {"id": i, "name": name, "last_updated": last_updated}


# endpoint: (fetch function, model, id field, result factory, id converter)
ENDPOINTS: dict[str, tuple[Callable[..., None], Any, str, Callable[..., dict[str, Any]], Callable[[int], Any]]] = {
    "launches": (fetch_launches, Launch, "launch_id", _launch, lambda i: UUID(int=i)),
    "events": (fetch_events, Event, "event_id", _event, lambda i: i),
}


@pytest.fixture
def provider() -> Provider:
    return Provider.objects.create(name="Launch Library 2")


@pytest.mark.django_db
@pytest.mark.parametrize("endpoint", ENDPOINTS)
class TestLaunchLibraryImport:
    def test_first_import_fetches_everything(self, provider: Provider, endpoint: str) -> None:
        fetch, model, id_field, result, to_id = ENDPOINTS[endpoint]
        ll2 = FakeLaunchLibrary(
            [
                [result(1, "One", "2026-01-01T00:00:00Z"), result(2, "Two", "2026-01-02T00:00:00Z")],
                [result(3, "Three", "2026-01-03T00:00:00Z")],
            ]
        )

        fetch(client=ll2.client())

        first = ll2.requests[0].url
        assert first.path == f"/2.3.0/{endpoint}/"
        assert first.params["ordering"] == "last_updated"
        assert "last_updated__gte" not in first.params
        # The next page is fetched through the `next` link.
        assert ll2.requests[1].url.params["offset"] == "1"

        items = {getattr(item, id_field): item for item in model.objects.all()}
        assert set(items) == {to_id(1), to_id(2), to_id(3)}
        assert items[to_id(3)].name == "Three"
        assert items[to_id(3)].last_updated == datetime(2026, 1, 3, tzinfo=UTC)
        assert items[to_id(3)].provider == provider

    def test_later_import_only_fetches_updates(self, provider: Provider, endpoint: str) -> None:
        fetch, model, id_field, result, to_id = ENDPOINTS[endpoint]
        for i, last_updated in ((1, datetime(2026, 1, 1, tzinfo=UTC)), (2, datetime(2026, 1, 5, tzinfo=UTC))):
            model.objects.create(**{id_field: to_id(i)}, name=f"Old {i}", provider=provider, last_updated=last_updated)
        ll2 = FakeLaunchLibrary(
            [[result(2, "Renamed", "2026-01-06T00:00:00Z"), result(3, "New", "2026-01-07T00:00:00Z")]]
        )

        fetch(client=ll2.client())

        assert ll2.requests[0].url.params["last_updated__gte"] == "2026-01-05T00:00:00+00:00"
        names = {getattr(item, id_field): item.name for item in model.objects.all()}
        assert names == {to_id(1): "Old 1", to_id(2): "Renamed", to_id(3): "New"}

    def test_full_import_ignores_previous_updates(self, provider: Provider, endpoint: str) -> None:
        fetch, model, id_field, result, to_id = ENDPOINTS[endpoint]
        model.objects.create(
            **{id_field: to_id(1)}, name="Old", provider=provider, last_updated=datetime(2026, 1, 5, tzinfo=UTC)
        )
        ll2 = FakeLaunchLibrary([[result(1, "One", "2026-01-01T00:00:00Z")]])

        fetch(client=ll2.client(), full=True)

        assert "last_updated__gte" not in ll2.requests[0].url.params
        assert model.objects.get().name == "One"

    def test_queries_per_page_are_constant(
        self, provider: Provider, endpoint: str, django_assert_max_num_queries: Any
    ) -> None:
        fetch, _, _, result, _ = ENDPOINTS[endpoint]
        ll2 = FakeLaunchLibrary([[result(i, f"Item {i}", "2026-01-01T00:00:00Z") for i in range(1, 51)]] * 2)

        # Provider, latest update and one upsert per page.
        with django_assert_max_num_queries(4):
            fetch(client=ll2.client())

    def test_missing_provider(self, endpoint: str) -> None:
        fetch, *_ = ENDPOINTS[endpoint]

        with pytest.raises(ValueError, match="Launch Library 2 provider does not exist"):
            fetch(client=FakeLaunchLibrary([[]]).client())
