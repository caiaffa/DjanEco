# coding=utf-8

from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^categoria/(?P<slug>[\w_-]+)/$', views.category, name='category'),
    url(r'^(?P<slug>[\w_-]+)/$', views.product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
