from django.db import models
from customers.models import Customer
from dishes.models import Dishes
from datetime import datetime
# Create your models here.


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField(default=datetime.now)
    finished_time = models.DateTimeField()
