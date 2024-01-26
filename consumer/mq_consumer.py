import json
import logging
from pprint import pprint

import pika
from django.conf import settings

from consumer.serializers import (
    ArticleImportSerializer,
    BlogImportSerializer,
    ReportImportSerializer,
)


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

            pprint(message)

            match message["type"]:
                case "article":
                    self._save_data(ArticleImportSerializer, message["data"])
                case "blog":
                    self._save_data(BlogImportSerializer, message["data"])
                case "report":
                    self._save_data(ReportImportSerializer, message["data"])
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
        data: dict[str, str | dict[str, str | int]],
    ) -> None:
        serializer = serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.logger.info(
            f"Saved {serializer_class.__name__} with title: {serializer.validated_data['title']}"
        )

    def consume(self) -> None:
        self.connection = pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host=settings.AMQP_HOST,
                port=settings.AMQP_PORT,
                virtual_host=settings.AMQP_VHOST,
                credentials=pika.PlainCredentials(
                    username=settings.AMQP_USERNAME, password=settings.AMQP_PASSWORD
                ),
            )
        )

        # Create the channel
        channel = self.connection.channel()

        # Check that the queue exists
        channel.queue_declare(queue=settings.AMQP_QUEUE, durable=True)

        # Bind the queue to the exchange
        channel.queue_bind(exchange=settings.AMQP_EXCHANGE, queue=settings.AMQP_QUEUE)

        # Start consuming from the snapi queue
        channel.basic_consume(
            queue=settings.AMQP_QUEUE, on_message_callback=self._message_callback
        )

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
        finally:
            self.connection.close()
