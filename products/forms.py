from .models import *
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = {'title'}

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')

        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug may be unique. We have "{}" slug alredy'.format(new_slug))
        return new_slug


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = {'title', 'category'}

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')

        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug may be unique. We have "{}" slug alredy'.format(new_slug))
        return new_slug


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'slug', 'content', 'image', 'image_two', 'image_three', 'image_four', 'image_five',
                  'image_six', 'image_seven', 'fuel', 'rated_power', 'max_power', 'launch_sys', 'engine', 'weight',
                  'price', 'manufacturer', 'stok', 'available')

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')

        return new_slug


class GuestCommentForm(forms.ModelForm):

    # capctha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'неправильный текст'})
    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'product': forms.HiddenInput}
        fields = ('author', 'content')

