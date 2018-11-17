# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-10 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('home', '0021_auto_20180702_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.Entry'),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='order_weight',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]