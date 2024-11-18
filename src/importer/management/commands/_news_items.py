import logging
import time

from harvester import sources
from harvester.schemas import ArticleSchema, BlogSchema, ReportSchema

from api.models import Article, Blog, NewsSite, Report

logger = logging.getLogger(__name__)
news_sites = NewsSite.objects.all()


def process_article(article: ArticleSchema) -> None:
    # Get the news site
    news_site = news_sites.get(id=article.news_site_id)

    # Check if the article already exists
    if Article.objects.filter(title=article.title, url=article.url).exists():
        logger.debug(f"Article {article.title} already exists")
        return

    logger.info(f"Adding article: {article.title}")

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
    # Get the news site
    news_site = news_sites.get(id=blog.news_site_id)

    # Check if the blog already exists
    if Blog.objects.filter(title=blog.title, url=blog.url).exists():
        logger.info(f"Blog {blog.title} already exists")
        return

    logger.info(f"Adding blog: {blog.title}")

    # Create the blog
    Blog.objects.create(
        title=blog.title,
        url=blog.url,
        news_site=news_site,
        published_at=blog.published_at,
        summary=blog.summary,
        image_url=blog.image_url,
    )


def process_report(report: ReportSchema) -> None:
    # Get the news site
    news_site = news_sites.get(id=report.news_site_id)

    # Check if the report already exists
    if Report.objects.filter(title=report.title, url=report.url).exists():
        logger.info(f"Report {report.title} already exists")
        return

    logger.info(f"Adding report: {report.title}")

    # Create the report
    Report.objects.create(
        title=report.title,
        url=report.url,
        news_site=news_site,
        published_at=report.published_at,
        summary=report.summary,
        image_url=report.image_url,
    )


def fetch_news() -> None:
    logger.info("Fetching news")
    starttime = time.time()

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
            logger.error(f"Error processing {source}: {e}")

    logger.info(f"Finished fetching news in {time.time() - starttime} seconds")
