from django.urls import path
from ecommerce_app import views

urlpatterns = [
    path('order/', views.order_list, name='order_list'),
    path('order/delete/', views.order_delete, name='order_delete'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/edit/', views.order_edit, name='order_edit')
]
