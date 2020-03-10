from django.forms import ModelForm
from django import forms
from .models import *


class SpareForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    model_one = forms.CharField(max_length=50)
    model_two = forms.CharField(max_length=50)

    def save(self):
        new_spare = Spare.objects.create(
            name=self.cleaned_data['name'],
            phone=self.cleaned_data['phone'],
            model_one=self.cleaned_data['model_one'],
            model_two=self.cleaned_data['model_two']

        )
        return new_spare



