from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    s = """
    <h1>Hello Welcome to Django Classes... Django is Nursery Level Concept!</h1>
    <h2>Welcome back</h2>
    <h3>Welcome back</h3>
    <h4>Welcome back</h4>
    <h5>Welcome back</h5>
    """
    return HttpResponse(s)
