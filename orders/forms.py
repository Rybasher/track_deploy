from django.forms import ModelForm
from .models import Order


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'data_one']
