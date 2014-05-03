from django.contrib.auth.models import User
from divided_kingdom.apps.core.models import AuditModel
from django.db import models

GENDER = (
    ("M", "Male",),
    ("F", "Female",)
)


class Player(AuditModel):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, null=True, blank=True, related_name="+")
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField()
    xp = models.IntegerField()

    total_health = models.IntegerField()
    current_health = models.IntegerField()
    total_stamina = models.IntegerField()
    current_stamina = models.IntegerField()

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    will_power = models.IntegerField()
    perception = models.IntegerField()
    arcane_power = models.IntegerField()
    presence = models.IntegerField()
    manipulation = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()

    def __unicode__(self):
        return self.name