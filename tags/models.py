# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag = models.CharField(
        max_length=20
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        User,
        default='',
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __unicode__(self):
        return self.tag

    class Meta:
        abstract = True


class CustomerTag(Tag):
    is_customer = models.BooleanField(
        default=True,
        editable=False
    )

    class Meta:
        verbose_name_plural = "Customer Tags"


class StaffTag(Tag):
    is_customer = models.BooleanField(
        default=True,
        editable=False
    )

    class Meta:
        verbose_name_plural = "Staff Tags"


class PostTag(Tag):
    is_customer = models.BooleanField(
        default=True,
        editable=False
    )

    class Meta:
        verbose_name_plural = "Post Tags"
