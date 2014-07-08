from django.conf.urls import patterns, url
from divided_kingdom.apps.core.patterns import ID
from divided_kingdom.apps.game.views import game


urlpatterns = patterns(
    "",
    url(r"^play$", game.play, name="play"),
    url(r"^forward$", game.forward, name="forward"),
    url(r"^backward$", game.backward, name="backward"),
    url(r"^search$", game.search, name="search"),
    url(r"^(?P<route_id>%s)/travel$" % ID, game.travel, name="travel"),
    url(r"^(?P<action_id>%s)/action$" % ID, game.action, name="action"),
)