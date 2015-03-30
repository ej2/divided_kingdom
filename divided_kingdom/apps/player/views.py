from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.template import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.core.game_settings import STARTING_LOCATION_ID
from divided_kingdom.apps.game.helpers.helper import get_game_messages
from divided_kingdom.apps.item.models import Item
from divided_kingdom.apps.location.models import Location
from divided_kingdom.apps.player.forms import PlayerForm
from divided_kingdom.apps.player.models import Player


@login_required
def create(request):
    user = request.user

    if request.method == "POST":
        form = PlayerForm(data=request.POST, user=user)

        if form.is_valid():
            player = form.save()
            #messages.success(request, "Your product was created successfully")

            player.location = get_object_or_None(Location, pk=STARTING_LOCATION_ID)
            return redirect(reverse("game:play"))
    else:
        form = PlayerForm(user=user)

    context = RequestContext(request, {
        "form": form,
    })

    return TemplateResponse(request, "player/new.html", context)


@login_required
def detail(request, id):
    player = get_object_or_404(Player, pk=id)

    items = Item.objects.filter(player=player)

    context = RequestContext(request, {
        "player": player,
        "items": items,
        "game_messages": get_game_messages(player),
    })

    return TemplateResponse(request, "player/detail.html", context)


