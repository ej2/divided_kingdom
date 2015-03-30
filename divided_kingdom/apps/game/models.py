from django.db import models
from divided_kingdom.apps.core.models import AuditModel
from divided_kingdom.apps.item.models import ItemType
from divided_kingdom.apps.location.models import Route
from divided_kingdom.apps.player.models import Player, MotivatingForce


EVENT_TYPE = (
    ("A", "Assault",), #Innocent attacked, mugging, creature attack, battle between foes
    ("E", "Escort",), #prisoner escort, VIP escort
    ("I", "Injured",), #Innocent, enemy, animal, etc injured or trapped
    ("L", "Lost Party",), #Innocent, enemy, etc lost their way
    ("M", "Missing Object",), #request to help find object, request to find ingredient
    ("W", "Wandering Encounter",), #run into enemy, merchant, animal, etc
    ("U", "Unknown Object",), #discover object, structure, body, etc
)


class GameMessage(AuditModel):
    player = models.ForeignKey(Player)
    message = models.TextField()
    shown = models.BooleanField(default=False)

    def __unicode__(self):
        return self.message


class GameEvent(AuditModel):
    title = models.CharField(max_length=50)
    route = models.ForeignKey(Route)
    event_type = models.CharField(max_length="10", choices=EVENT_TYPE)
    incident_description = models.TextField()

    def __unicode__(self):
        return self.title


class EventAction(AuditModel):
    event = models.ForeignKey(GameEvent, related_name="actions")
    title = models.CharField(max_length=50)
    action_text = models.TextField()
    success_chance = models.IntegerField(default=0)
    success_text = models.TextField(null=True)
    failure_text = models.TextField(null=True)

    def __unicode__(self):
        return "{0}:{1}".format(self.event.title, self.title)


class Reward(AuditModel):
    action = models.ForeignKey(EventAction, related_name="rewards")
    motivating_force = models.ForeignKey(MotivatingForce, related_name="+")
    min_gold = models.IntegerField(default=0)
    max_gold = models.IntegerField(default=0)
    XP = models.IntegerField(default=0)
    success = models.BooleanField(default=True)
    health = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
    item_type = models.ForeignKey(ItemType, null=True, blank=True)


class EventLog(AuditModel):
    player = models.ForeignKey(Player, related_name="+")
    game_event = models.ForeignKey(GameEvent, related_name="+")
    resolved = models.BooleanField(default=False)
