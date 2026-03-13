from django.contrib import admin
from .models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'is_published']
    list_filter = ['category', 'is_published']
    search_fields = ['title', 'content']
