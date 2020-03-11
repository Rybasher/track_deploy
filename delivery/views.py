from django.shortcuts import render

# Create your views here.


def delivery(request):
    path = request.path_info
    url_split = path.split('/')
    print (url_split)
    url = url_split[2:]
    str_url = "/".join(url)
    return render(request, 'delivery/delivery.html', {'path': str_url})
