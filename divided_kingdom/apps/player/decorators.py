from functools import wraps
from annoying.functions import get_object_or_None
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from divided_kingdom.apps.player.models import Player


def player_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        player = get_object_or_None(Player, user=user)

        if player is None:
            return redirect("player:new")
        else:
            return func(request, player, *args, **kwargs)

        return HttpResponseForbidden()

    return wrapper


