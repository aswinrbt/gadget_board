# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20160614_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_admin',
        ),
    ]
