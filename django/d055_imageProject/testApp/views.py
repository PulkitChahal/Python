from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'testApp/demo.html')

def profile(request):
    return render(request, 'testApp/profile.html')