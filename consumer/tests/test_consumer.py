import json

import pytest

from api.models import NewsSite
from consumer.mq_consumer import MqConsumer


@pytest.mark.django_db
class TestConsumer:
    def test_saving_article(self, news_sites: list[NewsSite]) -> None:
        mq_consumer = MqConsumer()

        json_data = '{"type":"article","data":{"title":"TheBigCombo","url":"https://www.youtube.com/watch?v=5g4lY8Y3eoo","imageUrl":"https://i.ytimg.com/vi/5g4lY8Y3eoo/hqdefault.jpg","newsSite":1,"summary":"TheBigComboisa1955AmericanfilmnoircrimefilmdirectedbyJosephH.LewisandphotographedbycinematographerJohnAlton,withmusicbyDavidRaksin.ThefilmstarsCornelWilde,RichardConteandBrianDonlevy,aswellasJeanWallace,whowasWilde\'swifeatthetime.ItalsoincludedthefinalscreenappearanceofactressHelenWalker.TheBigCombowasbasedonastorybyformercrimereporterFrancisM.Cockrell,whosoldhisworktoproducerSidneyHarmonforonly$2,000.Thefilmwascompletedin18days,andwasreleasedonFebruary13,1955byAlliedArtistsPictures.ThefilmhasbeencitedasaprimaryinspirationforFrançoisTruffaut\'s1960filmShootthePianoPlayer.","publishedAt":"2021-02-13T00:00:00.000Z"}}'

        data = json.loads(json_data)

        mq_consumer._save_article(data["data"])
