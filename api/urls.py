from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from api import views

api_router = routers.SimpleRouter()
api_router.register(r"articles", views.ArticleViewSet, basename="articles")
api_router.register(r"blogs", views.BlogViewSet, basename="blogs")
api_router.register(r"reports", views.ReportViewSet, basename="reports")

urlpatterns = [
    path("", RedirectView.as_view(url="docs/")),
    path("", include(api_router.urls)),
    path("info/", views.InfoView.as_view()),
    path("schema/", SpectacularAPIView.as_view(api_version="v4"), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
