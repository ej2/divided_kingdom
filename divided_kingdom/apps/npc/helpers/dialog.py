import random
from divided_kingdom.apps.npc.helpers.greetings import GENERIC_GREETINGS, MERCHANT_GREETINGS


def get_generic_greeting():
    return random.choice(GENERIC_GREETINGS)


def get_merchant_greeting(service):
    return str(random.choice(MERCHANT_GREETINGS)).format(service.name)


