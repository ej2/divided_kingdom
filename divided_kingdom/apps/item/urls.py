from django.conf.urls import patterns, url
from divided_kingdom.apps.item import views


urlpatterns = patterns(
    "",
    url(r"^/create$", views.create_random, name="create"),
)