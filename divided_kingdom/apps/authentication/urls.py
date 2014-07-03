from django.conf.urls import patterns, url, include
from divided_kingdom.apps.authentication import views

urlpatterns = patterns(
    "",
    url(r"^/login$",
        views.login,
        name="login"),
    url(r"^/logout$",
        views.logout,
        name="logout"),
)
