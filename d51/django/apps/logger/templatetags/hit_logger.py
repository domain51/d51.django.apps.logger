from django.core.urlresolvers import reverse
from django import template
from d51.django.apps.logger.views import hit
import urllib

register = template.Library()

class HitLoggerNode(template.Node):
    def __init__(self, url, context_name=None, hit_view=hit):
        self.url = url
        self.context_name = context_name
        self.hit_view  = hit_view
        self.view_kwargs = {}

    def render(self, context):
        if self.url.find(":") == -1:
            # assume we have a variable
            self.url = template.Variable(self.url).resolve(context)
        if not 'url' in self.view_kwargs:
            self.view_kwargs['url'] = urllib.urlencode({'': self.url})[1:]
        url = reverse(self.hit_view, kwargs=self.view_kwargs)

        if self.context_name:
            context[self.context_name] = url
            return ''
        else:
            return url

@register.tag('log_hit')
def do_log_hit(parser, token):
    # TODO: add support for block parameters
    # TODO: add support for variable URLs
    tokens = token.split_contents()
    url = None
    context_name = None
    if len(tokens) == 2:
        [_tag_name, url] = tokens
    else:
        [_tag_name, url, _as, context_name] = tokens
    return HitLoggerNode(url, context_name)
