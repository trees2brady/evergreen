from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .models import Payment
from orders.models import Orders
from order_details.models import OrderDetails
from .forms import PayForm
from dishes.models import Dishes


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


class MakePayment(View):
    def get(self, request):
        user_id = request.user.id
        order = Orders.objects.filter(customer_id=user_id).filter(status="In shopping cart")
        if len(order) == 0:
            return render(request, 'dishes.html', {"msg": "You have nothing in cart! You can add dishes into cart now."})
        else:
            order = order[0]
            order_details = OrderDetails.objects.filter(order_id=order.id)
            dish_ids = [item.dish_id for item in order_details]
            dishes = Dishes.objects.filter(id__in=dish_ids)
            return render(request, 'pay_page.html', {"order": order, "dishes": dishes})

    def post(self, request):
        register_form = PayForm(request.POST)
        user_id = request.user.id
        order = Orders.objects.filter(customer_id=user_id).filter(status="In shopping cart")
        order = order[0]
        order_details = OrderDetails.objects.filter(order_id=order.id)
        dish_ids = [item.dish_id for item in order_details]
        dishes = Dishes.objects.filter(id__in=dish_ids)
        if register_form.is_valid():
            payment = Payment()
            payment.customer = request.user
            payment.order = order
            payment.amount = order.total_price_of_order
            payment.status = "finished"
            payment.save()
            order.status = "paid not delivered"
            order.save()
            msg = "Pay successfully!"
            return render(request, 'homepage.html', {"msg": msg})
        else:
            msg = "Input is invalid!"
            return render(request, 'pay_page.html', {"order": order, "dishes": dishes, "msg": msg})


class TransactionView(View):
    def get(self, request):
        transactions = Payment.objects.filter(customer_id=request.user.id)
        if len(transactions) == 0:
            msg = "You have no transaction yet!"
        else:
            msg = ""
        return render(request, 'transactions.html', {"transactions": transactions, "msg": msg})
