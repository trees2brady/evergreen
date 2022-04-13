from django import forms


class ReserveForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6, widget=forms.PasswordInput)
    number_of_people = forms.DecimalField(max_digits=2, decimal_places=0)
    reserve_date = date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
