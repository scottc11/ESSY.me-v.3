# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170917_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
