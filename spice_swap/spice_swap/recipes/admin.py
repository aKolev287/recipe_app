from django.contrib import admin

from .models import Recipe, Tag, Comment

from django.contrib import admin
from .models import Recipe, Tag, Comment

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date')
    list_filter = ('tags', 'date')
    search_fields = ('title', 'user__username')
    ordering = ('-date',)
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at')
    list_filter = ('recipe', 'created_at')
    search_fields = ('user__username', 'recipe__title')
    

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
