from django.urls import path

from . import views


app_name = 'order'
urlpatterns = [
    path('', views.index, name='index'),
    path('orders', views.orders, name='orders'),
    path('order/<int:id>', views.order_detail, name='order-detail'),
    path('archive', views.archive, name='archive'),
]