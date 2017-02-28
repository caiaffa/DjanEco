# coding=utf-8

from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^create/$', views.product_create, name='product_create'),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
