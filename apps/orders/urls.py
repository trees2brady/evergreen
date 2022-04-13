from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'shopping_cart', OrderView.as_view(), name='order_view'),
]