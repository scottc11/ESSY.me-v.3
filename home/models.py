from django.db import models


# Create your models here.


class Project(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    sub_title = models.CharField(max_length=200, blank=True, default='')
    body = models.CharField(max_length=1000, blank=True, default='')
