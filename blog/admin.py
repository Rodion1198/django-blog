from django.contrib import admin

from .models import Category, Comment, Post, Profile, RSSPost


@admin.register(RSSPost)
class RSSPostAdmin(admin.ModelAdmin):
    fields = ['title', 'link']
    list_display = ('title', 'link')


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
