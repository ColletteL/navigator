# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-10 07:48
from __future__ import unicode_literals

from django.db import migrations, models
from image_cropping import fields


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0060_remove_logo__encoded_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='cropping',
            field=fields.ImageRatioField('image', '400x302', adapt_rotation=False, allow_fullsize=False,
                                         free_crop=False, help_text='Use cropping tool to cut the image to the right\
                                         format. Always leave enough white space around the edges and try to keep the\
                                         largest possible size for good image quality.', hide_image_field=False,
                                         size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(help_text="After choosing an image to upload click 'Save' to access the 'Cropping'\
                                    tool and edit the image", null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='market',
            name='customer_support_hours',
            field=models.CharField(blank=True, help_text='Format: <br/>9:00am to 6:00pm (GMT+1), Monday - Friday',
                                   max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='seller_support_hours',
            field=models.CharField(blank=True, help_text='Format: <br/>9:00am to 6:00pm (GMT+1), Monday - Friday',
                                   max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='publishedmarket',
            name='customer_support_hours',
            field=models.CharField(blank=True, help_text='Format: <br/>9:00am to 6:00pm (GMT+1), Monday - Friday',
                                   max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='publishedmarket',
            name='seller_support_hours',
            field=models.CharField(blank=True, help_text='Format: <br/>9:00am to 6:00pm (GMT+1), Monday - Friday',
                                   max_length=150, null=True),
        ),
    ]
