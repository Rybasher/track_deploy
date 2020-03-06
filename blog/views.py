from django.shortcuts import render
from .models import *
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/posts_list.html', context)
