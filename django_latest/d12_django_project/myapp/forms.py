from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name should start with Z')


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, initial='Pulkit', label_suffix=' ', required=False, disabled=True, validators=[check_for_z, validators.MinLengthValidator(5)])
    marks = forms.IntegerField()
    mailid=forms.EmailField()
    address=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200, widget=forms.PasswordInput)
    retypepassword=forms.CharField(max_length=200, widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        pwd = self.cleaned_data['password']
        rpwd = self.cleaned_data['retypepassword']
        if pwd != rpwd:
            raise forms.ValidationError('Password and Confirm Password should be same')