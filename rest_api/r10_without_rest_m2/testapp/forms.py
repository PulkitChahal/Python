from django import forms
from testapp.models import Student


class StudentForm(forms.ModelForm):
    def clean_marks(self):
        input_marks = self.cleaned_data['marks']
        if input_marks < 35:
            raise forms.ValidationError('Marks should be greater than 35')
        return input_marks

    def clean_rollno(self):
        input_rollno = self.cleaned_data['rollno']
        if input_rollno > 9999:
            raise forms.ValidationError('Roll number should be less than 9999')
        return input_rollno

    class Meta:
        model = Student
        fields = '__all__'
