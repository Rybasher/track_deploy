from django.urls import path
from .views import *


app_name = 'about'

urlpatterns = [
    path('', about, name='about')
]