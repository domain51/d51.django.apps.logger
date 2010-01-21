from django.http import HttpResponseRedirect

from .models import Hit

def hit(request, url):
    hit = Hit.objects.create(url=url)
    return HttpResponseRedirect(url)
