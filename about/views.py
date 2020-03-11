from django.shortcuts import render

# Create your views here.
from django.conf.global_settings import LANGUAGE_CODE


def about(request):
    path = request.path_info
    url_split = path.split('/')
    url = url_split[2:]
    str_url = "/".join(url)

    return render(request, 'about/about.html', {'path': str_url})
