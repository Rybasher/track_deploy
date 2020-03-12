from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from django.shortcuts import get_object_or_404
from cart.cart import Cart
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
# Create your views here.
from .models import *



@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
            # return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})



