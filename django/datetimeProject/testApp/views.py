from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def datetimeinfo(request):
    date = datetime.now()
    h = int(date.strftime("%H"))
    msg = "<h1>Hello Guest Very "
    if h < 12:
        msg += "Good Morning!!!z"
    elif h < 16:
        msg += "Good Afternoon!!!"
    elif h < 21:
        msg += "Good Evening!!!"
    else:
        msg += "Good Night!!!"

    msg = msg + "</h1><hr>"
    msg = msg + "<h1>Now Server Time is : " + str(date) + "</h1>"

    return HttpResponse(msg)
