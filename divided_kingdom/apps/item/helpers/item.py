from datetime import datetime
import random
from divided_kingdom.apps.item.models import Item, ItemProperty


def create_item(item_type):
    item = Item.objects.create(
        name=item_type.name,
        description=item_type.description,
        base_type=item_type.base_type,
        classification=item_type.classification,
        uses=item_type.uses,
        strength=item_type.strength,
        dexterity=item_type.dexterity,
        constitution=item_type.constitution,
        intelligence=item_type.intelligence,
        will_power=item_type.will_power,
        perception=item_type.perception,
        arcane_power=item_type.arcane_power,
        presence=item_type.presence,
        manipulation=item_type.manipulation,
        attack=item_type.attack,
        defense=item_type.defense,
        speed=item_type.speed,
        min_damage=item_type.min_damage,
        max_damage=item_type.max_damage,
        date_created=datetime.now()
    )

    for item_property in item_type.properties.all():
        ItemProperty.objects.create(
            item=item,
            modifier_type=item_property.modifier_type,
            stat_modified=item_property.stat_modified,
            amount=item_property.amount
        )

    return item


def get_random_drop(drop_table):
    drop = random.randint(1, drop_table.max_rate)

    item_drops = drop_table.items.filter(drop_rate__gt=drop)

    if item_drops.count() > 0:
        return random.choice(item_drops)
    else:
        return None