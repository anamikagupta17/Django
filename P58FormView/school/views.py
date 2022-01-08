from django.shortcuts import render
from .forms import ContactFrom,FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

class ContactFormView(FormView):
    template_name='school/contact.html'
    form_class=ContactFrom  #form name
    initial={'name':'Anamika','email':'anamika@gmail.com'}  # set default or initail data
    success_url='/thankyou/'
    
    
    
    
class FeedbackFormView(FormView):
    template_name='school/feedback.html'
    form_class=FeedbackForm  #form name
    success_url='/thankyou/'   
    def form_valid(self,form):
        print(form) #get whole form
        data=form.cleaned_data  #form data
        print(data)
        return super().form_valid(form)  #we can also write httpResponse('msg')
    
class ThanksTemplateView(TemplateView)  :
     template_name='school/thankyou.html'     
    