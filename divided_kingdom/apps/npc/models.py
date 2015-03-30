from divided_kingdom.apps.core.game_settings import BASE_HEALTH, BASE_STAMINA, BASE_ATTACK, BASE_DEFENSE, BASE_SPEED
from divided_kingdom.apps.core.models import AuditModel
from django.db import models
from divided_kingdom.apps.player.models import MotivatingForce, GENDER, Player


class NPC(AuditModel):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField(default=0)

    total_health = models.IntegerField(default=BASE_HEALTH)
    total_stamina = models.IntegerField(default=BASE_STAMINA)

    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    will_power = models.IntegerField(default=0)
    perception = models.IntegerField(default=0)
    arcane_power = models.IntegerField(default=0)
    presence = models.IntegerField(default=0)
    manipulation = models.IntegerField(default=0)

    attack = models.IntegerField(default=BASE_ATTACK)
    defense = models.IntegerField(default=BASE_DEFENSE)
    speed = models.IntegerField(default=BASE_SPEED)

    motivating_force = models.ForeignKey(MotivatingForce, null=True, blank=True)
    personality = models.CharField(max_length=30, null=True, blank=True)

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

    def __unicode__(self):
        return self.name


class PlayerNPC(AuditModel):
    player = models.ForeignKey(Player)
    npc = models.ForeignKey(NPC)
    current_health = models.IntegerField(default=BASE_HEALTH)
    current_stamina = models.IntegerField(default=BASE_STAMINA)
    gold = models.IntegerField(default=0)
    opinion_of_player = models.IntegerField(default=0)
    mood = models.CharField(max_length=20)