# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0003_interactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactive',
            name='template',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
