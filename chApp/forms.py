from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField



class regForm(forms.Form):
    userName = forms.CharField(label='Username', max_length=20)
    fName = forms.CharField(label='First Name', max_length=20)
    lName = forms.CharField(label='Last Name', max_length=20)
    country = LazyTypedChoiceField(label='Country', choices=countries)
    email = forms.EmailField(label='Email', max_length=100)
