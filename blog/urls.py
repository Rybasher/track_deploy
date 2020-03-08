from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('news/', posts_list, name='posts_list'),
    path('news/<int:pk>', post_detail, name='post_detail')
]
