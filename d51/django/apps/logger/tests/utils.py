from django.core.urlresolvers import reverse
import random

def build_hit_url(url):
    return reverse('d51.django.apps.logger.views.hit', kwargs={"url": url})

def random_url():
    return (
        "http://example.com/bob",
        "http://example.com/alice",
        "http://example.org/chris",
        "http://example.org/travis",
    )[random.randint(0, 3)]


