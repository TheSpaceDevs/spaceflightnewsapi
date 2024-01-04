import json
import logging
from datetime import datetime
from typing import Any

import pika
from django.conf import settings
from django.core.management.base import BaseCommand

from api.serializers.importer import ArticleImportSerializer, BlogImportSerializer
from api.serializers.importer.report import ReportImportSerializer


class Command(BaseCommand):
    help = "Start consuming from the import queue."
    logger = logging.getLogger(__name__)

    def _message_callback(
        self,
        channel: pika.adapters.blocking_connection.BlockingChannel,
        method_frame: pika.spec.Basic.Deliver,
        header_frame: pika.spec.BasicProperties,
        body: bytes,
    ) -> None:
        try:
            # Decode the message
            message = json.loads(body)

            # Handle the message based on the type
            if message["type"] == "article":
                self._save_article(message["data"])

            if message["type"] == "blog":
                self._save_blog(message["data"])

            if message["type"] == "report":
                self._save_report(message["data"])

            # Acknowledge the message if there were no issues.
            # Apparently the method_frame.delivery_tag can be None,
            # so we need to check for that.
            if method_frame.delivery_tag:
                channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        except KeyError as e:
            self.logger.error(f"KeyError: {e} is probably missing from the message.")
            channel.basic_nack(delivery_tag=method_frame.delivery_tag)
        except Exception as e:
            self.logger.error(type(e))
            channel.basic_nack(delivery_tag=method_frame.delivery_tag)

    def _save_article(self, data: dict[str, str | datetime]) -> None:
        article = ArticleImportSerializer(data=data)
        article.is_valid(raise_exception=True)

        article.save()

    def _save_blog(self, data: dict[str, str | datetime]) -> None:
        blog = BlogImportSerializer(data=data)
        blog.is_valid(raise_exception=True)

        blog.save()

    def _save_report(self, data: dict[str, str | datetime]) -> None:
        report = ReportImportSerializer(data=data)
        report.is_valid(raise_exception=True)

        report.save()

    def handle(self, *args: Any, **kwargs: Any) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=settings.AMQP_HOST,
                port=settings.AMQP_PORT,
                virtual_host=settings.AMQP_VHOST,
                credentials=pika.PlainCredentials(
                    settings.AMQP_USERNAME, settings.AMQP_PASSWORD
                ),
            )
        )

        # Create the channel
        channel = connection.channel()

        # Check that the channel exists
        channel.queue_declare(queue="snapi", passive=True)

        # Start consuming from the snapi queue
        channel.basic_consume("snapi", self._message_callback)

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()

        connection.close()
