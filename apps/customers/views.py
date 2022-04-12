import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render
# from .models import Customer,EmailVerifyRecord
from django.views.generic.base import View
from .models import Customer
from .forms import LoginForm, RegisterForm

# from utils.email_send import send_register_email,send_resetpwd_email


def index(request):
    return render(request, "homepage.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "homepage.html", {
            "msg": "Logout!"})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user is not None:
                # if user.is_active:
                login(request, user)
                return render(request, "homepage.html", {
                "msg": "Login successfully!",
            })
            else:
                return HttpResponse(json.dumps({"status": 'fail', "msg": u"Wrong email or password！"}),
                                    content_type='application/json')
        else:
            return HttpResponse(json.dumps({"status": 'fail', "msg": "Illegal input!"}),
                                content_type='application/json')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        if request.POST.get("password1", "") != request.POST.get("password2", ""):
            return render(request, "register.html", {
                "msg": "Passwords are not consistent!",
            })
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email", "")
            if Customer.objects.filter(email=email):
                return render(request, "register.html", {
                    "register_form": register_form,
                    "msg": "Email already exists!",
                })

            username = request.POST.get("username", "")
            password = request.POST.get("password1", "")
            first_name= request.POST.get("first_name", "")
            last_name = request.POST.get("last_name", "")
            address = request.POST.get("address", "")
            mobile = request.POST.get("mobile", "")
            new_customer = Customer.objects.create_user(username=username, email=email, password=password,
                                                        first_name=first_name, last_name=last_name,
                                                        address=address, mobile=mobile)
            new_customer.save()
            return render(request, "register.html", {
                "register_success": True,
                "msg": "Register Successful!"
            })
        else:
            print(register_form.errors)
            try:
                msg = register_form.errors['checkword'][0]
            except:
                msg = 'Failed to register!'
            return render(request, "register.html", {
                "register_form": register_form,
                "msg": msg,
            })
