# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-06-19 02:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_post_schematic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='github',
        ),
        migrations.RemoveField(
            model_name='post',
            name='schematic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='soundcloud_embed',
        ),
        migrations.RemoveField(
            model_name='post',
            name='soundcloud_link',
        ),
        migrations.RemoveField(
            model_name='post',
            name='sub_title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
    ]
