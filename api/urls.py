from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from api import views

api_router = routers.SimpleRouter()
api_router.register(r"articles", views.ArticleViewSet, basename="articles")
api_router.register(r"blogs", views.BlogViewSet, basename="blogs")
api_router.register(r"reports", views.ReportViewSet, basename="reports")

urlpatterns = [
    path("", include(api_router.urls)),
    path("schema/", SpectacularAPIView.as_view(api_version="v4"), name="schema"),
    path(
        "documentation/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),  # Temp on the v4 path to not conflict with v3.
]
