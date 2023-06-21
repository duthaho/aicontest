from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from coding.services.util import get_random_string


@login_required
def index(request):
    template = loader.get_template("coding/index.html")
    avatar = (
        f"https://www.gravatar.com/avatar/{get_random_string(32)}?s=32&d=identicon&r=PG"
    )
    return HttpResponse(template.render(dict(avatar=avatar), request))
