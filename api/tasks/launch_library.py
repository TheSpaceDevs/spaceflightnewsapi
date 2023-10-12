import httpx
from celery import shared_task
from django.conf import settings

from api.models import Provider
from api.serializers.launch_library import (
    LaunchLibraryEventSerializer,
    LaunchLibraryLaunchSerializer,
)
from api.serializers.utils import ClientOptions

client_options: ClientOptions = {
    "base_url": settings.LL_URL,
    "headers": {
        "Authorization": f"Token {settings.LL_TOKEN}",
        "User-Agent": "SNAPI V4",
    },
    "timeout": 1440.0,
}


@shared_task(name="Sync Launches")
def sync_launches():
    next_url = "/launch/"
    provider = Provider.objects.get(name="Launch Library 2")

    with httpx.Client(**client_options) as client:
        while next_url:
            response = client.get(url=next_url).json()

            for data in response["results"]:
                launch = LaunchLibraryLaunchSerializer(
                    data=data, context={"provider": provider}
                )
                launch.is_valid(raise_exception=True)
                launch.save()

            next_url = response["next"]


@shared_task(name="Sync Events")
def sync_events():
    next_url = "/event/"
    provider = Provider.objects.get(name="Launch Library 2")

    with httpx.Client(**client_options) as client:
        while next_url:
            response = client.get(url=next_url).json()

            for data in response["results"]:
                event = LaunchLibraryEventSerializer(
                    data=data, context={"provider": provider}
                )
                event.is_valid(raise_exception=True)
                event.save()

            next_url = response["next"]
