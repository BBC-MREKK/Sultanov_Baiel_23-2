from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello! its my first project</h1>')

def now_date(request):
    return HttpResponse('<h2>13.12.2022</h2>')

def goodby(request):
    return HttpResponse('<h3>Goodbye user!</h3>')
