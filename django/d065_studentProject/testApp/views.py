from django.shortcuts import render
from testApp import forms


# Create your views here.
def student_view(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Form Data Inserted Into Database Successfully...')
            return render(request, 'testApp/thankyou.html', {'name': form.cleaned_data['name']})
    return render(request, 'testApp/register.html', {'form': form})
