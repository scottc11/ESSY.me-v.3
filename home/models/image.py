from datetime import datetime
from django.db import models
from django.conf import settings
from essy.storage import GoogleCloudStorage
from .post import Post


def format_storage_path(instance, filename):
    post_slug = instance.post.slug
    project_slug = instance.post.project.slug
    return 'projects/{0}/posts/{1}/{2}'.format(project_slug, post_slug, filename)

class Image(models.Model):
    image = models.ImageField(upload_to=format_storage_path, storage=GoogleCloudStorage(), max_length=300, blank=True)
    post = models.ForeignKey(Post, related_name='images', blank=True, null=True)
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
