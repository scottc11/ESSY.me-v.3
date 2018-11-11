from datetime import datetime
from django.db import models
from django.conf import settings
from essy.storage import GoogleCloudStorage
from blog.models import Entry

def format_storage_path(instance, filename):
    entry_slug = instance.entry.slug
    return 'blog/entries/{0}/{1}'.format(entry_slug, filename)

class Image(models.Model):
    image = models.ImageField(upload_to=format_storage_path, storage=GoogleCloudStorage(), max_length=300, blank=True)
    entry = models.ForeignKey(Entry, related_name='images', blank=True, null=True)
    description = models.TextField(blank=True, default='')
    thumbnail = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-thumbnail',)

    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]
