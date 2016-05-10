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
        req = ['username', 'fName', 'lName', 'country', 'email', 'pass', 'rePass']
        for i in req:
            if i not in request.POST:
                return render(request, 'signup.html')
            elif request.POST[i] != None:
                return render(request, 'signup.html')
        h = hashlib.md5(request.POST['pass']).hexdigest()
        u = User(userName=request.POST['username'], pHash=h, perms=0, fName=request.POST['fName'],
                 lName=request.POST['lName'], country=request.POST['country'], email=request.POST['email'])
        u.save()
        return render(request, 'login.html')
    else:
        context = {'regForm' : regForm}
        return render(request, 'index.html', context)