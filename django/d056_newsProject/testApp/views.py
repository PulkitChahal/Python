from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'testApp/index.html')


def moviesinfo(request):
    head_msg = 'Latest Movies Information'
    msg1 = 'Sonali slowly getting cured'
    msg2 = 'Salman going to jail'
    msg3 = 'Enjoying'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'testApp/news.html', context=my_dict)


def sportsinfo(request):
    head_msg = 'Latest Sports Information'
    msg1 = 'Kohli in form'
    msg2 = 'RCB Won'
    msg3 = 'World Cup start'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'testApp/news.html', context=my_dict)


def politicsinfo(request):
    head_msg = 'Latest Politics Information'
    msg1 = 'BJP Won'
    msg2 = 'Haryana Election'
    msg3 = 'BJP in Power'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return render(request, 'testApp/news.html', context=my_dict)
