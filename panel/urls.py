# coding=utf-8

from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^product/create/$', views.product_create, name='product_create'),
    url(r'^product/list/$', views.product_list, name='product_list'),     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
