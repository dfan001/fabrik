# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0003_auto_20170222_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothing',
            name='img_location',
        ),
    ]
