from django.shortcuts import render
from . import forms


# Create your views here.
def thankyou_view(request):
    return render(request, 'testApp/thankyou.html')


def feedback_view(request):
    form = forms.FeedbackForm()

    if request.method == 'GET':
        form = forms.FeedbackForm()
        return render(request, 'testApp/feedback.html', {'form': form})

    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and Printing Feedback Info')
            print('Student Name :', form.cleaned_data['name'])
            print('Student Roll No :', form.cleaned_data['roll_no'])
            print('Student Mail Id :', form.cleaned_data['email'])
            print('Student Feedback :', form.cleaned_data['feedback'])

            # return render(request, 'testApp/thankyou.html', {'name': form.cleaned_data['name']})
            # return render(request, 'testApp/thankyou.html')
            return thankyou_view(request)

    return render(request, 'testApp/feedback.html', {'form': form})
