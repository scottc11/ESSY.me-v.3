from django.template.defaultfilters import slugify
from django.conf import settings
from django.db import models
from essy.storage import GoogleCloudStorage
from datetime import datetime

# only here for old migrations. Been moved to image.py model
def format_storage_path(instance, filename):
    date = datetime.isoformat(instance.pub_date).split('T')[0]
    project_slug = instance.project.slug
    return 'projects/{0}/posts/{1}/{2}'.format(project_slug, date, filename)


# Create your models here.
class Post(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(default='', blank=True)
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    body = models.TextField(blank=True)
    youtube_video = models.URLField(blank=True)
    codepen = models.URLField(blank=True)
    codeblock = models.TextField(blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
