from django.contrib import admin

from .models import Category, Post

admin.site.register(Post)
admin.site.register(Category)


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
