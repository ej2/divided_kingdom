from django.contrib import admin
from divided_kingdom.apps.location.models import Route, Location, Service, ServiceItemType
from divided_kingdom.apps.player.models import Player


class RouteModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "distance", "start_location", "end_location")
    search_fields = ("id", "name", "distance")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class LocationModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    search_fields = ("id", "name", "type")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "service_type", "location", "hidden")
    search_fields = ("id", "name", "type")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class ServiceItemTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "service", "item_type", "price")
    search_fields = ("id", "service__name", "item_type__name", "price")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25

admin.site.register(Location, LocationModelAdmin)
admin.site.register(Route, RouteModelAdmin)
admin.site.register(Service, ServiceModelAdmin)
admin.site.register(ServiceItemType, ServiceItemTypeAdmin)