from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView
# Create your views here.

class StudentListView(ListView):
    model=Student  # this will return all data data will be in student_list
    tempalate_name_suffix='_list' # tempate name  by default it is modal_list we can change it anything in place of list
    ordering=['name']

class StudentListViewCustom(ListView):
    model=Student
    template_name='school/students.html'
    
    
class StudentListViewCustomObject(ListView): 
    model=Student
    template_name='school/list.html'
    context_object_name='students'    #by default it will be modelclassname_list eg : student_list
    
    
class StudentFilterListView(ListView):
    model=Student
    template_name='school/list.html'
    context_object_name='students'
    
    def get_queryset(self):
        return Student.objects.filter(course='Python')
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['fresher']=Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self): #dynamic template based on cookie
        if self.request.COOKIES['user']=='anamika':
            template_name='school/anamika.html'
        else:
            template_name='school/list.html'
            
        return [template_name]        
            
     
        