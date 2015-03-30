import random
from divided_kingdom.apps.core.models import GENDER
from divided_kingdom.apps.game.models import GameMessage
from divided_kingdom.apps.mob.models import Mob, Encounter


def random_encounter(player):
    encounter = Encounter.objects.get(route=player.route)
    enc = random.randint(1, encounter.max_rate)

    mob_encounters = encounter.mobs.filter(encounter_rate__gt=enc)

    if mob_encounters.count() > 0:
        mob_encounter = random.choice(mob_encounters)
        mob = create_mob(mob_encounter.mob_type)
        mob.drop_table = mob_encounter.drop_table
        mob.player = player
        mob.route = player.route
        mob.save()

        game_message = GameMessage()
        game_message.player = player
        game_message.message = "You are attacked by a {0}!".format(mob.name)
        game_message.save()

        return mob
    else:
        return None


def create_mob(mob_type):
    mob = Mob()

    if mob_type.is_named:
        pass  #  TODO: Random Name generation

    mob.name = mob_type.name
    mob.xp_amount = mob_type.xp_amount
    mob.total_stamina = mob_type.total_stamina
    mob.total_health = mob_type.total_health

    mob.current_health = mob.total_health
    mob.current_stamina = mob.total_stamina

    mob.strength = mob_type.strength
    mob.dexterity = mob_type.dexterity
    mob.constitution = mob_type.constitution
    mob.intelligence = mob_type.intelligence
    mob.will_power = mob_type.will_power
    mob.perception = mob_type.perception
    mob.arcane_power = mob_type.arcane_power
    mob.presence = mob_type.presence
    mob.manipulation = mob_type.manipulation
    mob.attack = mob_type.attack
    mob.defense = mob_type.defense
    mob.speed = mob_type.speed

    mob.mob_type = mob_type

    mob.gender = random.choice(GENDER)
    #mob.age

    return mob
