from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hydjobsinfo(request):
    s = """
    <h1>Job Information</h1>
    <h2>Hyderabad Jobs Information</h2>
    """
    return HttpResponse(s)


def punejobsinfo(request):
    s = """
    <h1>Job Information</h1>
    <h2>Pune Jobs Information</h2>
    """
    return HttpResponse(s)


def mumbaijobsinfo(request):
    s = """
    <h1>Job Information</h1>
    <h2>Mumbai Jobs Information</h2>
    """
    return HttpResponse(s)


def chennaijobsinfo(request):
    s = """
    <h1>Job Information</h1>
    <h2>Chennai Jobs Information</h2>
    """
    return HttpResponse(s)
