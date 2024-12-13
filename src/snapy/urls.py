"""snapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/

Examples
--------
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

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, re_path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView  # type: ignore

urlpatterns = [
    # Jet URLs
    re_path(r"^v4/jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),  # Django JET dashboard URLS
    re_path(r"^v4/jet/", include("jet.urls", "jet")),  # Django JET URLS
    # GraphQL URLs
    re_path(r"^v4/graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # API URLs
    re_path(r"^v4/", include(("api.urls", "api"), namespace="v4")),
    # Non v4 URLs
    re_path(r"health/", include("health_check.urls")),
    re_path(r"admin/", admin.site.urls),
] + debug_toolbar_urls()
