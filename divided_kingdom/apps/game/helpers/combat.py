import random
from annoying.functions import get_object_or_None


def basic_attack(player, mob):
    damage_amount = random.randint(1, 10)
    mob.adjust_health(damage_amount * -1)
    mob.save()

    return "You hit {0} for {1} damage!".format(mob.name, damage_amount)


def basic_mob_attack(player, mob):

    hit_chance = 50

    strike = random.randint(1, 100)

    if strike < hit_chance:
        damage_amount = random.randint(1, 6)

        player.adjust_health(damage_amount * -1)
        player.save()

        return "The {0} hits you for {1}.".format(mob.name, damage_amount)
    else:
        return "The {0} tries to hit you but misses.".format(mob.name)