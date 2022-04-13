from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .models import Dishes
from orders.models import Orders
from order_details.models import OrderDetails


class OrderView(View):
    def get(self, request):
        if request.user.is_authenticated:
            order = Orders.objects.filter(customer_id=request.user.id).filter(status="In shopping cart")
            if len(order) == 0:
                return render(request, 'shopping_cart.html', {"msg": "There is nothing in your shopping cart yet!"})
            else:
                order = order[0]
            order_details = OrderDetails.objects.filter(order_id=order.id)
            dish_ids = [item.dish_id for item in order_details]
            dishes = Dishes.objects.filter(id__in=dish_ids)
            return render(request, 'shopping_cart.html', {"order": order, "dishes": dishes})
        else:
            return render(request, 'login.html', {"msg": "Please login first!"})
