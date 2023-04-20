from django.contrib import admin
from django.urls import path, include 
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('parts.urls', namespace='parts')),
    url('order/', include('order.urls', namespace='order')),
]
