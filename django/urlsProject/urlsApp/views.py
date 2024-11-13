from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsInfo(request):
    s = """
    <h1>Job Information</h1>
    <h2>Hyderabad Jobs Information</h2>
    """
    return HttpResponse(s)

def punejobsInfo(request):
    s = """
    <h1>Job Information</h1>
    <h2>Pune Jobs Information</h2>
    """
    return HttpResponse(s)

def mumbaijobsInfo(request):
    s = """
    <h1>Job Information</h1>
    <h2>Mumbai Jobs Information</h2>
    """
    return HttpResponse(s)

def noidajobsInfo(request):
    s = """
    <h1>Job Information</h1>
    <h2>Noida Jobs Information</h2>
    """
    return HttpResponse(s)