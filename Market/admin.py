from django.contrib import admin
from .models import Products, Category


# Register your models here.
class ProdAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'published')
    list_display_links = ('name', 'cost')
    search_fields = ('name', 'cost')


class CatAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Products,) #ProdAdmin)
admin.site.register(Category,) #CatAdmin)
