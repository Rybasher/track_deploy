"""trackdeploy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.conf.urls import handler404, handler403, handler500
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
      path('i18n/set_language', include('django.conf.urls.i18n')),
      path(_('admin/'), admin.site.urls),
      path('', include('spare.urls')),
      path('', include('blog.urls')),
      path('', include('cart.urls')),
      path('', include('orders.urls')),
      path('', include('payments.urls')),
      path('', include('products.urls')),
      path('', include('contacts.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'blog.views.error_404'
handler403 = 'blog.views.error_403'

