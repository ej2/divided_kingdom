from django.contrib import admin
from divided_kingdom.apps.player.models import Player


class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("id", "name",)
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


admin.site.register(Player, PlayerModelAdmin)