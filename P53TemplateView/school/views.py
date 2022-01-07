from django.shortcuts import render
from django.views.generic.base  import TemplateView

# Create your views here.

# class HomeTemplateView(TemplateView):
#     template_name='home.html'



#child class of TempalteView
class HomeTemplateView(TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['name']='Anamika'
        context['roll']=101
        
        # context={'name':'Anamika','roll':101}# can write like this also but extra context will not work in this
        print(context)
        print(kwargs) #parameter of url
        return context
        


