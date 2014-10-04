import random
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.game.helpers.event import resolve_event, generate_event
from divided_kingdom.apps.game.helpers.helper import get_game_messages, create_game_message
from divided_kingdom.apps.game.helpers.reward import calculate_reward
from divided_kingdom.apps.game.models import EventAction, Reward, EventLog
from divided_kingdom.apps.location.models import Route, Service
from divided_kingdom.apps.npc.helpers.dialog import get_merchant_greeting
from divided_kingdom.apps.npc.helpers.moods import get_random_mood
from divided_kingdom.apps.npc.models import PlayerNPC
from divided_kingdom.apps.player.models import Player


@login_required
def display_service(request, service_id):
    user = request.user
    player = get_object_or_None(Player, user=user)

    if player is None:
        return redirect("player:new")

    service = get_object_or_None(Service, pk=service_id)

    service.npc.mood = get_random_mood()
    service.npc.save()

    context = {
        "user": player.user,
        "player": player,
        "service": service,
        "game_messages": get_game_messages(player),
        "greeting": get_merchant_greeting(service)
    }

    return TemplateResponse(request, "game/service.html", RequestContext(request, context))

def visit_service(request, service_id):
    request.session["service_id"] = service_id

    return redirect("game:display_service")

def insult(request):
    user = request.user
    player = get_object_or_None(Player, user=user)
    service = get_object_or_None(Service, pk=request.session["service_id"])

    player_npc = get_object_or_None(PlayerNPC, player=player, npc=service.npc)

    player_npc.opinion_of_player -1
    player_npc.save()

    result = ""
    create_game_message(player, "You insult {0}. {1}".format(service.npc.name, result))

    return redirect("game:play")