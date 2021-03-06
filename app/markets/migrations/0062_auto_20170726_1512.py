# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-26 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0061_auto_20170510_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='logo',
            name='cropping',
            field=image_cropping.fields.ImageRatioField(
                'image', '400x302', adapt_rotation=False, allow_fullsize=False,
                hide_image_field=False, size_warning=False, verbose_name='cropping',
                free_crop=False, help_text='Use cropping tool to cut the image to the right format. Always leave\
                enough white space around the edges and try to keep the largest possible size for good image quality.',
            ),
        ),
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(
                null=True, upload_to='',
                help_text="After choosing an image to upload click 'Save' to access the 'Cropping' tool and edit the\
                image"),
        ),
        migrations.AddField(
            model_name='market',
            name='language',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                to='markets.Language', verbose_name='Language of Marketplace'),
        ),
        migrations.AddField(
            model_name='publishedmarket',
            name='language',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                to='markets.Language', verbose_name='Language of Marketplace'),
        ),
    ]
