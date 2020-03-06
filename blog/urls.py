from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('news/', posts_list, name='posts_list')
]