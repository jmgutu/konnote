from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tags.models import PostTag
from topics.models import Topic
from django.conf import settings


class Post(models.Model):
    topic = models.ForeignKey(Topic, default='', on_delete=models.CASCADE)
    description = models.CharField(max_length=350, default='')
    tags = models.ManyToManyField(PostTag, default='', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.topic.name + ' | ' + self.description
