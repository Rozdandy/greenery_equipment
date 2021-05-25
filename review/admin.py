from django.contrib import admin

from .models import ProductReview


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['rate', 'body', 'date_added']
    readonly_fields = ('body', 'user', 'product', 'rate', 'id')
    ordering = ('date_added',)
