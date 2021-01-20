from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','user','publish')
    list_filter = ('created','publish','user')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('publish',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','created','active')
    list_filter = ('active','created','updated')
    search_fields = ('user','body')