from django.contrib import admin
from divided_kingdom.apps.mob.models import Mob, MobType, MobEncounter, Encounter


class MobModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "current_health", "player", "gender", "age")
    search_fields = ("id", "name", "gender", "age")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class MobTypeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    search_fields = ("id", "name",)
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class EncounterModelAdmin(admin.ModelAdmin):
    list_display = ("id", "route", "max_rate")
    search_fields = ("id", "route",)
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class MobEncounterModelAdmin(admin.ModelAdmin):
    list_display = ("id", "mob_type", "encounter", "encounter_rate")
    search_fields = ("id", "mob_type", "encounter", "encounter_rate")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25




admin.site.register(MobType, MobTypeModelAdmin)
admin.site.register(Mob, MobModelAdmin)
admin.site.register(Encounter, EncounterModelAdmin)
admin.site.register(MobEncounter, MobEncounterModelAdmin)