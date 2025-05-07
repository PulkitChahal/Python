from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'testApp/base.html')

def home(request):
    return render(request, 'testApp/home.html')
