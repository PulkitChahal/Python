from django.shortcuts import render
from django.http import HttpResponse
from .import forms
from django.contrib import messages

# Create your views here.
def v1(request):
    return HttpResponse('<h1>This is my View 1</h1>')

def v2(request):
    return HttpResponse('<h1>This is my View 2</h1>')

def date_time(request):
    import datetime
    time = datetime.datetime.now()
    t = '<h1>Current Date and Time is:'+str(time) + '</h1>'
    return HttpResponse(t)

def home(request):
    sum = 10 + 20
    return render(request, 'home.html', context={'name':'Pulkit', 'result':sum})

def home(request):
    return render(request, 'home.html')

def add(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
    sum = a + b
    return render(request, 'result.html', context={'result':sum})

def index(request):
    return render(request, 'index.html')


def emp_details(request):
    eid =1234
    ename='pulkit'
    eaddress='hyderabad'
    designation='MANAGER'
    salary=70000
    age=25

    details={'eid':eid, 'ename':ename, 'eaddress': eaddress, 'designation':designation, 'salary':salary, 'age':age}
    return render(request, 'emp.html', context=details)


def date_time(request):
    import datetime
    time = datetime.datetime.now()
    return render(request, 'index.html', context={'dt':time})


def v3(request):
    return render(request, 'index2.html', {'name':'Pulkit', 'age':'25'})


def v3(request):
    names = {'value':['pulkit', 'sai', 'sri', ]}
    return render(request, 'index2.html', names)


def student(request):
    if request.method == 'POST':
        fm = forms.StudentForm(request.POST)
        if fm.is_valid():
            print('Form is Validated')
            print('Name:', fm.cleaned_data['name'])
            print('Mail:', fm.cleaned_data['mailid'])
            print('Marks:', fm.cleaned_data['marks'])
            print('Address:', fm.cleaned_data['address'])
            print('Password:', fm.cleaned_data['password'])
            messages.add_message(request, messages.SUCCESS, 'Data Inserted Successfully')
    else:
        fm = forms.StudentForm()
        fm.order_fields(field_order=['name', 'mailid', 'marks', 'address', 'password'])
    return render(request, 'form.html', {'form':fm})