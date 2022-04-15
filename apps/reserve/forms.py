import datetime

from django import forms


class ReserveForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6, widget=forms.PasswordInput)
    number_of_people = forms.DecimalField(max_digits=2, decimal_places=0)
    reservation_time = forms.DateTimeField(input_formats=['yyyy-mm-dd hh:mm'])
