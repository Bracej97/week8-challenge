from django import forms
from django.core.exceptions import ValidationError
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer_name', 'product_name', 'quantity', 'order_date')

        labels = {
            'customer_name': 'Name of the customer',
            'product_name':  'Product to order',
            'quantity': 'How many to order',
            'order_date': 'when ordered'
        }

        # Custom validation for the 'title' field
    def clean_customer_name(self):
        customer_name = self.cleaned_data.get('customer_name')

        # Remove leading/trailing spaces
        customer_name = customer_name.strip()

        return customer_name

    def clean_product_name(self):
        product_name = self.cleaned_data.get('product_name')

        # Remove leading/trailing spaces
        product_name = product_name.strip()

        return product_name

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')

        return quantity

    def clean_order_date(self):
        order_date = self.cleaned_data.get('order_date')

        return order_date
