from django.contrib.auth.models import User
from divided_kingdom.apps.core.models import AuditModel
from django.db import models


class Location(AuditModel):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name


class Route(AuditModel):
    name = models.CharField(max_length=50)
    start_location = models.ForeignKey(Location, related_name="starting_routes")
    end_location = models.ForeignKey(Location, related_name="ending_routes")
    distance = models.IntegerField()

    def __unicode__(self):
        return self.name