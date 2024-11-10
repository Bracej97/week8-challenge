from django.urls import path
from ecommerce_app import views

urlpatterns = [
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/delete/', views.order_delete, name='order_delete'),
    path('orders/create/', views.order_new, name='order_create'),
    path('orders/edit/', views.order_edit, name='order_edit')
]
