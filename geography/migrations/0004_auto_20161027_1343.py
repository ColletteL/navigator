# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0003_auto_20161027_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
