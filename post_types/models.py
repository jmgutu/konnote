# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class PostType(models.Model):
    name = models.CharField(default='', null=False, blank=False, max_length=settings.CHAR_MAX_LENGTH)
    description = models.TextField(default='', null=False, blank=False, max_length=settings.TEXT_AREA_MAX_LENGTH)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name