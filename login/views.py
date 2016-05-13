from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import regForm, loginForm


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def signUp(request):
    if request.method == 'POST':
        form = regForm(request.POST)
        if form.is_valid():
            if form.process():
                return redirect('/login/')
    context = {'regForm' : regForm}
    return render(request, 'signup.html', context)


def loginView(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['userName'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
    context = {'loginForm' : loginForm}
    return render(request, 'login.html', context)

