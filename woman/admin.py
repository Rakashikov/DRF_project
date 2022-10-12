from django.contrib import admin
from .models import Woman, Category


# Register woman model
@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    verbose_name = 'Женщина'
    verbose_name_plural = 'Женщины'
    save_as = True
    save_on_top = True


# Register category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
