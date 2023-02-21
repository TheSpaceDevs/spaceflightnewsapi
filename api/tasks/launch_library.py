import httpx
from celery import shared_task
from django.conf import settings

from api.models import Event as EventModel
from api.models import Launch as LaunchModel
from api.models import Provider
from api.types import Event, Launch

client_options = {
    "base_url": settings.LL_URL,
    "headers": {
        "Authorization": f"Token {settings.LL_TOKEN}",
        "User-Agent": "SNAPI V4",
    },
    "timeout": 30.0,
}


@shared_task(name="Sync Launches")
def sync_launches():
    next_url = "/launch/"
    provider = Provider.objects.get(name="Launch Library 2")

    with httpx.Client(**client_options) as client:
        while next_url:
            response = client.get(url=next_url).json()

            for data in response["results"]:
                launch = Launch(**data)
                LaunchModel.objects.update_or_create(
                    launch_id=launch.id,
                    defaults={"name": launch.name, "provider": provider},
                )

            next_url = response["next"]


@shared_task(name="Sync Events")
def sync_events():
    next_url = "/event/"
    provider = Provider.objects.get(name="Launch Library 2")

    with httpx.Client(**client_options) as client:
        while next_url:
            response = client.get(url=next_url).json()

            for data in response["results"]:
                event = Event(**data)
                EventModel.objects.update_or_create(
                    event_id=event.id,
                    defaults={"name": event.name, "provider": provider},
                )

            next_url = response["next"]
