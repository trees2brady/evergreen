from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
    # email = forms.EmailField(required=True)


class ResetpwdForm(forms.Form):
    newpwd1 = forms.CharField(required=True,min_length=6)
    newpwd2 = forms.CharField(required=True, min_length=6)