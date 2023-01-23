"""snapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api import views

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'blogs', views.BlogViewSet)
router.register(r'reports', views.ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('openapi.json', get_schema_view(
        title="Spaceflight News API",
        description="Documentation for the Spaceflight News API. Join The Space Devs Discord server to contact me for "
                    "support :)",
        version=settings.VERSION
    ), name='openapi-schema'),
    path('documentation/', TemplateView.as_view(
        template_name='api/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
]
