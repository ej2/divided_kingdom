from django.conf.urls import patterns, url
from divided_kingdom.apps.core.patterns import ID
from divided_kingdom.apps.player import views


urlpatterns = patterns(
    "",
    url(r"^/new$", views.create, name="new"),
    url(r"^/(?P<id>%s)$" % ID, views.detail, name="detail"),
)