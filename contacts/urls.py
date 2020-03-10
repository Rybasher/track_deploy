from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "contacts"

urlpatterns = [
    path('contacts/', contact_create, name='contact_create'),

]