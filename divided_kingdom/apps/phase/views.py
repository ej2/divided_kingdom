from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.player.models import Player


def index(request):

    context = RequestContext(request, {
    })

    return TemplateResponse(request, "phase/index.html", context)


def game(request):

    context = RequestContext(request, {
    })

    return TemplateResponse(request, "phase/game.html", context)
