from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.

from .models import *


@admin.register(CarName)
class CarNameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


@admin.register(CarLocation)
class CarLocation(admin.ModelAdmin):
    list_display = ('pk', 'title')


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery
    extra = 1



@admin.register(CarsModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'prise', 'created_at', 'location', 'colour', 'status', 'get_photo', 'distance', 'produced_at')
    list_editable = ('name', 'prise', 'location', 'colour', 'colour', 'produced_at')

    inlines = [GalleryInline]


    def get_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75">')
            except:
                return '-'
        return '-'

