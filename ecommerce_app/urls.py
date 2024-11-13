from django.urls import path
from ecommerce_app import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('delete/<int:id>/', views.order_delete, name='order_delete'),
    path('create/', views.order_create, name='order_create'),
    path('edit/<int:id>/', views.order_edit, name='order_edit')
]
