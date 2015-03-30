import random


def consume(item, target):
    item.uses -= 1

    for item_prop in item.properties.all():

        amount = random.randint(item_prop.min_amount, item_prop.max_amount)
        if item_prop.modifier_type == "ADD":
            result = "You gain {0} to {1}.".format(amount, item_prop.stat_modified)
            target.adjust_stat(item_prop.stat_modified, amount)
        elif item_prop.modifier_type == "SUB":
            result = "You gain {0} to {1}.".format(amount, item_prop.stat_modified)
            target.adjust_stat(item_prop.stat_modified, -amount)

    if item.uses == 0:
        item.delete()

    target.save()

    return result
