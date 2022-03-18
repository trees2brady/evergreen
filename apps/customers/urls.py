from django.urls import path

from .views import *

urlpatterns = [
    path(r'register/', RegisterView.as_view(), name="register"),
    path(r'login/', LoginView.as_view(), name="login"),
]