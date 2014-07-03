from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template.context import RequestContext
from django.template.response import TemplateResponse
from divided_kingdom.apps.authentication.forms import LoginForm


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            next = request.GET.get("next") or "/"
            return redirect(next)

    else:
        form = LoginForm()

    context = RequestContext(request, {
        "form": form})

    return TemplateResponse(request, "authentication/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect(request.GET.get("next") or reverse("authentication:login"))