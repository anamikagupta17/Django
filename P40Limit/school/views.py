
from django.shortcuts import render
from .models import Student
from django.db.models import Q
# Create your views here.

def home(req):
    students=Student.objects.all()
    # students=Student.objects.all()[:5] #first 5
    # students=Student.objects.all()[2:6] #3 to 6
    # students=Student.objects.all()[:6:2] #setp 2
    
   
    print("Return Data :",students)
    print('--------------------')
    print("Query : ",students.query)
    return render(req,'home.html',{'students':students})
