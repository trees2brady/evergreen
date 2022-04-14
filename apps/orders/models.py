from django.db import models
from customers.models import Customer
from dishes.models import Dishes
from datetime import datetime
# Create your models here.


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    total_price_of_order = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=20, default="In shopping cart")


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="In progress")
    way_of_pay = models.CharField(max_length=20, default="Debit Card")
