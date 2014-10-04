from django import template
from django.template.loader import render_to_string
from divided_kingdom.apps.player.models import Player
from annoying.functions import get_object_or_None
from divided_kingdom.settings import STATIC_URL


register = template.Library()


@register.simple_tag()
def player_info(user):
    player = get_object_or_None(Player, user=user)

    if player:
        return render_to_string("player/header_info.html", {
            "user": user,
            "player": player,
            "STATIC_URL": STATIC_URL
            })
    else:
        return ""