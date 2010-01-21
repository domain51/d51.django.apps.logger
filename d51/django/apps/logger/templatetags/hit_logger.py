from django.core.urlresolvers import reverse
from django import template
from ..views import hit

register = template.Library()

class HitLoggerNode(object):
    def __init__(self, url):
        self.url = url

    def render(self, context):
        return reverse(hit, kwargs={"url": self.url})

@register.tag('log_hit')
def do_log_hit(parser, token):
    # TODO: add support for block parameters
    # TODO: add support for variable URLs
    [_tag_name, url] = token.split_contents()
    return HitLoggerNode(url)
