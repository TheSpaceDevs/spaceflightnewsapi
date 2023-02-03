from django.urls import include, path
from rest_framework import routers

from api import views

api_router = routers.SimpleRouter()
api_router.register(r"articles", views.ArticleViewSet, basename="articles")
api_router.register(r"blogs", views.BlogViewSet, basename="blogs")
api_router.register(r"reports", views.ReportViewSet, basename="reports")

urlpatterns = [
    path("", include(api_router.urls)),
]
