from django.views.generic.base import View
import json
from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate
from django.http import HttpResponse
from customers.models import Customer
from .models import Reservation


class Reserve(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer_id = request.user.id
            reservations = Reservation.objects.filter(customer_id=customer_id)
            if len(reservations) == 0:
                return render(request, 'reserve.html', {"msg": "You have no reservation yet! You can make reservations now."})
            else:
                return render(request, "reservations.html", {"reservations": reservations})
        else:
            return render(request, 'login.html', {"msg": "Please login first!"})

    def post(self, request):
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                customer = Customer.objects.filter(username=username)
                number_of_people = request.POST.get("number_of_people", "")
                reservation_time = request.POST.get("reservation_time", "")
                new_reservation = Reservation()
                new_reservation.customer = customer
                new_reservation.number_of_people = number_of_people
                new_reservation.reservation_time = reservation_time
                new_reservation.save()
                return render(request, "reserve.html", {
                    "register_success": True,
                    "msg": "Reserve Successful!"
                })
            else:
                return render(request, "reserve.html", {
                    "msg": u"Wrong email or password！"})
        else:
            return render(request, "reserve.html", {
                "msg": "Illegal input!"})
