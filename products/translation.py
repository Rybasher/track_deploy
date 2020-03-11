from modeltranslation.translator import translator, TranslationOptions
from .models import *


class CategoryTranslation(TranslationOptions):
    fields = ('title', )


class ManTranslation(TranslationOptions):
    fields = ('title', 'country')


class ProductTranslation(TranslationOptions):
    fields = ('title', 'content', 'fuel', 'launch_sys', 'engine')


translator.register(Category, CategoryTranslation)
translator.register(Manufacturer, ManTranslation)
translator.register(Product, ProductTranslation)

