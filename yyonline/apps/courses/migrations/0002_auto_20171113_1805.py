# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-13 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '\u521d\u7ea7\u8bfe\u7a0b'), ('zj', '\u4e2d\u7ea7\u8bfe\u7a0b'), ('gj', '\u9ad8\u7ea7\u8bfe\u7a0b')], max_length=2, verbose_name='\u96be\u5ea6'),
        ),
    ]