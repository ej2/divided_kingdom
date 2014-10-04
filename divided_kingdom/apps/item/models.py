from divided_kingdom.apps.core.models import AuditModel
from django.db import models
from divided_kingdom.apps.player.models import Player


BASE_TYPE = (
    ("WEA", "Weapon",),
    ("ARM", "Armor",),
    ("CON", "Consumable",),
    ("QST", "Quest",),
)

CLASSIFICATION = (
    ("BLADE", "Blade",),
    ("BLUNT", "Blunt",),
    ("AXE", "Axe",),
    ("BOW", "Bow",),
    ("STAFF", "Staff",),
    ("SPEAR", "Spear",),
    ("SHIELD", "Shield",),
    ("CHEST", "Chest",),
    ("GLOVE", "Gloves",),
    ("BOOTS", "Boots",),
    ("LEGS", "Leggings",),
    ("HEAD", "Head",),
    ("FOOD", "Food",),
    ("POTION", "Potion",),
    ("JEWLRY", "Jewelry",),
    ("MOUNT", "Mount",),
    ("MAT", "Material",),
    ("DRINK", "Drink",),
)

MODIFIER = (
    ("ADD", "Add",),
    ("SUB", "Subtract",),
    ("MUL", "Multiply",),
    ("DIV", "Divide",),
)

STAT = (
    ("STR", "strength",),
    ("DEX", "dexterity",),
    ("CON", "constitution",),
    ("INT", "intelligence",),
    ("WIL", "will_power",),
    ("PER", "perception",),
    ("ARC", "arcane_power",),
    ("PRE", "presence",),
    ("MAN", "manipulation",),
    ("ATT", "attack",),
    ("DEF", "defense",),
    ("SPD", "speed",),
    ("HP", "total_health",),
    ("ST", "total_stamina",),
)


class ItemType(AuditModel):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    base_type = models.CharField(max_length=3, choices=BASE_TYPE)
    classification = models.CharField(max_length=6, choices=CLASSIFICATION)
    uses = models.IntegerField(default=0)

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

    min_damage = models.IntegerField(default=0)
    max_damage = models.IntegerField(default=0)


    def __unicode__(self):
        return self.name


class ItemTypeProperty(AuditModel):
    item_type = models.ForeignKey(ItemType, related_name="properties")
    modifier_type = models.CharField(max_length=3, choices=MODIFIER)
    stat_modified = models.CharField(max_length=3, choices=STAT)
    amount = models.IntegerField()

    class Meta:
        verbose_name_plural = "Item Type Properties"

    def __unicode__(self):
        return "{0} {1}{2}".format(self.stat_modified, self.modifier_type, self.amount)


class Item(AuditModel):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    base_type = models.CharField(max_length=3, choices=BASE_TYPE)
    classification = models.CharField(max_length=6, choices=CLASSIFICATION)
    uses = models.IntegerField(default=0)
    player = models.ForeignKey(Player, null=True, blank=True)

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

    min_damage = models.IntegerField(default=0)
    max_damage = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class ItemProperty(AuditModel):
    item = models.ForeignKey(Item, related_name="properties")
    modifier_type = models.CharField(max_length=3, choices=MODIFIER)
    stat_modified = models.CharField(max_length=3, choices=STAT)
    amount = models.IntegerField()

    class Meta:
        verbose_name_plural = "Item Properties"

    def __unicode__(self):
        return "{0} {1}{2}".format(self.stat_modified, self.modifier_type, self.amount)


class DropTable(AuditModel):
    name = models.CharField(max_length=30)
    max_rate = models.IntegerField(default=100)

    def __unicode__(self):
        return self.name


class ItemDrop(AuditModel):
    drop_table = models.ForeignKey(DropTable, related_name="items")
    item_type = models.ForeignKey(ItemType, related_name="+")
    drop_rate = models.IntegerField() #From 0 to 1000