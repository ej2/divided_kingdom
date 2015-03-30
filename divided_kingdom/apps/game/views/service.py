from annoying.functions import get_object_or_None

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.response import TemplateResponse

from divided_kingdom.apps.game.helpers.helper import get_game_messages, create_game_message

from divided_kingdom.apps.item.helpers.item import create_item
from divided_kingdom.apps.location.models import Service, ServiceItemType
from divided_kingdom.apps.npc.helpers.dialog import get_merchant_greeting
from divided_kingdom.apps.npc.helpers.moods import update_merchant_mood
from divided_kingdom.apps.npc.models import PlayerNPC
from divided_kingdom.apps.player.decorators import player_required
from divided_kingdom.apps.player.models import Player


@login_required
@player_required
def display_service(request, player, service_id):
    service = get_object_or_None(Service, pk=service_id)


    context = {
        "user": player.user,
        "player": player,
        "service": service,
        "game_messages": get_game_messages(player),

    }

    return TemplateResponse(request, "game/service.html", RequestContext(request, context))


@login_required
@player_required
def visit_service(request, player, service_id):
    service = get_object_or_None(Service, pk=service_id)
    player_npc = get_object_or_None(PlayerNPC, player=player, npc=service.npc)

    if player_npc is None:
        player_npc = PlayerNPC(player=player, npc=service.npc)
        player_npc.save()
        update_merchant_mood(player_npc)

    if player_npc.mood == 'Infuriated':
        greeting = 'The merchant yells at you "GET OUT OF MY SHOP!"'
    else:
        greeting = 'The {0} merchant says "{1}"'.format(player_npc.mood.lower(), get_merchant_greeting(service))

    create_game_message(player, greeting)

    return redirect("game:service:display_service", service_id)


@login_required
@player_required
def purchase(request, player, service_item_id):
    service_item = get_object_or_None(ServiceItemType, pk=service_item_id)
    player_npc = get_object_or_None(PlayerNPC, player=player, npc=service_item.service.npc)

    if player.gold >= service_item.price:
        item = create_item(service_item.item_type)
        item.player = player
        item.save()

        player.gold -= service_item.price
        player.save()

        result = "You purchase the {0} for <span class='gold'>{1} gold</span>.".format(item.name, service_item.price)
        player_npc.opinion_of_player += 1
    else:
        result = 'The {0} merchant says "You don''t have enough gold to buy that."'.format(player_npc.mood.lower())
        player_npc.opinion_of_player -= 1

    update_merchant_mood(player_npc)

    create_game_message(player, result)

    return redirect("game:service:display_service", service_item.service.pk)


@login_required
@player_required
def inquire(request, player, service_item_id):
    service_item = get_object_or_None(ServiceItemType, pk=service_item_id)
    player_npc = get_object_or_None(PlayerNPC, player=player, npc=service_item.service.npc)

    result = 'The merchant says "It is a {0}".'.format(service_item.item_type.description)
    update_merchant_mood(player_npc)

    create_game_message(player, result)

    return redirect("game:service:display_service", service_item.service.pk)


@login_required
@player_required
def insult(request):
    user = request.user
    player = get_object_or_None(Player, user=user)
    service = get_object_or_None(Service, pk=request.session["service_id"])

    player_npc = get_object_or_None(PlayerNPC, player=player, npc=service.npc)

    player_npc.opinion_of_player -= 1
    player_npc.save()

    result = ""
    create_game_message(player, "You insult {0}. {1}".format(service.npc.name, result))

    return redirect("game:play")