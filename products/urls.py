from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "products"

urlpatterns = [
    path('katalog/', product_list, name='product_list'),
    path('product/<str:slug>/', product_detail, name="product_detail"),
    # path('product/<str:slug>/edit/', product.edit)
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('category/<str:slug>/', category_detail, name="category_detail"),
    path('manufacturer/<str:slug>/', manufacturer_detail, name="manufacturer_detail"),
    path('add_manufacturer/', ManufaturerCreateView.as_view(), name='add_manufacturer'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),



]
