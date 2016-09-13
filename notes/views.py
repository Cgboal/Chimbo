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
    return render(request, 'courses.html', context={"Courses": c})


@login_required()
def courseView(request):
    if request.method != 'GET':
        return courseList(request)
    c = request.GET.get('c', '')
    if not c:
        return courseList(request)
    try:
        modules = models.Module.objects.filter(course=c)
        years = models.Course.objects.get(name=c)
        notes = models.Note.objects.filter(module__in=modules)
        return render(request, 'modules.html',
                      context={"Modules": modules, "Years": range(years.years), "Notes": notes})
    except Exception, e:
        return courseList(request)


@login_required()
def noteView(request):
    if request.method != "GET":
        return courseList()
    pKey = request.GET.get('id', '')
    mKey = request.GET.get('c', '')
    if not pKey:
        return courseList(request)

    note = models.Note.objects.get(id=pKey)
    module = models.Module.objects.get(title=mKey)
    chapters = models.Note.get(module__in=module)
    return render(request, 'notes.html', context={"Note" : note, "Module" : module, "Chapters" : chapters})
