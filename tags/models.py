# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    A Word or short phrase that can be used to describe a post. E.g django, models, fields, format etc
    """
    tag = models.CharField(
        max_length=30
    )

    date_created = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        User,
        default=None,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    @property
    def slug(self):
        return slugify(self.tag)

    def __unicode__(self):
        return str(self.tag)

    def __str__(self):
        return str(self.tag)
