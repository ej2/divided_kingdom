from annoying.functions import get_object_or_None
from divided_kingdom.apps.game.helpers.event import get_random_event, generate_event, resolve_event
from divided_kingdom.apps.game.helpers.weather import get_weather
from divided_kingdom.apps.game.models import GameMessage, EventLog


def get_route(player):

    route = player.route

    remaining_miles = route.distance - player.distance_marker

    event_log = get_object_or_None(EventLog, player=player, resolved=False)
    if event_log is None:
        event = generate_event(player)
    else:
        event = event_log.game_event

    context = {
        "user": player.user,
        "player": player,
        "route": route,
        "remaining_miles": remaining_miles,
        "weather": get_weather(),
        "event": event,
        "game_messages": get_game_messages(player),
    }

    return context


def get_location(player):
    location = player.location

    context = {
        "user": player.user,
        "player": player,
        "location": location,
        "messages": get_game_messages(player)
    }

    return context


def get_game_messages(player):
    messages = GameMessage.objects.filter(player=player, shown=False).order_by("date_created")

    for message in messages:
        message.shown = True
        message.save()

    return messages