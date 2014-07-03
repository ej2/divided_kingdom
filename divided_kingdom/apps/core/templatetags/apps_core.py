import locale
from decimal import Decimal
from django import template
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.forms.widgets import CheckboxInput, RadioSelect, CheckboxSelectMultiple, TextInput
from django.template.loader import render_to_string


register = template.Library()


@register.simple_tag(takes_context=True)
def messages(context, *args, **kwargs):
    return render_to_string("core/messages.html", context_instance=context)



@register.simple_tag(takes_context=True)
def errors(context, *args, **kwargs):
    form = args[0]

    if form.is_bound and not form.is_valid():
        field = kwargs.get("field")

        if field:
            errors = form[field].errors
            as_alert = False

        else:
            errors = form.non_field_errors()
            as_alert = True

        if errors:
            return render_to_string("core/errors.html", {
                "errors": errors,
                "as_alert": as_alert}, context)

    return ""


@register.simple_tag(takes_context=True)
def formfield(context, *args, **kwargs):
    field = args[0]

    template = "core/form_field.html"

    if isinstance(field.field.widget, CheckboxInput):
        template = "core/form_field_checkbox.html"

    if isinstance(field.field.widget, RadioSelect):
        template = "core/form_field_radio.html"

    return render_to_string(template, {
        "field": field,
        "hide": kwargs.get("hide", False),
        "show_required": kwargs.get("show_required", False)}, context)



@register.simple_tag(takes_context=True)
def urlfor(context, urlname, *args, **kwargs):
    return reverse(urlname, args=args, kwargs=kwargs)


@register.filter
def currency(value, arg="", symbol=True):
    existing_locale = locale.getlocale()
    provided_locale = arg and ("." in arg and str(arg) or str(arg) + ".UTF-8")

    if existing_locale == (None, None,):
        existing_locale = settings.DEFAULT_LOCALE
    else:
        existing_locale = ".".join(existing_locale)

    # Workaround for Python bug 1699853
    if "." in existing_locale and existing_locale.split(".")[1].lower() in ("utf", "utf8"):
        existing_locale = existing_locale.split(".")[0] + ".UTF-8"

    if isinstance(value, (str, unicode,)):
        if value:
            value = Decimal(value)
        else:
            value = 0.0

    try:
        locale.setlocale(locale.LC_ALL, provided_locale or existing_locale)

        return locale.currency(value or 0, symbol, True)

    except (TypeError, locale.Error):
        return ""

    finally:
        locale.setlocale(locale.LC_ALL, existing_locale)


@register.filter()
def startswith(value, arg=""):
    return str(value).startswith(arg)


@register.filter()
def convbool(value):
    if isinstance(value, bool):
        return "Yes" if value else "No"

    return ""


@register.filter()
def strip(value):
    return str(value).strip()
