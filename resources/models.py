# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default='')  # staff number
    resource_file = models.FileField(upload_to='uploads/', default='')  # staff number
    description = models.TextField(default='', blank=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Resources"