# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from chapters.models import Chapter


class Topic(models.Model):
    chapter = models.ForeignKey(Chapter, default='')
    name = models.CharField(max_length=100, default='')
    created_by = models.ForeignKey(User, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.chapter.level.name + ' | ' + self.chapter.name + ' | ' + self.name



