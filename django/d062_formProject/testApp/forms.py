from django import forms
from django.core import validators


def starts_with_d(value):
    if value[0] != 'd':
        raise forms.ValidationError('Name Should Starts With d')


def gmail_verification(value):
    if value[len(value) - 9:] != 'gmail.com':
        raise forms.ValidationError('Email Should End With gmail.com')


class FeedbackForm(forms.Form):
    # name = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100, validators=[starts_with_d])
    roll_no = forms.IntegerField()
    # email = forms.EmailField()
    email = forms.EmailField(validators=[gmail_verification])
    # password = forms.CharField(widget=forms.PasswordInput)
    # rpassword = forms.CharField(widget=forms.PasswordInput)
    # feedback = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(widget=forms.Textarea,
                               validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        print('Total Form Validation...')
        cleaned_data = super().clean()
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError('Thanks Bot')

    def clean_name(self):
        input_name = self.cleaned_data['name']
        print('Validating Name')
        if len(input_name) < 4:
            raise forms.ValidationError('Length of Name Field should be >= 4')
        return input_name

    def clean_roll_no(self):
        input_roll_no = self.cleaned_data['roll_no']
        print('Validating Roll Number')
        if input_roll_no < 1 or input_roll_no > 1000:
            raise forms.ValidationError('Roll Number should be between 1 and 1000')
        return input_roll_no

    def clean_email(self):
        input_email = self.cleaned_data['email']
        print('Validating Email')
        if '@gmail.com' not in input_email:
            raise forms.ValidationError('Email should contain @gmail.com')
        return input_email

    def clean_feedback(self):
        input_feedback = self.cleaned_data['feedback']
        print('Validating Feedback')
        if len(input_feedback) > 1000:
            raise forms.ValidationError('Feedback should be less than 1000 characters')
        return input_feedback
