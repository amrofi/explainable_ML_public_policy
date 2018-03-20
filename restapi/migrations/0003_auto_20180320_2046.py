# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-20 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20180317_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factor',
            name='balanced',
        ),
        migrations.RemoveField(
            model_name='factor',
            name='enabled',
        ),
        migrations.AddField(
            model_name='factor',
            name='is_balanced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='factor',
            name='is_binary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='factor',
            name='is_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='factor',
            name='description',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='mlmodel',
            name='description',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
    ]
