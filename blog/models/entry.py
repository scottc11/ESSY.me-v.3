from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Entry(models.Model):
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250, blank=False)
    sub_title = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(default='', blank=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
