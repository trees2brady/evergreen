from django.db import models

# Create your models here.


class Dishes(models.Model):
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.CharField(max_length=200, default="1")
    description = models.CharField(max_length=200, default="")
    image = models.ImageField(default="img\\default.jpg")

    def __str__(self):
        return self.dish_name
