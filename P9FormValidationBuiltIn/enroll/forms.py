from django import forms
from django.core import validators
class StudentRegistration(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(4)]) 
    email=forms.EmailField()  
    password=forms.CharField(widget=forms.PasswordInput,required=True) 
    