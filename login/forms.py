import hashlib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField


class regForm(forms.Form):
    userName = forms.CharField(label='Username', max_length=30)
    fName = forms.CharField(label='First Name', max_length=20)
    lName = forms.CharField(label='Last Name', max_length=20)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    rePass = forms.CharField(label='Re-type password', widget=forms.PasswordInput())


    def process(self):
        cd = self.cleaned_data
        if cd['password'] == cd['rePass']:
            user = User.objects.create_user(cd['userName'], cd['email'], cd['password'], first_name=cd['fName'], last_name=cd['lName'])
            user.save()
            return True


class loginForm(forms.Form):
    userName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'formInput', 'placeholder' : 'username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class' : 'formInput', 'placeholder' : 'password'}))

