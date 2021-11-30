from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
   # email=forms.CharField(max_length=50) # we can use form validatores also this will be high precedence
    class Meta:
        model=Student
        fields=['name','password','email']
        labels={'name':'Enter Name','email':'Enter Email'}
        error_messages={'email':{'required':'Email is must'},'password':{'max_length':12}}
        widgets={'password':forms.PasswordInput,
                 'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Your Name '}),
                 'email':forms.EmailInput
        }
                
    
    