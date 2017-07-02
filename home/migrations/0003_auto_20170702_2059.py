# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_snippet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.AddField(
            model_name='project',
            name='sub_title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
