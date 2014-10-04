from annoying.functions import get_object_or_None
from divided_kingdom.apps.game.helpers.event import get_random_event, generate_event, resolve_event
from divided_kingdom.apps.game.helpers.weather import get_weather
from divided_kingdom.apps.game.models import GameMessage, EventLog


def get_game_messages(player):
    messages = GameMessage.objects.filter(player=player, shown=False).order_by("date_created")

    for message in messages:
        message.shown = True
        message.save()

    return messages


def create_game_message(player, message):
    game_message = GameMessage()
    game_message.player = player
    game_message.message = message
    game_message.save()

