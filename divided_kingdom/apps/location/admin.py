from django.contrib import admin
from divided_kingdom.apps.location.models import Route, Location
from divided_kingdom.apps.player.models import Player


class RouteModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "distance")
    search_fields = ("id", "name", "distance")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class LocationModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    search_fields = ("id", "name", "type")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


admin.site.register(Location, LocationModelAdmin)
admin.site.register(Route, RouteModelAdmin)