from django.urls import path
from .views import *
from django.conf.urls.i18n import i18n_patterns


app_name = 'blog'

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/edit', PostEditView.as_view(), name='edit'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
    path('add/', PostCreateView.as_view(), name='add'),


]

