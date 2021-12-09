from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms 
class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']  # we are not adding password fields because that is part of UserCreationForm that wil come automatically but we can validate separatly
        labels={'email':'Email'}
        
        
class EditUserProfileForm(UserChangeForm)  :
    password=None     
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login'] 
        labels={'email':'Email','first_name':'First Name','date_joined':'Joining Date'}
        
class EditAdminProfileForm(UserChangeForm)  :
    password=None     
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email','first_name':'First Name','date_joined':'Joining Date'}        