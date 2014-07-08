from django.contrib import admin
from divided_kingdom.apps.game.models import GameMessage, EventAction, GameEvent, Reward, EventLog
from divided_kingdom.apps.location.models import Route, Location, Service
from divided_kingdom.apps.player.models import Player


class GameMessageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "player", "message")
    search_fields = ("id", "player", "message")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class GameEventModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "route", "event_type")
    search_fields = ("id", "title", "route", "event_type")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class EventActionModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "event", "action_text")
    search_fields = ("id", "title", "event", "action_text")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class RewardModelAdmin(admin.ModelAdmin):
    list_display = ("id", "action", "motivating_force", "XP")
    search_fields = ("id", "action", "motivating_force", "XP")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class EventLogModelAdmin(admin.ModelAdmin):
    list_display = ("id", "player", "game_event", "resolved")
    search_fields = ("id", "player", "game_event", "resolved")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25

admin.site.register(GameMessage, GameMessageModelAdmin)
admin.site.register(GameEvent, GameEventModelAdmin)
admin.site.register(EventAction, EventActionModelAdmin)
admin.site.register(Reward, RewardModelAdmin)
admin.site.register(EventLog, EventLogModelAdmin)