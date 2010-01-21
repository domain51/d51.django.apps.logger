import datetime
from django.test import TestCase
from django.test.client import Client

from ..models import Hit
from .utils import build_hit_url, random_url

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

    def test_redirects_to_url(self):
        url = random_url()
        response = Client().get(build_hit_url(url))
        self.assertEquals(response.status_code, 302)
        # TODO: refactor this - we can't use assertRedirect() because it
        #       tries to load crap, but this test should be simplified
        self.assertEquals(response._headers['location'][1], url, "ensure redirection took place")
