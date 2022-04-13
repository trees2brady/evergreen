from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Dishes
# Create your views here.


def index(request):
    return render(request, "login.html")


class DishView(View):

    def get(self, request):
        dishes = Dishes.objects.all()
        return render(request, 'dishes.html', {"dishes": dishes})


class DishDetail(View):

    def get(self, request, id):
        dish = Dishes.objects.get(id=id)
        return render(request, 'dish_detail.html', {"dish": dish})