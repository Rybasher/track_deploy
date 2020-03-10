from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, reverse
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.http import HttpResponse

# Create your views here.


def error_404(request, exception):
    return render(request, 'blog/error_404.html')


def error_403(request, exception):
    return render(request, 'blog/error_403.html')


def about(request):
    # cart = Cart(request)
    return render(request, 'blog/about.html')


def delivery(request):
    # cart = Cart(request)
    return render(request, 'blog/delivery.html')


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


# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('blog:post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', {'form': form})


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:posts_list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostEditView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/post_edit.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:posts_list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog/post_delete.html'
    model = Post
    success_url = reverse_lazy('blog:posts_list')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




