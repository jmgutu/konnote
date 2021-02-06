# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from chapters.models import Chapter
from django.conf import settings


class Topic(models.Model):
    chapter = models.ForeignKey(
        Chapter,
        default='',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=100,
        default=''
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default='',
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    modified_date = models.DateTimeField(
        auto_now=True
    )

    def __unicode__(self):
        return ''.join([
            self.chapter.level.name,
            ' | ',
            self.chapter.name,
            ' | ',
            self.name
            ]
        )
