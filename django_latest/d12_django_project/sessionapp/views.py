from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setsession(request):
    request.session['MySession'] = 'John Doe'
    return render(request, 'set.html')


def getsession(request):
    name = request.session.get('MySession', default='No Name')
    return render(request, 'get.html', {'name': name})


def delsession(request):
    if 'MySession' in request.session:
        del request.session['MySession']
    return render(request, 'del.html')