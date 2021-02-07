# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from resources.models import Resource

admin.site.register(Resource)
