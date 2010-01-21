from django.db import models

class Hit(models.Model):
    url = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)
