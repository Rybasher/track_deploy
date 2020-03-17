from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import *
from django.urls import reverse_lazy
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.


def product_list(request):
    path = request.path_info
    url_split = path.split('/')
    url = url_split[2:]
    str_url = "/".join(url)
    cart = Cart(request)
    search_query = request.GET.get('search', '')
    ot = request.GET.get('ot', '')
    do = request.GET.get('do', '')

    if search_query:
        products = Product.objects.filter(Q(title__contains=search_query) | Q(content__icontains=search_query))

    else:
        products = Product.objects.all()
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())

    else:
        prev_url = ''

    if page.has_next():
        last_url = '?page={}'.format(paginator.page_range[-1])
        next_url = '?page={}'.format(page.next_page_number())

    else:
        next_url = ''
        last_url = ''

    categories = Category.objects.all()
    cart_product_form = CartAddProductForm

    context = {'page_object': page,
               'catagories': categories,
               'cart_product_form': cart_product_form,
               'cart': cart,
               'is_paginated': is_paginated,
               'prev_url': prev_url,
               'next_url': next_url,
               'last_url': last_url,
               'ot': ot,
               'do': do,
               'path': str_url
               }
    return render(request, 'products/product_list.html', context)


def filter_products(request):
    cart = Cart(request)
    cart_product_form = CartAddProductForm
    ot = request.GET.get('ot')
    do = request.GET.get('do')
    if request.method == "GET":

        if not ot and not do:
            ot = 0.0
            do = 20000.0
        elif not ot:
            ot = 0.0
        elif not do:
            do = 20000.0

        products = Product.objects.filter(Q(Q(price__gte=ot) & Q(price__lte=do)) & Q(kind__iexact=request.GET.get("kind")))
        print(ot, do)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request, 'products/product_list.html', {'page_object': page, 'cart': cart,
                                                          'cart_product_form': cart_product_form})

def product_detail(request, slug):
    path = request.path_info
    url_split = path.split('/')
    url = url_split[2:]
    str_url = "/".join(url)
    cart = Cart(request)
    product = Product.objects.get(slug__iexact=slug)
    cart_product_form = CartAddProductForm
    products = product.manufacturer.products.all()
    comments = product.comments.all()
    form_class = GuestCommentForm
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = form_class(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = GuestCommentForm()

    return render(request, 'products/product_detail.html', {'product': product, 'products': products,
                                                            'cart_product_form': cart_product_form, 'cart': cart,
                                                            'comments': comments, 'form': comment_form,
                                                            'new_comment': new_comment,
                                                            'path': str_url})


def category_detail(request, slug):
    path = request.path_info
    url_split = path.split('/')
    url = url_split[2:]
    str_url = "/".join(url)
    categories = Category.objects.all()
    category = Category.objects.get(slug__iexact=slug)
    cart_product_form = CartAddProductForm
    cart = Cart(request)

    return render(request, 'products/categories_detail.html', {'categories': categories,
                                                               'category': category, 'path': str_url,
                                                               'cart': cart,
                                                               'cart_product_form': cart_product_form
                                                               })


def manufacturer_detail(request, slug):
    path = request.path_info
    url_split = path.split('/')
    url = url_split[2:]
    str_url = "/".join(url)
    categories = Category.objects.all()
    manufactures = Manufacturer.objects.all()
    manufacturer = Manufacturer.objects.get(slug__iexact=slug)
    ot = request.GET.get('ot', '')
    do = request.GET.get('do', '')
    if ot and do:
        products = manufacturer.products.filter(price__gte=ot, price__lte=do).all()

    elif ot:
        products = manufacturer.products.filter(price__gte=ot)
    elif do:
        products = manufacturer.products.filter(price__lte=do)
    else:
        products = manufacturer.products.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())

    else:
        prev_url = ''

    if page.has_next():
        last_url = '?page={}'.format(paginator.page_range[-1])
        next_url = '?page={}'.format(page.next_page_number())

    else:
        next_url = ''
        last_url = ''
    cart_product_form = CartAddProductForm
    cart = Cart(request)
    context = {'manufacturer': manufacturer,
               'page_object': page,
               "manufacturers": manufactures,
               'categories': categories,
               'cart_product_form': cart_product_form,
               'cart': cart,
               'is_paginated': is_paginated,
               'prev_url': prev_url,
               'next_url': next_url,
               'last_url': last_url,
               'ot': ot,
               'do': do,
               'path': str_url
               }
    return render(request, 'products/manufacturer_detail.html', context)


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryCreateView(CreateView):
    template_name = 'products/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ManufaturerCreateView(CreateView):
    template_name = 'products/manufacturer_create.html'
    form_class = ManufacturerForm
    success_url = reverse_lazy('products:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




