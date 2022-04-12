from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class Customer(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.last_name
