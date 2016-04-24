import hashlib
from django.shortcuts import render
from django.template.context import RequestContext
from .models import User
# Create your views here.


def index(request):
    return render('index.html', context_instance=RequestContext(request))


def welcome(request):
    return render('welcome.html', context_instance=RequestContext(request))


def login(request):
    return render('login.html', context_instance=RequestContext(request))


def navTest(request):
    return render('navtest.html', context_instance=RequestContext(request))


def signUp(request):
    req = ['username', 'fName', 'lName', 'country', 'email', 'pass', 'rePass']
    for i in req:
        if i not in request.POST:
            return render('signup.html', context_instance=RequestContext(request))
    h = hashlib.md5(request.POST['pass']).hexdigest()
    u = User(userName=request.POST['username'], pHash=h, perms=0, fName=request.POST['fName'],
             lName=request.POST['lName'], country=request.POST['country'], email=request.POST['email'])
    u.save()
    return render(request, 'index.html')