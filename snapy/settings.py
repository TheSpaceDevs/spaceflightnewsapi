"""Django's settings for snapy project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import sys
from pathlib import Path

import django_stubs_ext
import sentry_sdk
from environs import Env
from sentry_sdk.integrations.django import DjangoIntegration

env = Env()
env.read_env()

# Extensions for Django Stubs
django_stubs_ext.monkeypatch()

VERSION = env.str("SNAPI_VERSION")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# Get the forwarded protocol from the proxy server
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)

if DEBUG is False:
    sentry_sdk.init(
        dsn=env.str("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
        enable_tracing=True,
        release=VERSION,
    )

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGIN")

# Application definition

INSTALLED_APPS = [
    "api.apps.ApiConfig",
    "consumer.apps.ConsumerConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_celery_beat",
    "django_filters",
    "corsheaders",
    "drf_spectacular",
    "django_celery_results",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "snapy.urls"

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

LOGLEVEL = "DEBUG" if DEBUG else "INFO"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%m-%d-%Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {"handlers": ["console"], "level": LOGLEVEL, "propogate": True},
        "django": {
            "handlers": ["console"],
            "level": LOGLEVEL,
            "propagate": True,
        },
    },
}

WSGI_APPLICATION = "snapy.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {"default": env.dj_db_url("DATABASE_URL")}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# STATIC_URL = "static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"
USE_MINIO = env.bool("USE_MINIO", False)
if USE_MINIO:
    INSTALLED_APPS.append("django_minio_backend")
    MINIO_ENDPOINT = env.str("MINIO_ENDPOINT", "http://localhost:9000")
    MINIO_USE_HTTPS = True
    MINIO_ACCESS_KEY = env.str("MINIO_ACCESS_KEY", "minioadmin")
    MINIO_SECRET_KEY = env.str("MINIO_SECRET_KEY", "minioadmin")
    MINIO_PUBLIC_BUCKETS = env.list("MINIO_BUCKET_NAME", ["static"])
    MINIO_STATIC_FILES_BUCKET = env.str("MINIO_BUCKET_NAME", "static")
    MINIO_BUCKET_CHECK_ON_SAVE = True

    STATICFILES_STORAGE = "django_minio_backend.models.MinioBackendStatic"
    STATIC_URL = "https://none/"  # This is required but not used because we use STATICFILES_STORAGE.
else:
    STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "api.utils.pagination.CustomLimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Spaceflight News API",
    "DESCRIPTION": "The Spaceflight News API (SNAPI) is a product by [The Space Devs](https://thespacedevs.com) (TSD). It's the most complete and up-to-date spaceflight news API currently available."
    "\n\nWhile this API is **free to use**, we do encourage developers to support us through [Patreon](https://www.patreon.com/TheSpaceDevs) to keep the API up and running."
    "\n\n ### FAQs & Tutorials"
    "\n\n - [GitHub repository](https://github.com/TheSpaceDevs/Tutorials/): contains FAQs and tutorials for TSD APIs"
    "\n\n - [TSD FAQ](https://github.com/TheSpaceDevs/Tutorials/blob/main/faqs/faq_TSD.md): TSD-specific FAQ (e.g. history, network, funding, etc.)"
    "\n\n - [SNAPI FAQ](https://github.com/TheSpaceDevs/Tutorials/blob/main/faqs/faq_SNAPI.md): SNAPI-specific FAQ"
    "\n\n ### Feedback & Support"
    "\n\n If you need any help with SNAPI, you can ask in the "
    "[`💬feedback-and-help`](https://discord.com/channels/676725644444565514/1019976345884827750) forum of the TSD "
    "[Discord server](https://discord.gg/p7ntkNA) or email [derk@spaceflightnewsapi.net](mailto:derk@spaceflightnewsapi.net).",
    "VERSION": VERSION,
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/v4",
}

# Celery Configuration Options
CELERY_TIME_ZONE = TIME_ZONE
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_RESULT_EXTENDED = True

# LL Settings
LL_URL = env.str("LL_URL")
LL_TOKEN = env.str("LL_TOKEN", "")


# AMQP Settings
AMQP_HOST = env.str("AMQP_HOST", "localhost")
AMQP_PORT = env.int("AMQP_PORT", 5672)
AMQP_USERNAME = env.str("AMQP_USERNAME", "guest")
AMQP_PASSWORD = env.str("AMQP_PASSWORD", "guest")
AMQP_VHOST = env.str("AMQP_VHOST", "/")
AMQP_QUEUE = env.str("AMQP_QUEUE", "snapi")
AMQP_EXCHANGE = env.str("AMQP_EXCHANGE", "importer")
