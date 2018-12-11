# -*- coding: utf-8 -*-
# Departments?
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django_countries.fields import CountryField
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from konnote import regular_expressions
from tags.models import CustomerTag, StaffTag


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+254722722722'. Up to 15 digits allowed.")
    postal_code_regex = RegexValidator(regex=r'^\d{5,6}$',
                                       message="Postal Code must be entered in the format: '00100'. "
                                               "Up to 6 digits allowed.")
    alphabet_only_regex = RegexValidator(regex=r'^[a-zA-Z]*$',
                                         message="Use Alphabet characters only. No numericals.")
    website_url = models.TextField(default='', blank=True, null=True)
    email = models.EmailField(max_length=100, default='', blank=True)
    physical_address = models.CharField(max_length=100, default='', blank=True, null=True)
    postal_code = models.CharField(validators=[regular_expressions.postal_code_regex], default='', blank=True,
                                   max_length=6)
    mobile = models.CharField(validators=[regular_expressions.phone_regex], max_length=17, blank=True)
    telephone = models.CharField(validators=[regular_expressions.phone_regex], max_length=17, blank=True)
    postal_address = models.CharField(validators=[regular_expressions.postal_code_regex], default='', blank=True,
                                      max_length=6)
    country = CountryField(default='', blank=True, null=True)
    county = models.CharField(max_length=settings.CHAR_MAX_LENGTH, default='Nairobi')
    bio = models.TextField(max_length=settings.TEXT_AREA_MAX_LENGTH, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.BooleanField(choices=settings.GENDER, default=0)
    email_verification_code = models.PositiveIntegerField(default=1234)
    email_verification_generation_date = models.DateTimeField(auto_now=True)
    email_verification_date = models.DateTimeField(auto_now=True)
    mobile_verified = models.BooleanField(choices=settings.VERIFICATION_OPTIONS, default=0,)
    mobile_verification_code = models.PositiveIntegerField(default=1234)
    mobile_verification_generation_date = models.DateTimeField(auto_now=True)
    mobile_verification_date = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(choices=settings.VERIFICATION_OPTIONS, default=0,)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='+')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    profilephoto = models.ImageField(upload_to='static/profiles/', default='profiles/None/no-img.jpg', blank=True,
                                     null=True, )  # staff number

    def __unicode__(self):
        return '%s' % self.first_name

    def __str__(self):
        return '%s ' % self.first_name

    class Meta:
        ordering = ['-last_name']
        #   get_latest_by = "order_date"
        #   permissions = (("can_deliver_pizzas", "Can deliver pizzas"),)
        #   indexes = [
        #             models.Index(fields=['last_name', 'first_name']),
        #             models.Index(fields=['first_name'], name='first_name_idx'),
        #         ]
        #   **Best Practice for indexes is to have more than one field per index
        #   unique_together = (("driver", "restaurant"),)
        #   index_together = [
        #     ["pub_date", "deadline"],
        # ]

    @property
    def slug(self):
        return slugify('%s %s' % self.first_name + ' ' + self.last_name)


class Customer(User):
    is_customer = models.BooleanField(default=True, editable=False)
    customer_type = models.CharField(max_length = settings.SHORT_TEXT_LENGTH, choices=settings.CUSTOMER_PHASE,
                                     default=0, null=False, blank=False)
    role = models.CharField(max_length = settings.SHORT_TEXT_LENGTH, choices=settings.CUSTOMER_USER_ROLES, default=0, null=False,
                            blank=False)
    parent_customer = models.ForeignKey("self", default='', blank=True, null=True)
    #https://docs.djangoproject.com/en/2.1/howto/custom-lookups/
    #https://stackoverflow.com/questions/37946885/how-can-make-the-admin-for-a-foreignkeyself-ban-referring-to-itself

    tags = models.ManyToManyField(CustomerTag, default='', blank=True, related_name='+')
    #write a function to determine if the user is active from the last_active field

    class Meta:
        ordering = ["last_name"]

    #  there has to be a check for parent of parent
    #   Check for similar emails, phone numbers, national id cards etc
    #   A customer can be associated with multiple accounts
    #   Add a customer care module
    #   Upon creating a user, the Customer Induction Workflow is initiated #behind the scenes
    #   Have a "Hustler-ratio" that is like a index of you are doing well or not
    #   At any one time, you have the Customer, their customer (who is simply a listener), the Customer's relationship
    #       manager, and the relationship manager's supervisor
    #   The External Staff can only verify their email, sms and receive notifications.
    #   They can also register to be log-in users.
    #   Need to create a method that will generate a new verification code for email + mobile
    #   Choose a personality > Hustler, Side hustle, etc
    #   Sales, Order Handling, Problem Solving (Withing the order), Customer QoS, Invoicing & Collextion
    #   Value of Customer Base
    #   Business Opportunities
    #   What are the different roles played?
    #   Intelligent Login.



class Staff(User):
    is_konnote_staff = models.BooleanField(default=True, editable=False)
    supervisor = models.ForeignKey("self", default='', blank=True, null=True)
    tags = models.ManyToManyField(StaffTag, default='', blank=True, related_name='+')
    role = models.CharField(max_length = settings.SHORT_TEXT_LENGTH, choices=settings.STAFF_USER_ROLES, default=0, null=False,
                                     blank=False)

    class Meta:
        verbose_name_plural = "Staff"
        ordering = ["last_name"]