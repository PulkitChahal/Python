from django.shortcuts import render


# Create your views here.
def name_view(request):
    return render(request, 'testApp/name.html')


def age_view(request):
    name = request.GET['name']  # reading data from name.html
    response = render(request, 'testApp/age.html')
    response.set_cookie('name', name)  # setting cookie
    return response


def gf_view(request):
    age = request.GET['age']
    response = render(request, 'testApp/gf.html')
    response.set_cookie('age', age)
    return response


def results_view(request):
    gf_name = request.GET['gf_name']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    response = render(request, 'testApp/results.html', {'name': name, 'age': age, 'gf_name': gf_name})
    return response
