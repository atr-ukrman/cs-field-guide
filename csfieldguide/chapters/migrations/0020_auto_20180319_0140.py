# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-19 01:40
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0019_merge_20180316_0511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chaptersection',
            old_name='heading',
            new_name='name',
        ),
        migrations.AddField(
            model_name='chapter',
            name='introduction_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=[], size=None),
        ),
        migrations.AddField(
            model_name='chapter',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='chaptersection',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='chaptersection',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=[], size=None),
        ),
        migrations.AddField(
            model_name='chaptersection',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='glossaryterm',
            name='definition_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='glossaryterm',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=[], size=None),
        ),
        migrations.AddField(
            model_name='glossaryterm',
            name='term_en',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='chaptersection',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter_sections', to='chapters.Chapter'),
        ),
    ]
