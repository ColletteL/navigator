# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-19 22:06
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0007_new_countries_remove_regions'),
        ('products', '0009_auto_20161103_1038'),
        ('markets', '0048_auto_20161104_1149'),
        ('reversion', '0001_squashed_0004_auto_20160611_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishedMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(verbose_name='e-Marketplace Description')),
                ('web_address', models.URLField()),
                ('signup_address', models.URLField(blank=True, null=True, verbose_name='Explore the marketplace')),
                ('web_traffic', models.FloatField(blank=True, default=0, help_text='in millions', null=True,
                                                  verbose_name='Number of registered users')),
                ('customer_support_hours', models.CharField(blank=True, max_length=150, null=True)),
                ('seller_support_hours', models.CharField(blank=True, max_length=150, null=True)),
                ('customer_demographics', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('marketing_merchandising', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('product_details_upload_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                  verbose_name='Notes')),
                ('payment_terms_days', models.IntegerField(blank=True, help_text='in days', null=True,
                                                           verbose_name='Payment terms - sale to payment duration')),
                ('logistics_structure_notes', models.CharField(blank=True, max_length=200, null=True,
                                                               verbose_name='notes')),
                ('commission_lower', models.FloatField(blank=True, null=True)),
                ('commission_upper', models.FloatField(blank=True, null=True)),
                ('commission_notes', models.CharField(blank=True, max_length=255, null=True)),
                ('ukti_terms',
                    ckeditor.fields.RichTextField(blank=True, null=True,
                                                  verbose_name='Department of International Trade special terms')),
                ('local_bank_account_needed', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],
                                                                  default=False,
                                                                  verbose_name='A local bank account')),
                ('local_bank_account_needed_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                     verbose_name='Notes')),
                ('local_incorporation_needed', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],
                                                                   default=False, verbose_name='A local company')),
                ('local_incorporation_needed_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                      verbose_name='Notes')),
                ('exclusivity_required', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False,
                                                             verbose_name='Product exclusivity required')),
                ('exclusivity_required_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                verbose_name='Notes')),
                ('translation_verbal', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False,
                                                           verbose_name='To negotiate with the marketplace')),
                ('translation_verbal_notes', models.CharField(blank=True, max_length=255, null=True,
                                                              verbose_name='Notes')),
                ('translation_application_process', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],
                                                                        default=False,
                                                                        verbose_name='To apply to join')),
                ('translation_application_process_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                           verbose_name='Notes')),
                ('translation_product_content', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],
                                                                    default=False,
                                                                    verbose_name='For product content')),
                ('translation_product_content_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                       verbose_name='Notes')),
                ('translation_seller_support', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],
                                                                   default=False, verbose_name='For seller support')),
                ('translation_seller_support_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                      verbose_name='Notes')),
                ('payment_terms_rate_fixed', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],
                                                                 default=False,
                                                                 verbose_name='Payment Terms - Exchange rate fixed')),
                ('payment_terms_rate_fixed_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                    verbose_name='Notes')),
                ('registration_fees', models.FloatField(default=0, verbose_name='One off registration fee')),
                ('registration_fees_notes', models.CharField(blank=True, max_length=255, null=True,
                                                             verbose_name='Notes')),
                ('fee_per_listing', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False,
                                                        verbose_name='Fee per Listing')),
                ('fee_per_listing_notes', models.CharField(blank=True, max_length=255, null=True,
                                                           verbose_name='Notes')),
                ('membership_fees', models.FloatField(default=0, verbose_name='Membership fees')),
                ('membership_fees_frequency', models.CharField(blank=True,
                                                               choices=[
                                                                ('D', 'daily'),
                                                                ('W', 'weekly'),
                                                                ('M', 'monthly'),
                                                                ('Q', 'quarterly'),
                                                                ('Y', 'annually')],
                                                               max_length=1, null=True)),
                ('deposit', models.FloatField(default=0)),
                ('deposit_notes', models.CharField(blank=True, max_length=255, null=True, verbose_name='Notes')),
                ('shipping_tracking_required', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],
                                                                   default=False,
                                                                   verbose_name='Shipping Tracking Required')),
                ('shipping_tracking_required_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                      verbose_name='Notes')),
                ('local_return_address_required',
                    models.BooleanField(choices=[(True, 'Yes'), (False, 'No')],
                                        default=False,
                                        verbose_name='A local address to handle returns?')),
                ('local_return_address_required_notes', models.CharField(blank=True, max_length=255, null=True,
                                                                         verbose_name='Notes')),
                ('dit_advisor_tip', models.TextField(blank=True, null=True,
                                                     verbose_name='Department of International Trade advisor tip')),
                ('countries_served', models.ManyToManyField(blank=True, to='geography.Country',
                                                            verbose_name='Operating Countries')),
                ('currency_of_payments', models.ManyToManyField(blank=True, to='markets.Currency',
                                                                verbose_name='Payment terms - Currency of payments')),
                ('customer_support_channels',
                    models.ManyToManyField(blank=True,
                                           related_name='markets_publishedmarket_customer_related',
                                           to='markets.SupportChannel')),
                ('deposit_currency', models.ForeignKey(blank=True, null=True,
                                                       on_delete=django.db.models.deletion.CASCADE,
                                                       related_name='markets_publishedmarket_deposit_currency',
                                                       to='markets.Currency')),
                ('famous_brands_on_marketplace', models.ManyToManyField(blank=True, to='markets.Brand')),
                ('logistics_structure', models.ManyToManyField(blank=True, to='markets.LogisticsModel')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                           to='markets.Logo')),
                ('membership_fees_currency',
                    models.ForeignKey(blank=True, null=True,
                                      on_delete=django.db.models.deletion.CASCADE,
                                      related_name='markets_publishedmarket_membership_fees_currency',
                                      to='markets.Currency')),
                ('product_categories', models.ManyToManyField(blank=True, to='products.Category')),
                ('product_details_upload', models.ManyToManyField(blank=True, to='markets.UploadMethod',
                                                                  verbose_name='Upload product details via')),
                ('product_type', models.ManyToManyField(blank=True, to='products.Type',
                                                        verbose_name='Product Positioning')),
                ('prohibited_items', models.ManyToManyField(blank=True, to='products.ProhibitedItem')),
                ('registration_fees_currency',
                    models.ForeignKey(blank=True, null=True,
                                      on_delete=django.db.models.deletion.CASCADE,
                                      related_name='markets_publishedmarket_registration_fees_currency',
                                      to='markets.Currency')),
                ('seller_model', models.ManyToManyField(blank=True, to='markets.SellerModel')),
                ('seller_support_channels',
                    models.ManyToManyField(blank=True,
                                           related_name='markets_publishedmarket_seller_related',
                                           to='markets.SupportChannel')),
            ],
            options={
                'abstract': False,
                'ordering': ('-name',),
            },
        ),
        migrations.DeleteModel(
            name='MarketForSignOff',
        ),
        migrations.AlterModelOptions(
            name='market',
            options={'permissions': (('can_publish', 'Can publish Market'),)},
        ),
        migrations.AddField(
            model_name='market',
            name='live_version',
            field=models.IntegerField(null=True),
        ),
    ]
