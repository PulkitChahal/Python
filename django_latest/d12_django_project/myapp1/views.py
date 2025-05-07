from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def v3(request):
    return HttpResponse('<h1>This is my View 3</h1>')

def v4(request):
    return HttpResponse('<h1>This is my View 4</h1>')