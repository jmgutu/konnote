# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class PostType(models.Model):
    name = models.CharField(
        default='',
        null=False,
        blank=False,
        max_length=100,
    )
    description = models.TextField(
        default='',
        null=False,
        blank=False,
        max_length=350,
    )
    created_by = models.ForeignKey(
        User,
        default=None,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
