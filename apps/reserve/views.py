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
        return render(request, "reserve.html")

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
                return HttpResponse(json.dumps({"status": 'fail', "msg": u"Wrong email or password！"}),
                                    content_type='application/json')
        else:
            return HttpResponse(json.dumps({"status": 'fail', "msg": "Illegal input!"}),
                                content_type='application/json')