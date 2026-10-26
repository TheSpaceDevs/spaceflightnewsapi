"""Tests the per-site cache of the API responses."""

import pytest
from django.db import connection
from django.http.response import ResponseHeaders
from django.test.client import Client
from django.test.utils import CaptureQueriesContext

from api.models import Article

URL = "/v4/articles/?limit=5"

JSON_ACCEPTS = [None, "*/*", "application/json", "application/json, text/plain, */*", "application/*"]
ORIGINS = [None, "https://app-one.example", "https://app-two.example"]


def _get(client: Client, accept: str | None = None, origin: str | None = None) -> tuple[int, ResponseHeaders, int]:
    """Returns the status, headers and number of database queries of a request."""
    headers = {}
    if accept is not None:
        headers["Accept"] = accept
    if origin is not None:
        headers["Origin"] = origin
    with CaptureQueriesContext(connection) as ctx:
        response = client.get(URL, headers=headers)
    return response.status_code, response.headers, len(ctx.captured_queries)


@pytest.mark.django_db
@pytest.mark.usefixtures("articles")
class TestResponseCache:
    def test_json_clients_share_one_cache_entry(self, client: Client) -> None:
        _get(client)

        for origin in ORIGINS:
            for accept in JSON_ACCEPTS:
                status, headers, queries = _get(client, accept, origin)

                assert status == 200
                assert headers["Content-Type"] == "application/json"
                assert queries == 0, f"cache miss for Accept={accept!r} Origin={origin!r}"

    def test_cached_responses_have_cors_headers(self, client: Client) -> None:
        _get(client)

        _, headers, queries = _get(client, origin="https://app-one.example")

        assert queries == 0
        assert headers["Access-Control-Allow-Origin"] == "*"

    def test_browsers_get_html(self, client: Client) -> None:
        _get(client)

        status, headers, _ = _get(client, "text/html,application/xhtml+xml,*/*;q=0.8")

        assert status == 200
        assert headers["Content-Type"].startswith("text/html")

    def test_unsupported_media_type_is_still_rejected(self, client: Client) -> None:
        status, _, _ = _get(client, "application/xml")

        assert status == 406

    def test_cache_is_per_url(self, client: Client, articles: list[Article]) -> None:
        _get(client)

        with CaptureQueriesContext(connection) as ctx:
            assert client.get("/v4/articles/?limit=6").status_code == 200

        assert len(ctx.captured_queries) > 0
