from django.views.generic.base import View
from orders.models import Orders
import json
from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate
from django.http import HttpResponse
from customers.models import Customer
from django.contrib.auth import authenticate, login, logout

# customer看到my delivery:order id, delivery_men_name, delivery_from time, contact info


class DeliveryFromCustomer(View):
    def get(self, request):
        pass


class MakeDelivery(View):  # DeliveryMen make orders into delivery
    def get(self, request):
        orders = Orders.objects.filter(status="paid not delivered")
        return render(request, 'order_to_deliver.html', {"orders": orders})

    def post(self, request):
        order_id = request.POST.get("order_id", "")
        order = Orders.objects.get(id=order_id)
        order.status = "in delivery"
        order.save()
        # orders = Orders.objects.filter(status="paid not delivered")
        # return render(request, 'order_to_deliver.html', {"orders": orders})
        make_delivery = MakeDelivery()
        return make_delivery.get(request)


class DeliveryFromDeliveryMen(View):  # 看到自己delivery transactions 看到payment
    def get(self, request):
        pass


