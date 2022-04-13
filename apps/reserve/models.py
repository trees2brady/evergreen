from django.db import models
from customers.models import Customer
# Create your models here.


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    number_of_people = models.DecimalField(max_digits=2, decimal_places=0)
    creating_date = models.DateTimeField(auto_now_add=True)
    reservation_time = models.DateTimeField()
    status = models.CharField(max_length=20, default="incoming")
