# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Tag(models.Model):
    tag = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='')

    def __unicode__(self):
        return self.tag

    class Meta:
        abstract = True


class CustomerTag(Tag):
    is_customer = models.BooleanField(default=True, editable=False)

    class Meta:
        verbose_name_plural = "Customer Tags"


class StaffTag(Tag):
    is_customer = models.BooleanField(default=True, editable=False)

    class Meta:
        verbose_name_plural = "Staff Tags"

class PostTag(Tag):
    is_customer = models.BooleanField(default=True, editable=False)

    class Meta:
        verbose_name_plural = "Post Tags"