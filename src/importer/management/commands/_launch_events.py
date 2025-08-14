from typing import TypedDict

import httpx
from django.conf import settings

from api.models import Provider
from importer.serializers import LaunchLibraryEventSerializer, LaunchLibraryLaunchSerializer

try:
    provider = Provider.objects.get(name="Launch Library 2")
except Provider.DoesNotExist:
    raise ValueError("Launch Library 2 provider does not exist. Please create it before running this command.")


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


def fetch_launches() -> None:
    next_url = "/launch/"

    with httpx.Client(base_url=client_options["base_url"], timeout=1440, headers=client_options["headers"]) as client:
        while next_url:
            response = client.get(url=next_url)
            response.raise_for_status()

            data = response.json()

            for launch in data["results"]:
                launch = LaunchLibraryLaunchSerializer(data=launch, context={"provider": provider})
                launch.is_valid(raise_exception=True)
                launch.save()

            next_url = data["next"]


def fetch_events() -> None:
    next_url = "/event/"

    with httpx.Client(base_url=client_options["base_url"], timeout=1400, headers=client_options["headers"]) as client:
        while next_url:
            response = client.get(url=next_url)
            response.raise_for_status()

            data = response.json()

            for event in data["results"]:
                event = LaunchLibraryEventSerializer(data=event, context={"provider": provider})
                event.is_valid(raise_exception=True)
                event.save()

            next_url = data["next"]
