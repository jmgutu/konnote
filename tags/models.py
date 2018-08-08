# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default='')

    def __unicode__(self):
        return self.tag
