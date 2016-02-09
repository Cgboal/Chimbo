from django.shortcuts import render_to_response
from django.template.context import RequestContext
# Create your views here.


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def welcome(request):
    return render_to_response('welcome.html', context_instance=RequestContext(request))


def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))


def navTest(request):
    return render_to_response('navtest.html', context_instance=RequestContext(request))