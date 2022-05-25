# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    name = models.CharField(
        max_length=100,
        default=''
    )
    created_by = models.ForeignKey(
        User,
        default='',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
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
