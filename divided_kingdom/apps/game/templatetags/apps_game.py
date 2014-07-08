from __future__ import division
from django import template
from django.template.loader import render_to_string
from divided_kingdom.settings import STATIC_URL


register = template.Library()


@register.simple_tag()
def indicator_bar(title, bar_width, current_value, max_value, color):
    filled_amount = ((current_value / max_value) * bar_width)

    return render_to_string("game/indicator_bar.html", {
        "title": title,
        "current_value": current_value,
        "bar_width": bar_width,
        "max_value": max_value,
        "filled_amount": filled_amount,
        "color": color,
        "STATIC_URL": STATIC_URL
        })
