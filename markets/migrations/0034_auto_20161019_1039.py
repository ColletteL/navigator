# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-19 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0033_auto_20161018_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='membership_fees_frequency',
            field=models.CharField(blank=True, max_length=1, null=True,
                                   choices=[
                                       ('D', 'daily'),
                                       ('W', 'weekly'),
                                       ('M', 'monthly'),
                                       ('Q', 'quarterly'),
                                       ('Y', 'annually')]),
        ),
        migrations.AlterField(
            model_name='market',
            name='seller_support_hours',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]