from django.conf import settings
from django.db import models
from datetime import datetime


class Technology(models.Model):
    name = models.CharField(max_length=30, blank=False)
    link = models.URLField(max_length=250, blank=True)

    def __str__(self):
        return self.name
