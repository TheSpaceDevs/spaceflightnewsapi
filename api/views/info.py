from typing import List

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import NewsSite
from api.serializers import NewsSiteSerializer


class InfoView(APIView):
    def get_news_sites(self) -> List[str]:
        news_sites = NewsSite.objects.all()
        sites = [NewsSiteSerializer(site).data["name"] for site in news_sites]

        return sites

    def get(self, _request):
        sites = self.get_news_sites()
        return Response({"version": settings.VERSION, "news_sites": sites})
