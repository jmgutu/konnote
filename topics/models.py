# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from chapters.models import Chapter
from django.contrib.auth.models import User
from utility.helpers import generate_str


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
        User,
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
        return generate_str([
            self.chapter.level.name,
            ' | ',
            self.chapter.name,
            ' | ',
            self.name
            ]
        )

    def __str__(self):
        return generate_str([
            self.chapter.level.name,
            self.chapter.name,
            self.name
            ]
        )
