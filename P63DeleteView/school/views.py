from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Student


# Create your views here.

class StudentCreateView(CreateView):
    model=Student
    fields=['name','email','password']
    success_url='/thanks/'
       
class ThanksTemplate(TemplateView)  :
    template_name='school/thankyou.html'  



class StudentUpdateView(UpdateView):
    model=Student
    fields=['name','email','password']
    success_url='/thanksupdate/'
         
class ThanksUpdateTemplate(TemplateView)  :
    template_name='school/thankyouupdate.html'     
    
    
class StudentDeleteView(DeleteView):
    model=Student
    success_url='/'   
     
    # we can give custom template name for delete confirmation
    #template_name='school/delete_confirm.html'
    
    