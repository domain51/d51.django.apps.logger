import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
import random

from ..models import Hit

def build_hit_url(url):
    return reverse('d51.django.apps.logger.views.hit', kwargs={"url": url})

def random_url():
    return (
        "http://example.com/bob",
        "http://example.com/alice",
        "http://example.org/chris",
        "http://example.org/travis",
    )[random.randint(0, 3)]

class TestOfHitView(TestCase):
    def test_logs_hit(self):
        url = random_url()
        c = Client()
        response = c.get(build_hit_url(url))

        hit = Hit.objects.get(url=url)

    def test_stores_current_time(self):
        url = random_url()
        response = Client().get(build_hit_url(url))
        hit = Hit.objects.get(url=url)

        self.assert_(isinstance(hit.created_on, datetime.datetime))
        self.assert_((datetime.datetime.now() - hit.created_on).seconds < 1,
            "Check creation time, might fail on slow machines/network connections.")
