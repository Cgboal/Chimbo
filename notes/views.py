from django.shortcuts import render
import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def dashboard(request):
    return render(request, 'base.html')

@login_required()
def courses(request):
    c = models.Course.objects.all()
    return render(request, 'courses.html', context={"Courses" : c})
