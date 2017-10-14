from django.conf import settings
from django.db import models
from essy.storage import GoogleCloudStorage
from datetime import datetime

def format_storage_path(instance, filename):
    date = datetime.isoformat(instance.pub_date).split('T')[0]
    project_slug = instance.project.slug
    return 'projects/{0}/posts/{1}/{2}'.format(project_slug, date, filename)


# Create your models here.
class Post(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250, blank=False)
    sub_title = models.CharField(max_length=500, blank=False)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    soundcloud_embed = models.CharField(max_length=1000, blank=True)
    soundcloud_link = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to=format_storage_path, storage=GoogleCloudStorage(), blank=True)
    schematic = models.ImageField(upload_to=format_storage_path, storage=GoogleCloudStorage(), blank=True)
    thumbnail = models.ImageField(upload_to=format_storage_path, storage=GoogleCloudStorage())
    body = models.TextField()
    github = models.URLField(max_length=250, default='https://github.com/scottc11')

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
