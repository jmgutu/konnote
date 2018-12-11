# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from tags.models import CustomerTag, StaffTag
admin.site.register(CustomerTag)
admin.site.register(StaffTag)
