from django import forms
from django.forms.widgets import HiddenInput


class Login(forms.Form):
     username=forms.CharField(label='Your UserName',label_suffix=' @ ',initial='Anamika')
     password=forms.CharField(widget=forms.PasswordInput ,help_text='Limit 12',initial='Password')
     mobile=forms.CharField(widget=forms.NumberInput)
     security_text=forms.CharField(initial='goodvibes',disabled=True)
     key=forms.CharField(widget=HiddenInput)
     feedback=forms.CharField(widget=forms.Textarea(attrs={'class':'cls1 cls2'}))