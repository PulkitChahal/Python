from django import forms

class StudentRegisteration(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()