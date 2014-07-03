from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.template.response import TemplateResponse


@login_required
def index(request):
    context = RequestContext(request, {
        "user": request.user
    })

    return TemplateResponse(request, "site/index.html", context)
