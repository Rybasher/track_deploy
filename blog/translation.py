from modeltranslation.translator import translator, TranslationOptions
from .models import *
from .forms import *


class PostTranslations(TranslationOptions):
    fields = ('title', 'content', 'content_two')
    required_languages = {'ru': ('title',), 'default': ('title', 'content')}


translator.register(Post, PostTranslations)




