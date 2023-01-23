import httpx
from celery import shared_task
from django.conf import settings

from api.models import Provider, Event as EventModel
from api.types import Event


@shared_task
def sync_events():
    next_url = f"{settings.LL_URL}/event/"

    while next_url:
        response = httpx.get(next_url).json()

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
        name=event.name,
        event_id=event.id,
        provider=provider
    )
