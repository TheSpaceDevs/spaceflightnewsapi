import json
import logging
from datetime import datetime

import pika
from django.conf import settings

from api.serializers.importer import ArticleImportSerializer, BlogImportSerializer
from api.serializers.importer.report import ReportImportSerializer


class MqConsumer:
    logger = logging.getLogger(__name__)
    connection: pika.BlockingConnection

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

            match message["type"]:
                case "article":
                    self._save_article(message["data"])
                case "blog":
                    self._save_blog(message["data"])
                case "report":
                    self._save_report(message["data"])
                case _:
                    channel.basic_nack(
                        delivery_tag=method_frame.delivery_tag, requeue=False
                    )

            # Acknowledge the message if there were no issues.
            # Apparently the method_frame.delivery_tag can be None,
            # so we need to check for that.
            if method_frame.delivery_tag:
                channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        except KeyError as e:
            self.logger.error(f"KeyError: {e} is probably missing from the message.")
            channel.basic_nack(delivery_tag=method_frame.delivery_tag, requeue=False)
        except Exception as e:
            self.logger.error(f"Error processing message. Error: {e}")
            channel.basic_nack(delivery_tag=method_frame.delivery_tag, requeue=False)

    def _save_data(
        self,
        serializer_class: type[
            ArticleImportSerializer | BlogImportSerializer | ReportImportSerializer
        ],
        data: dict[str, str | datetime],
    ) -> None:
        serializer = serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.logger.info(
            f"Saved {serializer_class.__name__} with title: {serializer.validated_data['title']}"
        )

    def _save_article(self, data: dict[str, str | datetime]) -> None:
        self._save_data(ArticleImportSerializer, data)

    def _save_blog(self, data: dict[str, str | datetime]) -> None:
        self._save_data(BlogImportSerializer, data)

    def _save_report(self, data: dict[str, str | datetime]) -> None:
        self._save_data(ReportImportSerializer, data)

    def consume(self) -> None:
        self.connection = pika.BlockingConnection(
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
        channel = self.connection.channel()

        # Check that the channel exists
        channel.queue_declare(queue=settings.AMQP_QUEUE, passive=True)

        # Start consuming from the snapi queue
        channel.basic_consume(settings.AMQP_QUEUE, self._message_callback)

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
        finally:
            self.connection.close()
