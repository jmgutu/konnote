# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
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
    )

    @property
    def slug(self):
        return slugify(self.tag)

    def __unicode__(self):
        return str(self.tag)

    def __str__(self):
        return str(self.tag)
