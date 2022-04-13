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
    status = models.CharField(max_length=20, default="In shopping cart")
