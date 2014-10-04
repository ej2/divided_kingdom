from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.item.helpers.item import get_random_drop, create_item
from divided_kingdom.apps.item.models import DropTable
from divided_kingdom.apps.player.models import Player


@login_required
def create_random(request):
    user = request.user

    drop_table = DropTable.objects.get(pk=1)
    item_drop = get_random_drop(drop_table)
    item = create_item(item_drop.item_type)

    player = get_object_or_None(Player, user=user)
    item.player = player
    item.save()

    context = RequestContext(request, {
        "user": user,
        "item": item
    })

    return TemplateResponse(request, "item/detail.html", context)
