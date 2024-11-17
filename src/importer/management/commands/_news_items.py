import logging

from harvester import sources
from harvester.schemas import ArticleSchema, BlogSchema, ReportSchema

from api.models import Article, NewsSite

logger = logging.getLogger(__name__)


def process_article(article: ArticleSchema) -> None:
    logger.info(f"Processing article: {article.title}")

    # Get the news site
    news_site = NewsSite.objects.get(id=article.news_site_id)

    # Check if the article already exists
    if Article.objects.filter(title=article.title, url=article.url).exists():
        logger.info(f"Article {article.title} already exists")
        return

    # Create the article
    Article.objects.create(
        title=article.title,
        url=article.url,
        news_site=news_site,
        published_at=article.published_at,
        summary=article.summary,
        image_url=article.image_url,
    )


def process_blog(blog: BlogSchema) -> None:
    logger.info(f"Processing blog: {blog.title}")


def process_report(report: ReportSchema) -> None:
    logger.info(f"Processing report: {report.title}")


def fetch_news() -> None:
    for source in sources:
        try:
            data = source.harvest()

            if data.articles:
                for article in data.articles:
                    process_article(article=article)

            if data.blogs:
                for blog in data.blogs:
                    process_blog(blog=blog)

            if data.reports:
                for report in data.reports:
                    process_report(report=report)

        except Exception as e:
            print(f"Error processing {source}: {e}")
            continue
