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
from django.urls import include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    re_path(r"^v4/", include(("api.urls", "api"), namespace="v4")),
    re_path(
        r"^v4/schema/", SpectacularAPIView.as_view(api_version="v4"), name="schema"
    ),
    re_path(
        r"^v4/documentation/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),  # Temp on the v4 path to not conflict with v3.
    re_path(
        r"^v4/admin/", admin.site.urls
    ),  # Temp on the v4 path to not conflict with v3.
]
