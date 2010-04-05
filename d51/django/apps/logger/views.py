from django.http import HttpResponseRedirect

from .models import Hit
from .utils import HIT_RELATED_TO

def hit(request, url):
    hit = Hit(url=url)
    if HIT_RELATED_TO in request.session:
        related_to = request.session[HIT_RELATED_TO]
        del request.session[HIT_RELATED_TO]
        hit.related_to = related_to
    hit.save()
    return HttpResponseRedirect(url)
