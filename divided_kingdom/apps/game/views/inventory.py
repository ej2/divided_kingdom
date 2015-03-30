from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from divided_kingdom.apps.game.helpers.helper import create_game_message
from divided_kingdom.apps.item.helpers.consumable import consume
from divided_kingdom.apps.item.models import Item
from divided_kingdom.apps.player.decorators import player_required


@login_required
@player_required
def use_item(request, player, item_id):
    item = get_object_or_None(Item, pk=item_id)
    result = consume(item, player)

    message = "You use the {0}. {1}".format(item.name, result)
    create_game_message(player, message)

    return redirect("player:detail", player.pk)


@login_required
@player_required
def drop_item(request, player, item_id):
    item = get_object_or_None(Item, pk=item_id)
    message = "You drop the {0}.".format(item.name)

    item.delete()
    create_game_message(player, message)

    return redirect("player:detail", player.pk)