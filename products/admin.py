from django.contrib import admin
from .models import *
# Register your models here.



class ProductAdmin(admin.ModelAdmin):

    list_display_links = ('title', )
    search_fields = ('title', 'content')

    # def category(self, rec):
    #     return '%s (%s)' % (rec.manufacturer.title, rec.category.title)
    # category.short_description = "Название и рубрика"
    list_display = ('title', 'content', 'price', 'manufacturer', 'stok', 'available', 'published_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = ('title', )
    ordering = ['title']


class ManufacturerAdmin(admin.ModelAdmin):

    list_display_links = ('title', )
    list_display = ('title', 'category')
    ordering = ['title']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Comment)
