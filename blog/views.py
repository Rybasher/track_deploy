from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import *
from django.urls import reverse_lazy
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/posts_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # cart = Cart(request)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)
