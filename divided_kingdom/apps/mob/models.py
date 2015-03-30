from divided_kingdom.apps.core.models import AuditModel, GENDER
from django.db import models
from divided_kingdom.apps.item.models import DropTable
from divided_kingdom.apps.location.models import Route
from divided_kingdom.apps.player.models import Player


class MobType(AuditModel):
    name = models.CharField(max_length=30)
    is_named = models.BooleanField(default=False)

    xp_amount = models.IntegerField(default=0)
    total_health = models.IntegerField(default=0)
    total_stamina = models.IntegerField(default=0)

    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    will_power = models.IntegerField(default=0)
    perception = models.IntegerField(default=0)
    arcane_power = models.IntegerField(default=0)
    presence = models.IntegerField(default=0)
    manipulation = models.IntegerField(default=0)

    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Mob(AuditModel):
    name = models.CharField(max_length=30)
    mob_type = models.ForeignKey(MobType)

    xp_amount = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField(default=0)

    total_health = models.IntegerField(default=0)
    total_stamina = models.IntegerField(default=0)

    current_health = models.IntegerField(default=0)
    current_stamina = models.IntegerField(default=0)

    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    will_power = models.IntegerField(default=0)
    perception = models.IntegerField(default=0)
    arcane_power = models.IntegerField(default=0)
    presence = models.IntegerField(default=0)
    manipulation = models.IntegerField(default=0)

    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    route = models.ForeignKey(Route)
    drop_table = models.ForeignKey(DropTable)
    player = models.ForeignKey(Player)

    def __unicode__(self):
        return self.name

    def adjust_health(self, amount):
        self.current_health += amount

        if self.current_health < 0:
            self.current_health = 0

        if self.current_health > self.total_health:
            self.current_health = self.total_health

        result = "{0} {1} <span class='health'>{2} health</span>.".format(
            self.name,
            "gains" if amount > 0 else "loses", abs(amount))

        return result

    def adjust_stamina(self, amount):
        self.current_stamina += amount

        if self.current_stamina < 0:
            self.current_stamina = 0

        if self.current_stamina > self.total_stamina:
            self.current_stamina = self.total_stamina

        result = "{0} {1} <span class='stamina'>{2} stamina</span>.".format(
            self.name,
            "gains" if amount > 0 else "loses", abs(amount))

        return result


class Encounter(AuditModel):
    route = models.ForeignKey(Route, unique=True)
    max_rate = models.IntegerField()

    def __unicode__(self):
        return "Encounter on {0}".format(self.route.name)

class MobEncounter(AuditModel):
    mob_type = models.ForeignKey(MobType)
    encounter = models.ForeignKey(Encounter, related_name="mobs")
    encounter_rate = models.IntegerField()  # From 0 to 1000
    drop_table = models.ForeignKey(DropTable)