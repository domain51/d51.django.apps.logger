from django.test import TestCase
from django import template

from ..templatetags.hit_logger import HitLoggerNode
from .utils import build_hit_url, random_url

class TestOfHitLoggerNode(TestCase):
    def test_returns_a_parsed_url(self):
        url = random_url()
        node = HitLoggerNode(url)
        self.assertEqual(build_hit_url(url), node.render(template.Context()))

