from django.urls import path

from .views import *

urlpatterns = [
    path('', DeliveryFromCustomer.as_view(), name='reserve'),
    path('make_delivery', MakeDelivery.as_view(), name='make_delivery'),
]