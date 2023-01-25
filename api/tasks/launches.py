import httpx
from celery import shared_task
from django.conf import settings

from api.models import Launch as LaunchModel
from api.models import Provider
from api.types import Launch


@shared_task
def sync_launches():
    next_url = f"{settings.LL_URL}/launch/"

    while next_url:
        response = httpx.get(next_url).json()

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
