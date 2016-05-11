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
        for i in req:
            if i not in request.POST:
                return render(request, 'signup.html')
            elif request.POST[i] != None:
                return render(request, 'signup.html')
        form = regForm(request.POST)
        if form.process():
            return render(request, 'login.html')
    else:
        context = {'regForm' : regForm}
        return render(request, 'signup.html', context)