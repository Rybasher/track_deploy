from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class ProductTranslationAdmin(TranslationAdmin):
    list_display_links = ('title', )
    search_fields = ('title', 'content')

    # def category(self, rec):
    #     return '%s (%s)' % (rec.manufacturer.title, rec.category.title)
    # category.short_description = "Название и рубрика"
    list_display = ('title', 'content', 'price', 'manufacturer', 'stok', 'available', 'published_date', 'views')


class CategoryTranslationAdmin(TranslationAdmin):
    list_display_links = ('title',)
    list_display = ('title', )
    ordering = ['title']


class ManufacturerTranslationAdmin(TranslationAdmin):

    list_display_links = ('title', )
    list_display = ('title', 'category')
    ordering = ['title']


admin.site.register(Product, ProductTranslationAdmin)
admin.site.register(Category, CategoryTranslationAdmin)
admin.site.register(Manufacturer, ManufacturerTranslationAdmin)
admin.site.register(Comment)
