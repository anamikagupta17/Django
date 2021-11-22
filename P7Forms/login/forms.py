from django import forms
from django.forms.widgets import HiddenInput


class Login(forms.Form):
     username=forms.CharField(help_text='this is help text we can show some errro',initial='Anamika')
     password=forms.CharField()
     mobile=forms.NumberInput()
     security_text=forms.CharField()
     key=forms.CharField(widget=HiddenInput())