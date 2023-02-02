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
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"articles", views.ArticleViewSet, basename="articles")
router.register(r"blogs", views.BlogViewSet, basename="blogs")
router.register(r"reports", views.ReportViewSet, basename="reports")

urlpatterns = [
    path("v4/", include(router.urls)),
    path("v4/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "v4/documentation/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("v4/admin/", admin.site.urls),
]
