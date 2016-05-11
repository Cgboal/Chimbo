import hashlib
from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from .models import User



class regForm(forms.Form):
    userName = forms.CharField(label='Username', max_length=20)
    fName = forms.CharField(label='First Name', max_length=20)
    lName = forms.CharField(label='Last Name', max_length=20)
    country = LazyTypedChoiceField(label='Country', choices=countries)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    rePass = forms.CharField(label='Re-type password', widget=forms.PasswordInput())

    def process(self):
        cd = self.cleaned_data
        if cd['password'] == cd['rePass']:
            pHash = hashlib.md5(cd['password']).hexdigest()
            u = User(userName=cd['userName'], pHash=pHash, fName=cd['fName'], lName=cd['lName'], country=cd['country'],
                     email=cd['email'], perms=0)
            u.save()
        else:
            return None