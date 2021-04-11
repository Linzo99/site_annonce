from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published', 'status', 'jourj')
    list_filter = ('status', 'author', 'category', 'published')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author','category')
    date_hierarchy = 'published'
    ordering = ('status', 'published')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','post', 'created')
    list_filter = ('name', 'created', 'active')
    search_fields = ('name', 'body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('slug',)
    search_fields = ('slug',)
    prepopulated_fields = {'slug':('name',)}