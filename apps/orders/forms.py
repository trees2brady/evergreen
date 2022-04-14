from django import forms


class PayForm(forms.Form):
    card_number = forms.CharField(required=True, min_length=5)
    security_code = forms.CharField(required=True, min_length=3)


