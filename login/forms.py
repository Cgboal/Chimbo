import hashlib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField


class regForm(forms.Form):
    userName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder' : 'Username'}))
    fName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder' : 'First Name'}))
    lName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder' : 'Last Name'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder' : 'Email'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder' : 'Password'}))
    rePass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Retype Password'}))


    def process(self):
        cd = self.cleaned_data
        if cd['password'] == cd['rePass']:
            user = User.objects.create_user(cd['userName'].lower(), cd['email'], cd['password'], first_name=cd['fName'], last_name=cd['lName'])
            user.save()
            return True


class loginForm(forms.Form):
    userName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'formInput', 'placeholder' : 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'formInput', 'placeholder' : 'password'}))

