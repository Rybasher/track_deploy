from .models import *
from django import forms
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactCreate(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)

    name.widget.attrs.update({'class': 'form-control', 'id': 'form-name', 'placeholder': _('name')})
    email.widget.attrs.update({'class': 'form-control', 'id': 'form-email', 'placeholder': _('email')})
    content.widget.attrs.update({'class': 'form-control md-textarea', 'id': 'form-text', 'rows': '3',
                                 'placeholder': _('message')})

    def save(self):
        new_contact = Contact.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            content=self.cleaned_data['content'],


        )
        return new_contact

