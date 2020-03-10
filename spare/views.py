from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from cart.cart import Cart
from cart.forms import CartAddProductForm
from products.models import *
import re
from urllib.parse import urlsplit, urlunsplit

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.http import is_safe_url, urlunquote
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language
)

from trackdeploy import settings as MySettings
# Create your views here.


def spare_create(request):

    cart = Cart(request)
    cart_product_form = CartAddProductForm
    products = Product.objects.all()

    if request.method == "POST":
        form = SpareForm(request.POST)
        if form.is_valid():
            spare = form.save()
            spare.save()

    else:
        form = SpareForm()
    return render(request, 'spare/home_page.html', {'form': form, 'cart': cart, 'products': products,
                                                    'cart_product_form':  cart_product_form,})
    # template_name = 'spare/home_page.html'
    # form_class = SpareForm
    # success_url = reverse_lazy('spare:home_page')
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


