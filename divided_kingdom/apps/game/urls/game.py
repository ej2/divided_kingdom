from django.conf.urls import patterns, url, include
from divided_kingdom.apps.core.patterns import ID
from divided_kingdom.apps.game.views import game, service


urlpatterns = patterns(
    "",
    url(r"^play$", game.play, name="play"),

    url(r"^forward$", game.forward, name="forward"),
    url(r"^backward$", game.backward, name="backward"),
    url(r"^search$", game.search, name="search"),
    url(r"^attack$", game.attack, name="attack"),
    url(r"^rest$", game.rest, name="rest"),
    url(r"^(?P<route_id>%s)/travel$" % ID, game.travel, name="travel"),
    url(r"^(?P<action_id>%s)/action$" % ID, game.action, name="action"),

    url(r"^/service", include("divided_kingdom.apps.game.urls.service", namespace="service")),
    url(r"^/inventory", include("divided_kingdom.apps.game.urls.inventory", namespace="inventory")),
)