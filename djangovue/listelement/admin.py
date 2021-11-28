from django.contrib import admin
from . models import Element, Category, Type

class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Element, ElementAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)