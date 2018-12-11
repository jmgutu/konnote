# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from endusers.models import User, Customer, Staff


class UserAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active','date_joined', 'last_login')
    list_filter = ('is_staff',)
    search_fields = ('username', 'first_name', 'last_name')
    pass


class CustomerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_customer', 'is_active','date_joined', 'last_login')
    list_filter = ('is_customer',)
    search_fields = ('username', 'first_name', 'last_name')
    pass


class StaffAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active','date_joined', 'last_login')
    list_filter = ('is_staff',)
    search_fields = ('username', 'first_name', 'last_name')
    pass


# class ItemDetailInline(admin.TabularInline):
#     model = ItemDetail
#
# class ItemAdmin(admin.ModelAdmin):
#     inlines = [
#         ItemDetailInline,
#     ]

admin.ModelAdmin.actions_on_top = True
admin.ModelAdmin.actions_on_bottom = True
admin.ModelAdmin.actions_selection_counter = False
admin.ModelAdmin.show_full_result_count = True


admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Staff, StaffAdmin)

