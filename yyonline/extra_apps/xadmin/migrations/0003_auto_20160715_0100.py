# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xadmin', '0002_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='action_flag',
            field=models.CharField(max_length=32, verbose_name='action flag'),
        ),
    ]
