from datetime import datetime
from django.db import models
from django.conf import settings
from essy.storage import GoogleCloudStorage
from blog.models import Entry
from django.dispatch import receiver

def format_storage_path(instance, filename):
    entry_slug = instance.entry.slug
    return 'blog/entries/{0}/{1}'.format(entry_slug, filename)

class EntryImage(models.Model):
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


@receiver(models.signals.post_delete, sender=EntryImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Delete file from cloud storage when EntryImage object is deleted.
    """
    if instance.image.storage.exists(instance.image.name):
        instance.image.storage.delete(instance.image.name)


# NOTE: not working!
@receiver(models.signals.pre_save, sender=EntryImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `EntryImage` object is updated with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = EntryImage.objects.get(pk=instance.pk).image
    except EntryImage.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if instance.image.storage.exists(instance.image.name):
            instance.image.storage.delete(instance.image.name)
