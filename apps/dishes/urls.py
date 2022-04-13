from django.urls import path, re_path

from .views import *

urlpatterns = [
    re_path(r'^$', DishView.as_view(), name="dishes"),
    re_path(r'^(?P<id>\d)$', DishDetail.as_view(), name="dish_detail"),
    re_path(r'^add_to_cart/(?P<id>\d)$', AddToCart.as_view(), name="add_to_cart"),
]