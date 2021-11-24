from django import forms

class User(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    agree=forms.BooleanField(label='Agree')
    
    
