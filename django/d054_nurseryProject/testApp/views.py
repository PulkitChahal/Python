from django.shortcuts import render
import datetime


# Create your views here.
def dateinfo(request):
    date = datetime.datetime.now()
    print(date)
    name = 'Pulkit'
    h = int(date.strftime('%H'))
    if h < 12:
        msg = 'Good Morning!!!'
    elif h < 16:
        msg = 'Good Afternoon!!!'
    elif h < 22:
        msg = 'Good Evening!!!'
    else:
        msg = 'Good Night!!!'
    my_dict = {'msg': msg, 'name': name, 'date': date}
    return render(request, 'testApp/test.html', my_dict)
