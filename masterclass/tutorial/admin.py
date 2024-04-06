from django.contrib import admin

from . models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(Locate)
class LocateAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(MasterClass)
class MasterClassAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'description', 'time', 'locate', 'price', 'author', 'photo']
    search_fields = ['category', 'locate', 'price', 'author']