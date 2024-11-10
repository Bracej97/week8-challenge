from django.contrib import admin

# Register your models here.

from ecommerce_app.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product_name', 'quantity')
# Register your models here.
admin.site.register(Order, OrderAdmin)
