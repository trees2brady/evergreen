from django import forms


class LoginForm(forms.Form):
    # email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, min_length=6, widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, min_length=1)
    last_name = forms.CharField(required=True, min_length=1)
    address = forms.CharField(required=True, min_length=1)
    mobile = forms.CharField(required=True, min_length=5)
