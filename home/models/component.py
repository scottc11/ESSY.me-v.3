from django.conf import settings
from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=50, blank=False)
    type = models.CharField(max_length=50, blank=False)
    wiki = models.URLField(max_length=500, blank=True)
    datasheet = models.URLField(max_length=500, blank=True)
    purchase_link = models.URLField(max_length=500, blank=True)
