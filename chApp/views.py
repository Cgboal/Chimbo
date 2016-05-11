import hashlib
from django.shortcuts import render
from django.template.context import RequestContext
from .models import User
from .forms import regForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')


def login(request):
    return render(request, 'login.html')


def navTest(request):
    return render(request, 'navtest.html')


def signUp(request):
    if request.method == 'POST':
        req = ['userName', 'fName', 'lName', 'country', 'email', 'password', 'rePass']
        form = regForm(request.POST)
        if form.is_valid():
            if form.process():
                render(request, 'login.html')


    context = {'regForm' : regForm}
    return render(request, 'signup.html', context)