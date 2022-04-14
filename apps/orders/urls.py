from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'shopping_cart', OrderView.as_view(), name='order_view'),
    path(r'pay', MakePayment.as_view(), name='pay'),
    path(r'view_transaction', TransactionView.as_view(), name='view_transaction'),
]