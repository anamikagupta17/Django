from django.shortcuts import render
from .models import Student

# Create your views here.
def home(req):
    #students=Student.objects.all() #objects is a manager by default this will not work after change manager name
    students=Student.mymanager.all() # change manager name  
    return render(req,'home.html',{'students':students})
