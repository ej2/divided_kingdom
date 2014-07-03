from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'divided_kingdom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^authentication", include("divided_kingdom.apps.authentication.urls", namespace="authentication")),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r"^site/", include("divided_kingdom.apps.site.urls", namespace="site")),
    url(r"^player", include("divided_kingdom.apps.player.urls", namespace="player")),
)

