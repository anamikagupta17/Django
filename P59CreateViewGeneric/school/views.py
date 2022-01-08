from django.db import models
from django.db.models import fields
from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

# Create your views here.

class StudentCreateView(CreateView):
    #can create custom template also
    model=Student 
    fields=['name','email','password']
    # success_url='/thanks/' # we  can set absoulute url in model
    
     #get form from model and above fields and save data on submit
     
     
class ThankYouTemplateView(TemplateView):
    template_name='school/thankyou.html'
    
    
class StudentDetailView(DetailView):
    model=Student
        
 


