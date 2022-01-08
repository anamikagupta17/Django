from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView
from .models import Student
from django import forms
from .froms import StudentForm

# Create your views here.

class StudentCreateView(CreateView):
    model=Student
    fields=['name','email','password']
    success_url='/thanks/'
    def get_form(self) : # this will not come in update form so need to do it in that form also
        form= super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        return form
    # can do same thing using modelForm
    
class ThanksTemplate(TemplateView)  :
    template_name='school/thankyou.html'  


class StudentUpdateView(UpdateView):
    model=Student
    fields=['name','email','password']
    success_url='/thanksupdate/'
    def get_form(self) : 
        form= super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass'})
        return form
    # can do same thing using modelForm but here need to give model not like create
 
class StudentUpdateViewNew(UpdateView): #for model from  custom from changes
    model=Student
    form_class=StudentForm
    template_name='school/student_form.html'
    success_url='/thanksupdate/'
    
     
class ThanksUpdateTemplate(TemplateView)  :
    template_name='school/thankyouupdate.html'     