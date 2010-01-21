from django.http import HttpResponse

from .models import Hit

def hit(request, url):
    hit = Hit.objects.create(url=url)
    return HttpResponse()
