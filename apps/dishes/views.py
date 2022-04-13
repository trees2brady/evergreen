from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .models import Dishes
from django.db.models import Q
from orders.models import Orders
from order_details.models import OrderDetails


class DishView(View):

    def get(self, request):
        dishes = Dishes.objects.all()
        resp = request.GET.get('resp')
        return render(request, 'dishes.html', {"dishes": dishes, "msg": resp})


class DishDetail(View):

    def get(self, request, id):
        dish = Dishes.objects.get(id=id)
        return render(request, 'dish_detail.html', {"dish": dish})


class AddToCart(View):

    def get(self, request, id):
        if request.user.is_authenticated:
            dish = Dishes.objects.get(id=id)
            customer_id = request.user.id
            order = Orders.objects.filter(customer_id=customer_id).filter(status="In shopping cart")
            if len(order) == 0:
                new_order = Orders()
                new_order.dish = dish
                new_order.customer = request.user
                new_order.status = "In shopping cart"
                new_order.save()
            order = Orders.objects.filter(customer_id=customer_id).filter(status="In shopping cart")[0]
            new_order_detail = OrderDetails()
            new_order_detail.order = order
            new_order_detail.dish = dish
            new_order_detail.dish_amount = 1
            new_order_detail.total_price_of_dish = dish.price
            new_order_detail.save()
            order.total_price_of_order += dish.price
            order.save()

            msg = "The dish has been added to your shopping cart!"
            return HttpResponseRedirect('/dishes/?resp=%s'%msg)
        else:
            dish = Dishes.objects.get(id=id)
            return render(request, 'dish_detail.html', {"dish": dish, "msg": "Please login first!"})
