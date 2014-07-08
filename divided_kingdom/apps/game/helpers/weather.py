import random

SEASONS = ("spring", "summer", "fall", "winter")

WEATHER_TYPES = ("sunny", "rainy", "stormy", "foggy", "hot", "cold", "brisk", "clear", "cloudy")

def get_weather():
    return "It is {0} out.".format(random.choice(WEATHER_TYPES))