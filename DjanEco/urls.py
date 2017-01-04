from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

from core import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^produtos/', include('product.urls', namespace='product')),
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^admin/', admin.site.urls),
]


