from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def welcome(request):
    return render(request, 'welcome.html')


def login(request):
    return render(request, 'login.html')


def navTest(request):
    return render(request, 'navtest.html')

