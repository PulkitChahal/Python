from django.shortcuts import render
from testApp.models import *

# Create your views here.
def index(request):
    return render(request, 'testApp/index.html')

def hydjobs(request):
    jobs_list = hydjobs.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testApp/hydjobs.html', context=my_dict)

def blorejobs(request):
    jobs_list = blorejobs.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testApp/blorejobs.html', context=my_dict)

def punejobs(request):
    jobs_list = punejobs.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testApp/punejobs.html', context=my_dict)

def noidajobs(request):
    jobs_list = noidajobs.objects.order_by('date')
    my_dict = {'jobs_list': jobs_list}
    return render(request, 'testApp/noidajobs.html', context=my_dict)
