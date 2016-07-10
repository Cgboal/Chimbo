from django.shortcuts import render
import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def dashboard(request):
    return render(request, 'base.html')

@login_required()
def courseList(request):
    c = models.Course.objects.all()
    return render(request, 'courses.html', context={"Courses" : c})

@login_required()
def courseView(request):
    if request.method != 'GET':
         return courseList(request)
    c = request.GET.get('c', '')
    if not c:
        courseList(request)
    try:
        modules = models.Module.objects.filter(course=c)
        years = models.Course.objects.get(name=c)
        notes = models.Note.objects.filter(module__in=modules)
        return render(request, 'modules.html', context={"Modules" : modules, "Years" : range(years.years), "Notes" : notes})
    except Exception, e:
        return courseList()