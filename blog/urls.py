from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('news/', posts_list, name='posts_list')
]