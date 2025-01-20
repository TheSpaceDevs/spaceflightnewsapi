import logging
import time
from functools import lru_cache

from harvester import sources
from harvester.schemas import ArticleSchema, BlogSchema, ReportSchema

from api.models import Article, Author, Blog, NewsSite, Report

logger = logging.getLogger(__name__)


@lru_cache
def _get_author(author_name: str) -> Author:
    author_name = author_name.strip()
    author = Author.objects.filter(name=author_name).first()
    if not author:
        logger.info(f"Adding author: {author_name}")
        author = Author.objects.create(name=author_name)

    return author


@lru_cache
def _get_news_site(id: int) -> NewsSite:
    news_site = NewsSite.objects.get(id=id)
    return news_site


def process_article(article: ArticleSchema) -> None:
    # Get the news site
    news_site = _get_news_site(id=article.news_site_id)
    author = _get_author(author_name=article.author)

    # Check if the article already exists
    if Article.objects.filter(url=article.url).exists():
        logger.debug(f"Article {article.title} already exists")
        return

    logger.info(f"Adding article: {article.title}")

    # Create the article
    new_article = Article.objects.create(
        title=article.title,
        url=str(article.url),
        news_site=news_site,
        published_at=article.published_at,
        summary=article.summary,
        image_url=str(article.image_url),
    )

    new_article.authors.add(author)


def process_blog(blog: BlogSchema) -> None:
    # Get the news site
    news_site = _get_news_site(id=blog.news_site_id)
    author = _get_author(author_name=blog.author)

    # Check if the blog already exists
    if Blog.objects.filter(url=blog.url).exists():
        logger.debug(f"Blog {blog.title} already exists")
        return

    logger.info(f"Adding blog: {blog.title}")

    # Create the blog
    new_blog = Blog.objects.create(
        title=blog.title,
        url=str(blog.url),
        news_site=news_site,
        published_at=blog.published_at,
        summary=blog.summary,
        image_url=str(blog.image_url),
    )

    new_blog.authors.add(author)


def process_report(report: ReportSchema) -> None:
    # Get the news site
    news_site = _get_news_site(id=report.news_site_id)
    author = _get_author(author_name=report.author)

    # Check if the report already exists
    if Report.objects.filter(url=report.url).exists():
        logger.debug(f"Report {report.title} already exists")
        return

    logger.info(f"Adding report: {report.title}")

    # Create the report
    new_report = Report.objects.create(
        title=report.title,
        url=str(report.url),
        news_site=news_site,
        published_at=report.published_at,
        summary=report.summary,
        image_url=str(report.image_url),
    )

    new_report.authors.add(author)


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
