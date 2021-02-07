# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    """
    The name of a discipline or language. A noun.
    """
    name = models.CharField(
        max_length=100,
        default=''
    )
    description = models.CharField(
        max_length=250,
        default=''
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
