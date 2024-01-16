import logging
from typing import Any

from django.core.management.base import BaseCommand

from consumer.mq_consumer import MqConsumer


class Command(BaseCommand):
    help = "Start consuming from the import queue."
    logger = logging.getLogger(__name__)

    consumer = MqConsumer()

    def handle(self, *args: Any, **kwargs: Any) -> None:
        self.logger.info("Starting to consume from the import queue.")
        self.consumer.consume()
