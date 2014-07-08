import random
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.game.helpers.event import resolve_event
from divided_kingdom.apps.game.helpers.helper import get_route, get_location
from divided_kingdom.apps.game.models import GameMessage, EventAction, Reward
from divided_kingdom.apps.location.models import Location, Route
from divided_kingdom.apps.player.models import Player


@login_required
def play(request):
    user = request.user
    player = get_object_or_None(Player, user=user)

    if player.route is not None:
        #Player is traveling on route
        return TemplateResponse(request, "game/route.html", RequestContext(request, get_route(player)))
    else:
        #Player is at location
        return TemplateResponse(request, "game/location.html", RequestContext(request, get_location(player)))


def forward(request):
    user = request.user
    player = get_object_or_None(Player, user=user)

    player.distance_marker += 1

    if player.distance_marker >= player.route.distance:
        player.distance_marker = 0
        player.location = player.route.end_location
        player.route = None

    player.save()
    return redirect("game:play")


def backward(request):
    user = request.user
    player = get_object_or_None(Player, user=user)

    player.distance_marker -= 1

    if player.distance_marker <= 0:
        player.distance_marker = 0
        player.location = player.route.start_location
        player.route = None

    player.save()
    return redirect("game:play")


def travel(request, route_id):
    user = request.user
    player = get_object_or_None(Player, user=user)

    player.route = get_object_or_None(Route, pk=route_id)
    player.distance_marker = 0
    player.save()

    return redirect("game:play")


def action(request, action_id):
    user = request.user
    player = get_object_or_None(Player, user=user)

    event_action = get_object_or_None(EventAction, id=action_id)

    i = random.randint(1, 100)

    game_message = GameMessage()
    game_message.player = player

    if i <= event_action.success_chance:
        #SUCCESS!
        #TODO: update this
        reward = get_object_or_None(Reward, action=event_action)

        gold_reward_text = ""
        xp_reward_text = ""

        if reward:
            if reward.min_gold > 0:
                gold_amount = random.randint(reward.min_gold, reward.max_gold)
                gold_reward_text = "<BR>You gain <span class='gold'>{0} gold</span>.".format(gold_amount)
                player.gold += gold_amount

            if reward.XP > 0:
                player.xp += reward.XP
                xp_reward_text = "<BR>You gain <span class='xp'>{0} XP</span>.".format(reward.XP)

            player.save()

        game_message.message = "{0} {1}{2}{3}".format(
            event_action.action_text, event_action.success_text, gold_reward_text, xp_reward_text)

    else:
        #FAILURE!
        game_message.message = "{0} {1}".format(event_action.action_text, event_action.failure_text)

    game_message.save()
    resolve_event(player, event_action.event)

    return redirect("game:play")


def search(request):
    user = request.user
    player = get_object_or_None(Player, user=user)

    random_event = random.randint(1, 8)

    if random_event == 1:
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

        location = random.randint(1,5)

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

    game_message = GameMessage()
    game_message.player = player
    game_message.message = result
    game_message.save()

    return redirect("game:play")