from django.contrib.auth.models import User
from divided_kingdom.apps.core.game_settings import STARTING_GOLD, BASE_HEALTH, BASE_STAMINA, STARTING_ACTION_POINTS, \
    STARTING_SKILL_POINTS, BASE_ATTACK, BASE_DEFENSE, BASE_SPEED
from divided_kingdom.apps.core.models import AuditModel
from django.db import models
from divided_kingdom.apps.location.models import Route, Location

GENDER = (
    ("M", "Male",),
    ("F", "Female",),
    ("U", "Unknown",)
)


class MotivatingForce(AuditModel):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Player(AuditModel):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, null=True, blank=True, related_name="players")
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    gold = models.IntegerField(default=STARTING_GOLD)

    action_points = models.IntegerField(default=STARTING_ACTION_POINTS)
    skill_points = models.IntegerField(default=STARTING_SKILL_POINTS)

    total_health = models.IntegerField(default=BASE_HEALTH)
    current_health = models.IntegerField(default=BASE_HEALTH)
    total_stamina = models.IntegerField(default=BASE_STAMINA)
    current_stamina = models.IntegerField(default=BASE_STAMINA)

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

    route = models.ForeignKey(Route, null=True, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    distance_marker = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def adjust_health(self, amount):
        self.current_health += amount

        if self.current_health < 0:
            self.current_health = 0

        if self.current_health > self.total_health:
            self.current_health = self.total_health

        result = "You {0} <span class='health'>{1} health</span>.".format(
            "gain" if amount > 0 else "lose", abs(amount))

        return result

    def adjust_stamina(self, amount):
        self.current_stamina += amount

        if self.current_stamina < 0:
            self.current_stamina = 0

        if self.current_stamina > self.total_stamina:
            self.current_stamina = self.total_stamina

        result = "You {0} <span class='stamina'>{1} stamina</span>.".format(
            "gain" if amount > 0 else "lose", abs(amount))

        return result