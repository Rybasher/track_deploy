from .models import *
from django.forms import ModelForm
from modeltranslation.forms import TranslationModelForm


class PostForm(TranslationModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'content_two', 'image_one', 'image_two',)
