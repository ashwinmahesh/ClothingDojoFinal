# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-19 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_dojo', '0023_auto_20180719_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
    ]