from django.contrib import admin
from divided_kingdom.apps.npc.models import NPC, PlayerNPC


class NPCModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", )
    search_fields = ("id", "name", "age")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class PlayerNPCModelAdmin(admin.ModelAdmin):
    list_display = ("id", "npc", "player", )
    search_fields = ("id", "npc", "player")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


admin.site.register(NPC, NPCModelAdmin)
admin.site.register(PlayerNPC, PlayerNPCModelAdmin)