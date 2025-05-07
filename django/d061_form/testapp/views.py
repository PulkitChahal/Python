from django.shortcuts import render
from . import forms


# Create your views here.
def student_register_views(request):
    form = forms.StudentRegisteration()
    my_dict = {'form': form}
    return render(request, 'testapp/register.html', context=my_dict)
