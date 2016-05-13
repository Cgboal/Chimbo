from django.shortcuts import render, redirect
from .forms import regForm

# Create your views here.


def signUp(request):
    if request.method == 'POST':
        form = regForm(request.POST)
        if form.is_valid():
            if form.process():
                return redirect('/login/')


    context = {'regForm' : regForm}
    return render(request, 'signup.html', context)