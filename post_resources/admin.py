# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from post_resources.models import PostResource

admin.site.register(PostResource)
