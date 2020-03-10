from django.urls import path
from .views import *

app_name = 'spare'

urlpatterns = [
    path('', spare_create, name='home_page'),

]
