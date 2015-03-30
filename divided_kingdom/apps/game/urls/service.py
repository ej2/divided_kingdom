from django.conf.urls import patterns, url

from divided_kingdom.apps.core.patterns import ID
from divided_kingdom.apps.game.views import service


urlpatterns = patterns(
    "",
    url(r"^(?P<service_id>%s)/visit_service$" % ID, service.visit_service, name="visit_service"),
    url(r"^(?P<service_id>%s)/display_service$" % ID, service.display_service, name="display_service"),
    url(r"^(?P<service_item_id>%s)/purchase$" % ID, service.purchase, name="purchase"),
    url(r"^(?P<service_item_id>%s)/inquire" % ID, service.inquire, name="inquire"),
)