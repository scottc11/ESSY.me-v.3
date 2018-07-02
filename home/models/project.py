from django.template.defaultfilters import slugify
from django.conf import settings
from django.db import models
from essy.storage import GoogleCloudStorage
from datetime import datetime
from home.models.technology import Technology
from home.models.social_media import SocialMediaAccount

def format_storage_path(instance, filename):
    project_name = instance.slug
    return 'projects/{0}/media/{1}'.format(project_name, filename)

# put your models here
class Project(models.Model):

    ORDER_WEIGHT_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    slug = models.SlugField(default='', blank=True)
    sub_title = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True, default='')
    thumbnail = models.ImageField(upload_to=format_storage_path, storage=GoogleCloudStorage(), default='')
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    order_weight = models.IntegerField(choices=ORDER_WEIGHT_CHOICES, default=1)
    technologies = models.ManyToManyField(Technology)
    github = models.URLField(max_length=250, blank=True)
    website = models.URLField(max_length=250, blank=True)

    class Meta:
        ordering = ('-order_weight',)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
