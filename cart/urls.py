from django.conf.urls import url
from . import views


app_name = 'cart'

urlpatterns = [
    url(r'^detail/', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^add/(?P<product_id>\d+)/$', views.add_one, name='add_one'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),

]