from django.db import models
from orders.models import Orders
from dishes.models import Dishes
# Create your models here.


class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    dish_amount = models.CharField(max_length=200)
    total_price_of_dish = models.DecimalField(max_digits=10, decimal_places=2)
