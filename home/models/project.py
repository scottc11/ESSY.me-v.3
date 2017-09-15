from django.conf import settings
from django.db import models
from essy.storage import GoogleCloudStorage
from datetime import datetime


def format_storage_path(instance, filename):
    project_name = instance.title.replace(' ', '_')
    return 'projects/{0}/{1}'.format(project_name, filename)

# put your models here
class Project(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    sub_title = models.CharField(max_length=200, blank=True, default='')
    thumbnail = models.ImageField(upload_to=format_storage_path, storage=GoogleCloudStorage(), default='')
    body = models.CharField(max_length=1000, blank=True, default='')
    github = models.URLField(max_length=250, default='https://github.com/scottc11')

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
