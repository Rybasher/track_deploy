from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class PostTranslationAdmin(TranslationAdmin):
    list_display = ('title', 'content', 'content_two')
    list_display_links = ('title',)


admin.site.register(Post, PostTranslationAdmin)

