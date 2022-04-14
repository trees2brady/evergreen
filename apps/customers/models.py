from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class Customer(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=20, null=True, blank=True)
    is_delivery_man = models.CharField(max_length=1, default="0")
    ssn = models.CharField(max_length=10, default="")
    bank_account = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.last_name
