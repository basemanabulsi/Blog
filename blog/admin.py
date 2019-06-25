# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, User

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = User


admin.site.register(Article)
admin.site.register(User, UserAdmin)