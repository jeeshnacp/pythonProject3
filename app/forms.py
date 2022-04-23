import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from app.models import Login, nurse, hospital


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is not valid number')



class loginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)

class nurseregister(forms.ModelForm):
    Contact_no=forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = nurse
        fields = ('Nurse_Name', 'Contact_no', 'Address', 'Email','Hospital_name')

class hospitalform(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model= hospital
        fields=('Hospital_Name','place','contact_no','email')
