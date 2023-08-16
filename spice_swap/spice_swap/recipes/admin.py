from django.contrib import admin

from .models import Recipe, Tag, Comment, Like

admin.site.register(Recipe)

admin.site.register(Tag)

admin.site.register(Comment)

admin.site.register(Like)