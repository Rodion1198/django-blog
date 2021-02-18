from django.contrib import admin

from .models import Category, Post, Profile


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
