from logging import INFO, WARN, basicConfig, getLogger
from typing import Any, TypedDict

import httpx
from django.conf import settings
from django.db.models import Max
from rest_framework import serializers

from api.models import Event, Launch, Provider
from importer.serializers import LaunchLibraryEventSerializer, LaunchLibraryLaunchSerializer

LOGGER = getLogger(__name__)
basicConfig(level=INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# disable httpx INFO logging
httpx_logger = getLogger("httpx")
httpx_logger.setLevel(WARN)

# The maximum page size Launch Library 2 allows.
PAGE_SIZE = 100


class ClientOptions(TypedDict):
    base_url: str
    headers: dict[str, str]


# Not setting the timout on this dict since Bandit doesn't like it
client_options: ClientOptions = {
    "base_url": settings.LL_URL,
    "headers": {
        "Authorization": f"Token {settings.LL_TOKEN}",
        "User-Agent": f"SNAPI {settings.VERSION}",
    },
}


def _get_provider() -> Provider:
    try:
        return Provider.objects.get(name="Launch Library 2")
    except Provider.DoesNotExist:
        raise ValueError("Launch Library 2 provider does not exist. Please create it before running this command.")


def _import[M: (Launch, Event)](
    client: httpx.Client,
    endpoint: str,
    model: type[M],
    id_field: str,
    serializer_class: type[serializers.Serializer[Any]],
    full: bool,
    params: dict[str, str],
) -> None:
    """Imports everything Launch Library 2 updated since the previous import, or everything when `full` is set.

    Items are fetched oldest update first, so an import that stops halfway continues where it left off next time.
    """
    provider = _get_provider()
    since = None if full else model.objects.filter(provider=provider).aggregate(Max("last_updated"))["last_updated__max"]

    query = {**params, "ordering": "last_updated", "limit": str(PAGE_SIZE)}
    if since:
        query["last_updated__gte"] = since.isoformat()

    LOGGER.info(f"Fetching {endpoint} updated since {since.isoformat() if since else 'the beginning'}")
    next_url: str | None = f"/{endpoint}/"
    first_page = True
    imported = 0

    while next_url:
        # The `next` link already contains the query parameters.
        response = client.get(next_url, params=query if first_page else None)
        first_page = False
        response.raise_for_status()
        data = response.json()

        serializer = serializer_class(data=data["results"], many=True)
        serializer.is_valid(raise_exception=True)

        # Keyed by id, as an upsert can't contain the same item twice.
        items = {
            item["id"]: model(
                **{id_field: item["id"]}, name=item["name"], last_updated=item["last_updated"], provider=provider
            )
            for item in serializer.validated_data
        }
        # One upsert per page instead of a SELECT and UPDATE/INSERT per item.
        model.objects.bulk_create(
            list(items.values()),
            update_conflicts=True,
            unique_fields=[id_field],
            update_fields=["name", "provider", "last_updated"],
        )

        imported += len(items)
        next_url = data["next"]

    LOGGER.info(f"Finished fetching {endpoint}, imported {imported}.")


def fetch_launches(client: httpx.Client | None = None, full: bool = False) -> None:
    with client or httpx.Client(timeout=1440, **client_options) as client:
        _import(client, "launches", Launch, "launch_id", LaunchLibraryLaunchSerializer, full, {"mode": "list"})


def fetch_events(client: httpx.Client | None = None, full: bool = False) -> None:
    # The list mode of events doesn't include `last_updated`, the normal mode does.
    with client or httpx.Client(timeout=1440, **client_options) as client:
        _import(client, "events", Event, "event_id", LaunchLibraryEventSerializer, full, {"mode": "normal"})
