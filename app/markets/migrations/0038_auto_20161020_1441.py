# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-20 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0037_delete_sellermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='customer_support_hours',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]