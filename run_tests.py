try:
    from d51.django.virtualenv.test_runner import run_tests
except ImportError:
    print "Please install d51.django.virtualenv.test_runner to run these tests"

import sys


def setUp():
    from django.conf.urls.defaults import patterns, include, handler500
    sys.modules[setUp.__module__].handler500 = handler500
    sys.modules[setUp.__module__].urlpatterns = patterns('',
        (r'^logger/', include('d51.django.apps.logger.urls')),
    )

def main():
    settings = {
        "INSTALLED_APPS": (
            "d51.django.apps.logger",
        ),
        # Make this the urls.py and include the necessary patterns here
        'ROOT_URLCONF': '__main__',
    }
    run_tests(settings, 'logger')

if __name__ == '__main__':
    main()
