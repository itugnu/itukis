# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 13:46
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]