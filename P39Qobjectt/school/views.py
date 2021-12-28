from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from .models import Student
from django.db.models import Q
# Create your views here.

def home(req):
    students=Student.objects.filter(Q(id=6) & Q(roll=106))
    students=Student.objects.filter(Q(id=5) | Q(roll=106))
    students=Student.objects.filter(~Q(id=5))  # negation
    print("Return Data :",students)
    print('--------------------')
    print("Query : ",students.query)
    return render(req,'home.html',{'students':students})
