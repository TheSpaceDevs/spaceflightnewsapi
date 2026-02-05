"""WSGI config for snapy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from granian.utils.proxies import wrap_wsgi_with_proxy_headers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snapy.settings")

application = wrap_wsgi_with_proxy_headers(get_wsgi_application(), trusted_hosts="*")
