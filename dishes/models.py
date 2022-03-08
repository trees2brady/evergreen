from django.db import models

# Create your models here.


class Dishes(models.Model):
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
