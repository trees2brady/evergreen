from django.urls import path, re_path

from .views import *

urlpatterns = [
    path(r'', DishView.as_view(), name="dishes"),
    re_path(r'(?P<id>\d)', DishDetail.as_view(), name="dish_detail")
]