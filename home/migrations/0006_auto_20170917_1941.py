# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170915_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='end_goal',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='idea',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]