from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

from  .forms import Student
from .models import User
# Create your views here.

#using TemplateView 
class Home(TemplateView):
    template_name='addShow.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        fm=Student() 
        stu=User.objects.all()
        context={'fm':fm,'stu':stu}
        return context
    
    def post(self,req):
        fm=Student(req.POST)
        if fm.is_valid():
            data=fm.cleaned_data
            reg=User(name=data['name'],email=data['email'],password=data['password'])
            reg.save() 
            return HttpResponseRedirect('/')

#using RedirectView 
class DeleteData(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        id=kwargs['id']
        User.objects.get(pk=id).delete()
        return super().get_redirect_url(*args, **kwargs)
    
 
#using View 
class EditData(View):
    def get(self, req,id):
        pi=User.objects.get(pk=id)
        fm=Student(instance=pi)  
        return render(req,'update.html',{'fm':fm})
    
    def post(self,req,id):
        pi=User.objects.get(pk=id)
        fm=Student(req.POST,instance=pi) 
        if fm.is_valid():
           fm.save()   
        return HttpResponseRedirect('/')
       
    
 