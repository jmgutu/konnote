from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag
from topics.models import Topic
# Create your models here.


class Post(models.Model):
    topic = models.ForeignKey(Topic, default='')
    description = models.CharField(max_length=350, default='')
    tags = models.ManyToManyField(Tag, default='', blank=True,)
    created_by = models.ForeignKey(User, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.topic.name + ' | ' + self.description
