from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import NewsSite
from api.serializers import InfoSerializer


class InfoView(APIView):
    serializer_class = InfoSerializer
    authentication_classes = []

    def _get_news_sites(self) -> list[str]:
        news_sites = NewsSite.objects.all().order_by("name")
        sites = [site.name for site in news_sites]

        return sites

    def get(self, _request: Request) -> Response:
        sites = self._get_news_sites()
        return Response({"version": settings.VERSION, "news_sites": sites})
