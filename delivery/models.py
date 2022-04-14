from django.db import models
from orders.models import Orders
from customers.models import Customer
from datetime import datetime


class Delivery(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    delivery_men = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creating_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="in progress")
    service_fee = models.DecimalField(max_digits=5, decimal_places=2)


class Salary(models.Model):
    delivery_men = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField()
    status = models.CharField(max_length=20, default="in accumulating")
