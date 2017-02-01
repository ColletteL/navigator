from __future__ import unicode_literals
import base64
import datetime
import json
import reversion

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.numberformat import format
from django.core import serializers
from django.contrib.contenttypes.models import ContentType

from reversion.models import Version
from ckeditor.fields import RichTextField

from . import PAYMENT_FREQUENCIES, BOOL_CHOICES
from geography.models import Country
from products.models import Type, Category, ProhibitedItem


class LogisticsModel(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('name',)


class Logo(models.Model):
    name = models.CharField(max_length=200)
    _encoded_data = models.TextField()

    def base64_logo(self):
        return self._encoded_data

    def __str__(self):
        return "{0}".format(self.name)


class SellerModel(models.Model):
    name = models.CharField(max_length=200, unique=True,)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('name',)


class SupportChannel(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('name',)


class UploadMethod(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('name',)


class Currency(models.Model):
    code = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "{0}".format(self.code)

    class Meta:
        verbose_name_plural = "Currencies"
        ordering = ('code',)


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('name',)


class TranslationRequirement(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ordering = models.IntegerField()

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('ordering',)


class SetupRequirement(models.Model):
    name = models.CharField(max_length=200, unique=True)
    ordering = models.IntegerField()

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('ordering',)


class BaseMarket(models.Model):

    class Meta:
        abstract = True
        ordering = ('-name',)

    last_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    logo = models.ForeignKey('Logo', null=True, blank=True)
    description = RichTextField(verbose_name="e-Marketplace Description")
    web_address = models.URLField(max_length=200)
    signup_address = models.URLField(max_length=200, null=True, blank=True, verbose_name="Explore the marketplace")

    countries_served = models.ManyToManyField(Country, verbose_name="Operating Countries", blank=True)
    product_categories = models.ManyToManyField(Category, blank=True)

    web_traffic = models.FloatField(default=0, null=True, blank=True, help_text="in millions",
                                    verbose_name="Number of registered users")
    famous_brands_on_marketplace = models.ManyToManyField(Brand, blank=True)
    seller_model = models.ManyToManyField(SellerModel, blank=True)

    customer_support_channels = models.ManyToManyField(SupportChannel, blank=True,
                                                       related_name="%(app_label)s_%(class)s_customer_related")
    customer_support_hours = models.CharField(max_length=150, blank=True, null=True)

    seller_support_channels = models.ManyToManyField(SupportChannel, blank=True,
                                                     related_name="%(app_label)s_%(class)s_seller_related")
    seller_support_hours = models.CharField(max_length=150, null=True, blank=True)

    customer_demographics = RichTextField(null=True, blank=True)

    marketing_merchandising = RichTextField(null=True, blank=True)

    product_details_upload = models.ManyToManyField(UploadMethod, blank=True,
                                                    verbose_name="Upload product details via")
    product_details_upload_notes = models.TextField(null=True, blank=True, verbose_name="Notes")

    payment_terms_days = models.IntegerField(null=True, blank=True, help_text="in days",
                                             verbose_name="Payment terms - sale to payment duration")

    currency_of_payments = models.ManyToManyField(Currency, blank=True,
                                                  verbose_name="Payment terms - Currency of payments")

    logistics_structure = models.ManyToManyField(LogisticsModel, blank=True)
    logistics_structure_notes = models.TextField(blank=True, null=True, verbose_name='notes')

    product_type = models.ManyToManyField(Type, blank=True, verbose_name="Product Positioning")
    prohibited_items = models.ManyToManyField(ProhibitedItem, blank=True)

    commission_lower = models.FloatField(null=True, blank=True)
    commission_upper = models.FloatField(null=True, blank=True)
    commission_notes = models.TextField(null=True, blank=True)

    ukti_terms = RichTextField(null=True, blank=True, verbose_name="Department of International Trade special terms")

    exclusivity_required = models.BooleanField(choices=BOOL_CHOICES, default=False,
                                               verbose_name="Product exclusivity required")
    exclusivity_required_notes = models.TextField(null=True, blank=True, verbose_name="Notes")

    translation_requirements = models.ManyToManyField(TranslationRequirement, blank=True)
    translation_notes = models.TextField(null=True, blank=True, verbose_name="Notes")

    setup_requirements = models.ManyToManyField(SetupRequirement, blank=True)
    setup_notes = models.TextField(null=True, blank=True, verbose_name="Notes")

    payment_terms_rate_fixed = models.BooleanField(choices=BOOL_CHOICES, default=False,
                                                   verbose_name="Payment Terms - Exchange rate fixed")
    payment_terms_rate_fixed_notes = models.TextField(null=True, blank=True, verbose_name="Notes")

    registration_fees = models.FloatField(default=0, verbose_name="One off registration fee")
    registration_fees_notes = models.TextField(null=True, blank=True, verbose_name="Notes")
    registration_fees_currency = models.ForeignKey(Currency, null=True, blank=True,
                                                   related_name="%(app_label)s_%(class)s_registration_fees_currency")

    fee_per_listing = models.BooleanField(choices=BOOL_CHOICES, default=False,
                                          verbose_name="Fee per Listing")
    fee_per_listing_notes = models.TextField(null=True, blank=True, verbose_name="Notes")

    membership_fees = models.FloatField(default=0, verbose_name="Membership fees")
    membership_fees_frequency = models.CharField(choices=PAYMENT_FREQUENCIES, max_length=1, null=True, blank=True)
    membership_fees_currency = models.ForeignKey(Currency, null=True, blank=True,
                                                 related_name="%(app_label)s_%(class)s_membership_fees_currency")

    deposit = models.FloatField(default=0)
    deposit_currency = models.ForeignKey(Currency, null=True, blank=True,
                                         related_name="%(app_label)s_%(class)s_deposit_currency")
    deposit_notes = models.TextField(null=True, blank=True, verbose_name="Notes")

    shipping_tracking_required = models.BooleanField(choices=BOOL_CHOICES, default=False,
                                                     verbose_name="Shipping Tracking Required")
    shipping_tracking_required_notes = models.TextField(null=True, blank=True, verbose_name="Notes")

    dit_advisor_tip = RichTextField(null=True, blank=True,
                                    verbose_name="Department of International Trade advisor tip")

    def save(self, *args, **kwargs):
        """
        Populate the slug based on the marketplace's name on save
        """

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        """
        Do some manual error checking for the Market, in particular, that if a amount of money has been specified
        (e.g. for deposit, or membership_fees), then the currency must also be specified.
        """

        errors = {}

        if self.deposit > 0 and self.deposit_currency is None:
            errors['deposit_currency'] = 'You must specify the currency if you specify an amount'
        if self.membership_fees > 0 and self.membership_fees_currency is None:
            errors['membership_fees_currency'] = 'You must specify the currency if you specify an amount'
        if self.membership_fees > 0 and self.membership_fees_frequency is None:
            errors['membership_fees_frequency'] = 'You must specify the frequency if you specify an amount'
        if self.registration_fees > 0 and self.registration_fees_currency is None:
            errors['registration_fees_currency'] = 'You must specify the currency if you specify an amount'

        try:
            super().clean(*args, **kwargs)
        except ValidationError as super_errors:
            errors.update(super_errors)

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return "{0}".format(self.name)

    @property
    def commission_display(self):
        if self.commission_lower is None and self.commission_upper is None:
            return "None"

        values = [self.commission_lower, self.commission_upper]
        lower = min(val for val in values if val is not None)
        upper = max(val for val in values if val is not None)

        if lower == upper:
            commission = "{0}%".format(lower)
        else:
            commission = "{0} - {1}%".format(lower, upper)

        return commission

    @property
    def membership_fees_display(self):
        display_value = self._value_display('membership_fees')
        if display_value != "None":
            return "{0} {1}".format(display_value, self.get_membership_fees_frequency_display())
        else:
            return display_value

    @property
    def deposit_display(self):
        return self._value_display('deposit')

    @property
    def registration_fees_display(self):
        return self._value_display('registration_fees')

    @property
    def web_traffic_display(self):
        if self.web_traffic != 0:
            return "{0} million".format(self.web_traffic)

        return "Not available"

    def _value_display(self, attr):
        value = getattr(self, attr, 0)
        if value > 0:
            formatted_value = format(value, '.', decimal_pos=2, grouping=3, thousand_sep=',', force_grouping=True)
            currency = getattr(self, "{0}_currency".format(attr)).code
            display_str = "{0} {1}".format(currency, formatted_value)
        else:
            display_str = "None"

        return display_str

    @property
    def payment_terms_days_display(self):
        if self.payment_terms_days:
            if self.payment_terms_days == 1:
                return "1 day"
            else:
                return "{0} days".format(self.payment_terms_days)
        else:
            return ""


class Market(BaseMarket):

    class Meta:
        permissions = (
            ("can_publish", "Can publish Market"),
        )

    live_version = models.IntegerField(null=True)

    approval_fields = [
        'logo',
        'countries_served',
        'product_categories',
        'web_traffic',
        'customer_support_channels',
        'customer_support_hours',
        'seller_support_channels',
        'seller_support_hours',
        'customer_demographics',
        'marketing_merchandising',
        'product_details_upload',
        'payment_terms_days',
        'currency_of_payments',
        'logistics_structure',
        'product_type',
        'ukti_terms',
        'dit_advisor_tip',
        'seller_model',
        'signup_address',
        'famous_brands_on_marketplace',
    ]

    def validate_for_publishing(self):
        errors = []

        for field_name in self.approval_fields:
            field = getattr(self, field_name, None)
            verbose_name = self._meta.get_field(field_name).verbose_name
            if getattr(field, 'all', False):
                value = field.all()
                if len(value) == 0:
                    msg = '{0} must be filled in for publishing'.format(verbose_name)
                    errors.append(msg)
            else:
                value = field
                if value is None or value == '':
                    msg = '{0} must be filled in for publishing'.format(verbose_name)
                    errors.append(msg)
        if errors:
            raise ValidationError(errors)

    def publish(self, user=None):
        """
        Publish the Market.  Check that all the approval_fields are completed, then create a PublishedMarket copy of
        the Market, by serialising and deserialiseing it as a PublishedMarket object.  Create a revision for it, and
        mark that revision as it being published.
        """

        with reversion.create_revision():
            # Just save the model to trigger the new revision
            self.save()

            # Store the meta-information to say that the model has been published
            reversion.set_user(user)
            reversion.set_comment("Published")

        # Get the latest revision id that was just completed
        latest_version = Version.objects.get_for_object(self)[0]
        # Save it to the model
        self.live_version = latest_version.revision_id
        self.save()

        # Get the model data from the Version
        data = latest_version.serialized_data
        model_data = json.loads(data)

        # Change it's content type to PublishedMarket
        content_type = ContentType.objects.get_for_model(PublishedMarket)
        model_name = "{0}.{1}".format(content_type.app_label, content_type.model)
        model_data[0]['model'] = model_name
        # Pop the live_version (which isn't on the PublisheMarket model)
        model_data[0]['fields'].pop('live_version')

        # Then deserialise and save the PublishedMarket object
        published_market = next(serializers.deserialize("json", json.dumps(model_data)))
        published_market.save()

    def unpublish(self, user=None):
        """
        Unpublish the market, deleting the associated PublishedMarket model, and setting the live_version to None
        """

        if not self.published:
            raise ValidationError("Market is not published, so cannot unpublish.")

        # Delet the associated PublishedMarket
        PublishedMarket.objects.get(pk=self.pk).delete()

        with reversion.create_revision():
            # Make null the live_version and save
            self.live_version = None
            self.save()

            # Store the meta-information to say that the model has been unpublished
            reversion.set_user(user)
            reversion.set_comment("Unpublished")

    def delete(self):
        """
        Override standard delete behaviour to ensure we delete the associated PublishedMarket, if indeed there is one
        """

        if self.published:
            published_market = PublishedMarket.objects.get(pk=self.pk)
            pub_count, pub_objects = published_market.delete()
            count, objects = super().delete()
            for model, updated in pub_objects.items():
                if model in objects:
                    objects[model] += updated
                else:
                    objects[model] = updated

            return (count + pub_count, objects)
        else:
            return super().delete()

    @property
    def published(self):
        """
        Property the returns true/false based on whether a matching PublishedMarket exists in the database
        """

        try:
            PublishedMarket.objects.get(pk=self.pk)
            return True
        except PublishedMarket.DoesNotExist:
            return False

    def is_published(self):
        """
        For use as a column in the list_display of the ModelAdmin
        """
        return self.published

    is_published.boolean = True


class PublishedMarket(BaseMarket):
    pass
