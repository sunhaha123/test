# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-19 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20171118_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y%m', verbose_name='\u5934\u50cf'),
        ),
    ]