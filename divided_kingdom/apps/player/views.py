from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.template import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.player.forms import PlayerForm
from divided_kingdom.apps.player.models import Player


@login_required
def create(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            player = form.save()
            #messages.success(request, "Your product was created successfully")

            return redirect(reverse("player:detail", args=(player.pk,)))
    else:
        form = PlayerForm()

    context = RequestContext(request, {
        "form": form,
    })

    return TemplateResponse(request, "player/new.html", context)


@login_required
def detail(request, id):
    player = get_object_or_404(Player, pk=id)

    context = RequestContext(request, {
        "player": player,
    })

    return TemplateResponse(request, "player/detail.html", context)
