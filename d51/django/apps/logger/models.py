from django.db import models

class Hit(models.Model):
    url = models.URLField()
