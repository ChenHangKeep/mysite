# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-07 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='is_show',
        ),
    ]
