from django.contrib import admin

from .models import Category, Post, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'overview',
        'article',
        'image',
        'date_added',
        'image_url'
        'thumbnail'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'article',
        'date_added',
    )
