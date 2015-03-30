import random
from annoying.functions import get_object_or_None
from divided_kingdom.apps.game.models import GameEvent, GameMessage, EventLog


def get_random_event(player):
    return random.choice(GameEvent.objects.filter(route=player.route))


def generate_event(player):
    event_log = get_object_or_None(EventLog, player=player, resolved=False)
    if event_log:
        game_message = GameMessage()
        game_message.player = player
        game_message.message = event_log.game_event.incident_description
        game_message.save()

        return event_log.game_event
    else:
        game_event = get_random_event(player)
        log_event(player, game_event)

        game_message = GameMessage()
        game_message.player = player
        game_message.message = game_event.incident_description
        game_message.save()

        return game_event


def log_event(player, game_event):
    event_log = EventLog(player=player, game_event=game_event)
    event_log.save()


def resolve_event(player, game_event):
    event_log = get_object_or_None(EventLog, player=player, game_event=game_event, resolved=False)
    event_log.resolved = True
    event_log.save()

    player.status = 'R'
    player.save()
