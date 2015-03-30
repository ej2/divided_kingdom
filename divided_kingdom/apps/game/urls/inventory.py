from django.conf.urls import patterns, url
from divided_kingdom.apps.core.patterns import ID
from divided_kingdom.apps.game.views import inventory


urlpatterns = patterns(
    "",
    url(r"^(?P<item_id>%s)/drop$" % ID, inventory.drop_item, name="drop"),
    url(r"^(?P<item_id>%s)/use$" % ID, inventory.use_item, name="use"),
)