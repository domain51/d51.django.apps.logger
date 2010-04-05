from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

class Hit(models.Model):
    url = models.URLField(verify_exists=False)
    created_on = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    related_to = generic.GenericForeignKey('content_type', 'object_id')

