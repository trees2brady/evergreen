# from operation.sql_views import *
# from news.models import news,postings
import json

from django.contrib.auth import authenticate, login
# ,ForgetpwdForm,ResetpwdForm
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


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=user_name, password=password)
            if user is not None:
                # if user.is_active:
                    login(request, user)
                    return HttpResponse(json.dumps({"status": 'success', "username": user_name}), content_type='application/json')
                # else:
                #     return HttpResponse(json.dumps({"status":'fail', "msg":u"用户未激活！"}),
                #                         content_type='application/json')
            else:
                return HttpResponse(json.dumps({"status": 'fail', "msg": u"用户名或密码错误！"}),
                                    content_type='application/json')
        else:
            return HttpResponse(json.dumps({"status": 'fail', "msg":"输入不合法！"}),
                                content_type='application/json')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        if request.POST.get("password1", "") != request.POST.get("password2", ""):
            return render(request, "signup.html", {
                "msg": "两次密码不一致！",
            })
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # email = request.POST.get("email", "")
            # if UserProfile.objects.filter(email=email):
            #     return render(request, "signup.html", {
            #         "msg": "该邮箱已被注册！",
            #         "register_form": register_form,
            #     })
            user_name = request.POST.get("username", "")
            if Customer.objects.filter(username=user_name):
                return render(request, "signup.html", {
                    "register_form": register_form,
                    "msg": "该用户名已被注册！",
                })
            password = request.POST.get("password1", "")
            user_profile = Customer()
            user_profile.username = user_name
            # user_profile.email = email
            user_profile.email = ""
            user_profile.is_active = False
            user_profile.password = make_password(password)
            user_profile.save()
            # if send_register_email(email,"register"):
            #     return render(request, "signup.html", {
            #         "register_success":True,
            #         "msg":"注册成功，请注意查收激活邮件！"
            #     })
            # else:
            #     return render(request, "signup.html", {
            #         "register_form": register_form,
            #         "msg": "邮件发送失败！",
            #     })
            return render(request, "signup.html", {
                    "register_success":True,
                    "msg":"注册成功！"
                })
        else:
            try:
                msg = register_form.errors['checkword'][0]
            except:
                msg = '注册失败!'
            return render(request, "signup.html", {
                "register_form": register_form,
                "msg":msg,
            })