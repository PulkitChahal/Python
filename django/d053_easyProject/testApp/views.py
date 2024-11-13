from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def hello(request):
    s = '<html><body><h1>Hello World of Django</h1></html></body>'
    return HttpResponse(s)


def hello_html(request):
    return render(request, 'testApp/hello.html')


def wish(request):
    date = datetime.datetime.now()
    name = 'Pulkit'
    my_dict = {'date_msg': date, 'name': name}
    return render(request, 'testApp/wish.html', context=my_dict)
