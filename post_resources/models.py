from __future__ import unicode_literals

from django.db import models
from posts.models import Post
from resources.models import Resource
from django.conf import settings


class PostResource(models.Model):
    post = models.ForeignKey(Post, default='')
    resource = models.ForeignKey(Resource, default='')
    description = models.CharField(max_length=350, default='')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.topic.name + ' | ' + self.description