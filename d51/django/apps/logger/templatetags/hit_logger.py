from django.core.urlresolvers import reverse
from django import template
from d51.django.apps.logger.views import hit

register = template.Library()

class HitLoggerNode(template.Node):
    def __init__(self, url, context_name=None):
        self.url = url
        self.context_name = context_name

    def render(self, context):
        if self.url.find(":") == -1:
            # assume we have a variable
            self.url = template.Variable(self.url).resolve(context)
        url = reverse(hit, kwargs={"url": self.url})
        if self.context_name:
            context[self.context_name] = url
        else:
            return url
        return ''

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
