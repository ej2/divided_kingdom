from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.player.models import Player


@login_required
def index(request):
    user = request.user
    player = get_object_or_None(Player, user=user)

    context = RequestContext(request, {
        "user": request.user,
        "player": player
    })

    return TemplateResponse(request, "site/index.html", context)
