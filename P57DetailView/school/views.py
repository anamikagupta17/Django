from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.


class StudentDetailView(DetailView):
    model=Student # context key for data will be model name in small
    
    
class StudentDetailViewCustom(DetailView) :
    model=Student
    template_name='school/student.html' 
    context_object_name='stu'  
    pk_url_kwarg='ana' # change pk name to ana  but it will work on primary key of table
    
    
class StudentListView(ListView)  :
      model=Student
      template_name='school/list.html' 
      context_object_name='students'
      
class StudentDetailMethods(DetailView):
    model=Student
    template_name='school/detail.html' 
    context_object_name='stu'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_students"] = self.model.objects.all().order_by('name')
        return context
        