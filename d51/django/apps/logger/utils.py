
HIT_RELATED_TO = 'd51.django.apps.logger.HIT_MODEL'

def add_object_to_session(request, obj):
    request.session[HIT_RELATED_TO] = obj
