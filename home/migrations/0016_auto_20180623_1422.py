# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-06-23 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import essy.storage
import home.models.image


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20180619_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=300, storage=essy.storage.GoogleCloudStorage(), upload_to=home.models.image.format_storage_path)),
                ('description', models.TextField(blank=True, default=b'')),
                ('thumbnail', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-thumbnail',),
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='media_accounts',
        ),
        migrations.AddField(
            model_name='post',
            name='codeblock',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='codepen',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='youtube_video',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.Post'),
        ),
    ]
