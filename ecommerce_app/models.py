from django.db import models

# Create your models here.

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    order_date = models.DateField()

    def __str__(self):
        return f'{self.customer_name} has ordered {self.product_name}'
