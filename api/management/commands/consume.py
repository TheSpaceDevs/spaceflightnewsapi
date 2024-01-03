import json
from typing import Any

import pika
from django.core.management.base import BaseCommand

from api.serializers.importer import ArticleImportSerializer, BlogImportSerializer
from api.serializers.importer.report import ReportImportSerializer


class Command(BaseCommand):
    help = "Start consuming from the article, blog and report queues."

    def _article_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        try:
            article = ArticleImportSerializer(data=json.loads(body))
            article.is_valid(raise_exception=True)

            article.save()
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        except Exception as e:
            print(e)
            channel.basic_nack(delivery_tag=method_frame.delivery_tag)

    def _blog_message_callback(self, channel, method_frame, header_frame, body) -> None:
        try:
            blog = BlogImportSerializer(data=json.loads(body))
            blog.is_valid(raise_exception=True)

            blog.save()
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        except Exception as e:
            print(e)
            channel.basic_nack(delivery_tag=method_frame.delivery_tag)

    def _report_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        try:
            report = ReportImportSerializer(data=json.loads(body))
            report.is_valid(raise_exception=True)

            report.save()
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        except Exception as e:
            print(e)
            channel.basic_nack(delivery_tag=method_frame.delivery_tag)

    def handle(self, *args: Any, **kwargs: Any) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="localhost", credentials=pika.PlainCredentials("guest", "guest")
            )
        )

        channel = connection.channel()

        channel.basic_consume("articles", self._article_message_callback)
        channel.basic_consume("blogs", self._blog_message_callback)
        channel.basic_consume("reports", self._report_message_callback)

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
        connection.close()
