from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'd51.django.apps.logger.views',
    url(r'^hit/(?P<url>.*)$', 'hit', name = 'logger_hit'),
)


