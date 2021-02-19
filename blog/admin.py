from django.contrib import admin

from .models import Category, Comment, Post, Profile


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
