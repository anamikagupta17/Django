from django import forms
class StudentRegistration(forms.Form):
    error_css_class='error'  # this will add only when error occur
    required_css_class='required'  # this will add only when required 
    name=forms.CharField(error_messages={'required':'Enter your Name'}) 
    email=forms.EmailField(error_messages={'required':'Enter your Email'},min_length=5,max_length=15)
    password=forms.EmailField(widget=forms.PasswordInput , min_length=7,error_messages={'required':'Enter your Password'})  
    
    
    
    