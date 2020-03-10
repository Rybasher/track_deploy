from django.urls import path
from .views import *
from django.conf.urls.i18n import i18n_patterns


app_name = 'blog'

urlpatterns = [
    path('about/', about, name='about'),
    path('delivery/', delivery, name='delivery'),
    path('news/', posts_list, name='posts_list'),
    path('news/<int:pk>', post_detail, name='post_detail'),
    path('news/<int:pk>/edit', PostEditView.as_view(), name='edit'),
    path('news/<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
    path('news/add/', PostCreateView.as_view(), name='add'),


]

