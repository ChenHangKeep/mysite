# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_comment_is_show'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '留言', 'verbose_name_plural': '留言'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(max_length=20, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='是否展示'),
        ),
    ]
