# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-05 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0057_auto_20170228_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='market',
            options={'permissions': (('can_publish', 'Can publish Market'), ('can_unpublish', 'Can unpublish Market'))},
        ),
    ]
