from django.contrib import admin
from .models import *
# Register your models here.


class SpareAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'model_one', 'model_two', 'published_date')
    list_display_links = ('name', )


admin.site.register(Spare, SpareAdmin)