# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-10 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20190310_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='content',
            new_name='comments',
        ),
    ]
