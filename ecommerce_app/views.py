from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

from .forms import OrderForm
from .models import Order


# Create your views here.

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'ecommerce_app/order_list.html', {'orders':orders})

def order_create(request):
    if request.method('POST'):
        form = OrderForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('orders_list')

    else:
        form = OrderForm()
    return render(request, 'ecommerce_app/order_form.html', {'form':form})

def order_edit(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order.save()

            # messages.success(request, "Order successfully edited!")
            return redirect('order_list', id=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'ecommerce_app/order_form.html', {'form': form, 'order':order})

def order_delete(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'ecommerce_app/order_confirm_delete.html', {'order':order})
