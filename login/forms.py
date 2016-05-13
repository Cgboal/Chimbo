import hashlib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField


class regForm(forms.Form):
    userName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder' : 'username'}))
    fName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder' : 'first name'}))
    lName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder' : 'last name'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder' : 'email'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder' : 'password'}))
    rePass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'retype password'}))


    def process(self):
        cd = self.cleaned_data
        if cd['password'] == cd['rePass']:
            user = User.objects.create_user(cd['userName'], cd['email'], cd['password'], first_name=cd['fName'], last_name=cd['lName'])
            user.save()
            return True


class loginForm(forms.Form):
    userName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'formInput', 'placeholder' : 'username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class' : 'formInput', 'placeholder' : 'password'}))

