from divided_kingdom.apps.core.models import AuditModel
from django.db import models


SERVICE_TYPE = (
    ("M", "Merchant",),
    ("S", "Stable",),
    ("I", "Inn",),
    ("H", "Healing",)
)


#City, town, outpost, farm, etc
class Location(AuditModel):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name


#path between two locations
class Route(AuditModel):
    name = models.CharField(max_length=50)
    start_location = models.ForeignKey(Location, related_name="starting_routes")
    end_location = models.ForeignKey(Location, related_name="ending_routes")
    distance = models.IntegerField()
    combat_chance = models.IntegerField(default=0)  # how likely combat will happen on route
    event_chance = models.IntegerField(default=0)   # how likely events will happen on route

    def __unicode__(self):
        return self.name


#merchant, inn, stable, etc
class Service(AuditModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    service_type = models.CharField(max_length=1, choices=SERVICE_TYPE)
    location = models.ForeignKey(Location, related_name="services")
    hidden = models.BooleanField(default=False)
    npc = models.ForeignKey("npc.NPC", null=True, blank=True)

    def __unicode__(self):
        return "{0} in {1}".format(self.name, self.location.name)


#items for sale at service location
class ServiceItemType(AuditModel):
    service = models.ForeignKey(Service, related_name="items")
    item_type = models.ForeignKey("item.ItemType")
    price = models.IntegerField()