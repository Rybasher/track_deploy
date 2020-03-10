from django.contrib import admin
from .models import *
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'content']
    list_display_links = ['name', ]


admin.site.register(Contact, ContactAdmin)
