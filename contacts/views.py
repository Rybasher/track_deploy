from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from django.urls import reverse_lazy
from .forms import *
from cart.cart import Cart
# Create your views here.


def contact_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = ContactCreate(request.POST)
        if form.is_valid():
            spare = form.save()
            spare.save()

    else:
        form = ContactCreate()
    return render(request, 'contacts/contsct_form.html', {'form': form, 'cart': cart})
