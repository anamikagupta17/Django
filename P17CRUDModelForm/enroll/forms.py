from django import forms
from django.forms import widgets
from .models import User
class Student(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True), #by default render_value is False
        }
        
    