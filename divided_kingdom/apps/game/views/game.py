import random
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.game.helpers.combat import basic_attack, basic_mob_attack
from divided_kingdom.apps.game.helpers.event import resolve_event, generate_event
from divided_kingdom.apps.game.helpers.helper import get_game_messages, create_game_message
from divided_kingdom.apps.game.helpers.reward import calculate_reward, combat_reward
from divided_kingdom.apps.game.models import EventAction, Reward, EventLog
from divided_kingdom.apps.location.models import Route, Service, Location
from divided_kingdom.apps.mob.helpers.encounter import random_encounter
from divided_kingdom.apps.mob.models import Mob
from divided_kingdom.apps.npc.helpers.dialog import get_merchant_greeting
from divided_kingdom.apps.npc.helpers.moods import get_random_mood
from divided_kingdom.apps.player.models import Player


@login_required
def play(request):
    user = request.user
    player = get_object_or_None(Player, user=user)

    if player is None:
        return redirect("player:new")

    context = {
        "user": player.user,
        "player": player,
    }

    if player.status == 'C': #Combat
        mob = get_object_or_None(Mob, player=player, current_health__gt=0)

        template = "game/combat.html"
        context["mob"] = mob

    elif player.status == 'E': #Event
        event_log = get_object_or_None(EventLog, player=player, resolved=False)
        #Player is in an Event
        template = "game/event.html"
        context["event"] = event_log.game_event

    elif player.status == 'L': #Location
        template = "game/location.html"
        context["location"] = player.location

    elif player.status == 'R': #Route
        #Player is traveling on route
        template = "game/route.html"
        context["route"] = player.route
        context["remaining_miles"] = player.route.distance - player.distance_marker

        event_chance = random.randint(1, 100)

        if event_chance < player.route.event_chance:
            combat_chance = random.randint(1, 100)

            if combat_chance < player.route.combat_chance:
                mob = random_encounter(player)
                player.status = 'C'
                player.save()

                template = "game/combat.html"
                context["mob"] = mob

            else:
                event = generate_event(player)
                player.status = 'E'
                player.save()

                template = "game/event.html"
                context["event"] = event


    context["game_messages"] = get_game_messages(player)
    return TemplateResponse(request, template, RequestContext(request, context))

    #----------------
    #event_log = get_object_or_None(EventLog, player=player, resolved=False)

    #if event_log:
        #Player is in an Event
    #    template = "game/event.html"
    #    context["event"] = event_log.game_event

    #elif mob:
    #    template = "game/combat.html"
    #    context["mob"] = mob

    #elif player.route is not None:
        #Player is traveling on route
    #    template = "game/route.html"
    #    context["route"] = player.route
    #    context["remaining_miles"] = player.route.distance - player.distance_marker

    #    event_chance = random.randint(1, 100)

    #    if event_chance < player.route.event_chance:
    #        combat_chance = random.randint(1, 100)

    #        if combat_chance < player.route.combat_chance:
    #            mob = random_encounter(player)
    #            template = "game/combat.html"
    #            context["mob"] = mob

    #        else:
    #            event = generate_event(player)
    #            template = "game/event.html"
    #            context["event"] = event
    #else:
    #    #Player is at location
    #    if player.location is None:
    #        player.location = Location.objects.get(pk=1)
    #        player.save()

    #    template = "game/location.html"
    #    context["location"] = player.location

    #context["game_messages"] = get_game_messages(player)
    #return TemplateResponse(request, template, RequestContext(request, context))


def forward(request):
    user = request.user
    player = get_object_or_None(Player, user=user)
    player.status = 'R'
    player.distance_marker += 1

    if player.distance_marker >= player.route.distance:
        player.distance_marker = 0
        player.location = player.route.end_location
        player.route = None
        player.status = "L"

    player.save()
    return redirect("game:play")


def backward(request):
    user = request.user
    player = get_object_or_None(Player, user=user)
    player.status = 'R'
    player.distance_marker -= 1

    if player.distance_marker <= 0:
        player.distance_marker = 0
        player.location = player.route.start_location
        player.route = None
        player.status = "L"

    player.save()
    return redirect("game:play")


def travel(request, route_id):
    user = request.user
    player = get_object_or_None(Player, user=user)

    player.route = get_object_or_None(Route, pk=route_id)
    player.distance_marker = 0
    player.status = 'R'
    player.save()

    return redirect("game:play")


def action(request, action_id):
    user = request.user
    player = get_object_or_None(Player, user=user)

    event_action = get_object_or_None(EventAction, id=action_id)

    i = random.randint(1, 100)

    if i <= event_action.success_chance:
        #SUCCESS!
        reward_message = calculate_reward(player, event_action, True)

        create_game_message(player, "{0} {1}{2}".format(
            event_action.action_text, event_action.success_text, reward_message))

    else:
        #FAILURE!
        reward_message = calculate_reward(player, event_action, False)
        create_game_message(player, "{0} {1}{2}".format(
            event_action.action_text, event_action.failure_text, reward_message))

    resolve_event(player, event_action.event)
    return redirect("game:play")


def search(request):
    user = request.user
    player = get_object_or_None(Player, user=user)

    random_event = random.randint(1, 8)

    if random_event < 6:
        result = "You look around and find nothing of interest."

    elif random_event == 6:
        player.distance_marker += 2
        player.save()

        result = "You find a shortcut through the woods that gets you a little closer to {0}.".format(
            player.route.end_location.name)

    elif random_event == 7:
        player.distance_marker -= 2
        player.save()

        result = "You get lost in the woods and find yourself a little further from {0}.".format(
            player.route.end_location.name)

    elif random_event == 8:
        coins = random.randint(2, 8)
        player.gold += coins
        player.save()

        location = random.randint(1, 5)

        if location == 1:
            result = "You find {0} gold coins in the bushes.".format(coins)
        elif location == 2:
            result = "You find {0} gold coins in the dust.".format(coins)
        elif location == 3:
            result = "You find {0} gold coins in the tall grass.".format(coins)
        elif location == 4:
            result = "You find {0} gold coins under a rock.".format(coins)
        elif location == 5:
            result = "You find {0} gold coins in the weeds.".format(coins)

    create_game_message(player, result)
    return redirect("game:play")


def rest(request):
    user = request.user
    player = get_object_or_None(Player, user=user)

    stamina_gained = random.randint(5, 10)
    health_gained = random.randint(1, 3)

    stamina_message = player.adjust_stamina(stamina_gained)
    health_message = player.adjust_health(health_gained)

    result = "You rest for a few minutes. <BR>{0}<BR>{1}".format(health_message, stamina_message)

    create_game_message(player, result)
    return redirect("game:play")


def attack(request):
    user = request.user
    player = get_object_or_None(Player, user=user)
    mob = get_object_or_None(Mob, player=player, current_health__gt=0)

    result = basic_attack(player, mob)
    create_game_message(player, result)

    if mob:
        if mob.current_health <= 0:
            result = "The {0} dies.".format(mob.name)
            create_game_message(player, result)

            result = combat_reward(player, mob)
            create_game_message(player, result)

            player.status = "R"
            player.save()
        else:
            result = basic_mob_attack(player, mob)
            create_game_message(player, result)

    return redirect("game:play")
