from typing import TypedDict

import httpx
from django.conf import settings

from api.models import Provider
from importer.serializers import LaunchLibraryEventSerializer, LaunchLibraryLaunchSerializer

provider = Provider.objects.get(name="Launch Library 2")


class ClientOptions(TypedDict):
    base_url: str
    headers: dict[str, str]
    timeout: float


client_options: ClientOptions = {
    "base_url": settings.LL_URL,
    "headers": {
        "Authorization": f"Token {settings.LL_TOKEN}",
        "User-Agent": f"SNAPI {settings.VERSION}",
    },
    "timeout": 1440.0,
}


def fetch_launches() -> None:
    next_url = "/launch/"

    with httpx.Client(
        base_url=client_options["base_url"], timeout=client_options["timeout"], headers=client_options["headers"]
    ) as client:
        while next_url:
            response = client.get(url=next_url).json()

            for data in response["results"]:
                launch = LaunchLibraryLaunchSerializer(data=data, context={"provider": provider})
                launch.is_valid(raise_exception=True)
                launch.save()

            next_url = response["next"]


def fetch_events() -> None:
    next_url = "/event/"

    with httpx.Client(
        base_url=client_options["base_url"], timeout=client_options["timeout"], headers=client_options["headers"]
    ) as client:
        while next_url:
            response = client.get(url=next_url).json()

            for data in response["results"]:
                event = LaunchLibraryEventSerializer(data=data, context={"provider": provider})
                event.is_valid(raise_exception=True)
                event.save()

            next_url = response["next"]
