"""Django's settings for snapy project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import importlib.metadata
from pathlib import Path

import django_stubs_ext
from environs import Env

env = Env()
env.read_env()

# Extensions for Django Stubs
django_stubs_ext.monkeypatch()

VERSION = importlib.metadata.version("snapy")

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


if env.str("SENTRY_DSN", None):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=env.str("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=0.01,
        send_default_pii=True,
        enable_tracing=True,
        release=VERSION,
        environment=env.str("SENTRY_ENVIRONMENT"),
    )

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGIN")

# Application definition

INSTALLED_APPS = [
    "api",
    "importer",
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "corsheaders",
    "drf_spectacular",
    "storages",
    "health_check",
    "health_check.cache",
    "health_check.db",
    "health_check.contrib.s3boto3_storage",
    "health_check.contrib.redis",
    "graphene_django",
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
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

JET_DEFAULT_THEME = "dark"

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
if env.bool("USE_S3", False):
    AWS_QUERYSTRING_AUTH = False
    AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_ENDPOINT_URL = "https://ams3.digitaloceanspaces.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    AWS_PRELOAD_METADATA = True
    AWS_IS_GZIPPED = True

    # static settings
    AWS_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
else:
    STATIC_URL = "static/"
    STATIC_ROOT = BASE_DIR.joinpath("staticfiles")

STATICFILES_DIRS = [BASE_DIR.joinpath("static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "api.utils.pagination.CustomLimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Spaceflight News API",
    "DESCRIPTION": "The Spaceflight News API (SNAPI) is a product by [The Space Devs](https://thespacedevs.com) (TSD). It's the most complete and up-to-date spaceflight news API currently available."
    "\n\nWhile this API is **free to use**, we do encourage developers to support us through [Patreon](https://www.patreon.com/TheSpaceDevs) to keep the API up and running."
    "\n\n ### GraphQL"
    "\n\n The Spaceflight News API also has GraphQL support available! You can find the GraphiQl IDE [here](https://api.spaceflightnewsapi.net/v4/graphql/)."
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

# LL Settings
LL_URL = env.str("LL_URL", "https://lldev.thespacedevs.com/2.2.0")
LL_TOKEN = env.str("LL_TOKEN", "")

HEALTH_CHECK = {
    "SUBSETS": {
        "startup-probe": ["MigrationsHealthCheck", "DatabaseBackend", "CacheBackend"],
        "liveness-probe": ["DatabaseBackend"],
    },
}

GRAPHENE = {
    "SCHEMA": "snapy.schema.schema",
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env.str("REDIS_URL", "redis://localhost:6379"),
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]
