import pytest
from rest_framework.exceptions import ValidationError

from api.models import NewsSite
from consumer.mq_consumer import MqConsumer


@pytest.mark.django_db
class TestConsumer:
    mq_consumer = MqConsumer()

    def test_saving_article(self, news_sites: list[NewsSite]) -> None:
        data = {
            "type": "article",
            "data": {
                "title": "TheBigCombo",
                "url": "https://www.youtube.com/watch?v=5g4lY8Y3eoo",
                "imageUrl": "https://i.ytimg.com/vi/5g4lY8Y3eoo/hqdefault.jpg",
                "newsSite": 1,
                "summary": "wieuhfgiuwehfguiweg",
                "publishedAt": "2021-02-13T00:0:00.000Z",
            },
        }

        # Ignore the type error since the real implementation of this method is called with a different object.
        self.mq_consumer._save_article(data["data"])  # type: ignore

    def test_saving_article_no_title(self, news_sites: list[NewsSite]) -> None:
        data = {
            "type": "article",
            "data": {
                "url": "https://www.youtube.com/watch?v=5g4lY8Y3eoo",
                "imageUrl": "https://i.ytimg.com/vi/5g4lY8Y3eoo/hqdefault.jpg",
                "newsSite": 1,
                "summary": "wieuhfgiuwehfguiweg",
                "publishedAt": "2021-02-13T00:00:00.000Z",
            },
        }

        with pytest.raises(ValidationError):
            self.mq_consumer._save_article(data["data"])  # type: ignore
