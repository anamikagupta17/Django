from django.db import models
from django.db.models import fields
from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django import forms
from .forms import StudentForm


# Create your views here.

class StudentCreateView(CreateView):
    model=Student 
    fields=['name','email','password']
    success_url='/thanks/'
    
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass','placeholder':'Please Enter Your name'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'mypass'})
        return form
    
    
# we can do the same thing by creating forms (modelform)  and then give form_class=yourformclass and give templatename in this class only 
class StudentCreateViewForm(CreateView):
    form_class=StudentForm #modelform
    template_name='school/student_form.html'
    success_url='/thanks/'
 
    
    
class ThankYouTemplateView(TemplateView):
    template_name='school/thankyou.html'
    
    

 


