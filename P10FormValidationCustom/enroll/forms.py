from django import forms
from django.core import validators

def starts_with_a(value):
    if value[0]!= 'a':
        raise forms.ValidationError('Name shoud starts with a')
class StudentRegistration(forms.Form):
    name=forms.CharField(validators=[starts_with_a]) 
    email=forms.EmailField()  
    