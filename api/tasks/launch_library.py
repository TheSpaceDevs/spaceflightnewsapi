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

    with httpx.Client(**client_options) as client:
        while next_url:
            response = client.get(url=next_url).json()

            for launch in response["results"]:
                process_launch.delay(launch)

            next_url = response["next"]


@shared_task
def process_launch(data):
    # Get the Provider object
    provider = Provider.objects.get(name="Launch Library 2")
    # Deserialize the received JSON object into a Python object.
    # This will validate the incoming data.
    launch = Launch(**data)

    LaunchModel.objects.update_or_create(
        name=launch.name, launch_id=launch.id, provider=provider
    )


@shared_task(name="Sync Events")
def sync_events():
    next_url = "/event/"

    with httpx.Client(**client_options) as client:
        while next_url:
            response = client.get(url=next_url).json()

            for event in response["results"]:
                process_event.delay(event)

            next_url = response["next"]


@shared_task
def process_event(data):
    # Get the Provider object
    provider = Provider.objects.get(name="Launch Library 2")
    # Deserialize the received JSON object into a Python object.
    # This will validate the incoming data.
    event = Event(**data)

    EventModel.objects.update_or_create(
        name=event.name, event_id=event.id, provider=provider
    )
