# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-23 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170923_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='soundcloud',
            new_name='soundcloud_embed',
        ),
        migrations.AddField(
            model_name='post',
            name='soundcloud_link',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
