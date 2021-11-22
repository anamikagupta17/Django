from django import forms


class Login(forms.Form):
     username=forms.CharField(help_text='this is help text we can show some errro',initial='Anamika')
     password=forms.CharField()