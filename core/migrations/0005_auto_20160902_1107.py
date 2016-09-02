# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-02 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tvseries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvseries',
            name='download_link',
            field=models.CharField(max_length=30000, null=True, verbose_name='下载链接'),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='tags',
            field=models.CharField(max_length=100, null=True, verbose_name='电视剧类型'),
        ),
    ]
