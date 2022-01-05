from django import forms
from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.

def homefunc(req):
    return render(req,'home.html')

def aboutfun(req):
    context={'msg':'Welcome to Anamika Gupta Web Development: Function Based View'}
    return render(req,'about.html',context)


class HomeClassView(View):
    def get(self,req):
        return render(req,'home.html')
    
    
class AboutClassView(View):
    def get(self,req):
        context={'msg':'Welcome to Anamika Gupta Web Development: Class Based View'}
        return render(req,'about.html',context)
    
    
def contactfun(req):
    if req.method == 'POST' :
        form=ContactForm(req.POST)   
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse ('Thank You form Submmited!')
    else:
        form=ContactForm()
        return render(req,'contact.html',{'form':form})    
    
    
class ContactClassView(View):
    def get(self,req):
        form=ContactForm()
        return render(req,'contact.html',{'form':form})
    
    def post(self,req):
        form=ContactForm(req.POST)   
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse ('Thank You form Submmited!')
        
        
        
def newsfun(req,template_name):
    context={'info':'CBI enquiry !!!'}     
    return render(req,template_name,context)   


class NewsClassView(View):
    template_name=''
    def get(self,req):
        context={'info':'CBI enquiry !!!'}     
        return render(req,self.template_name,context)  
            