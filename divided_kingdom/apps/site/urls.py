from django.conf.urls import patterns, url
from divided_kingdom.apps.site import views


urlpatterns = patterns(
    "",
    url(r"^$", views.index, name="index"),

)
