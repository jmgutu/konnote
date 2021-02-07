from __future__ import unicode_literals

from django.db import models
from tags.models import Tag
from topics.models import Topic
from django.contrib.auth.models import User
from utility.helpers import generate_str
from post_types.models import PostType


class Post(models.Model):
    topic = models.ForeignKey(
        Topic,
        default=None,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    post_type = models.ForeignKey(
        PostType,
        default=None,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = models.TextField(
        default='',
        max_length=350,
    )
    tags = models.ManyToManyField(
        Tag,
        default='',
        blank=True
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
        return generate_str([
            self.topic.name,
            self.description
            ]
        )

    def __str__(self):
        return generate_str([
            self.topic.name,
            self.description
            ]
        )
