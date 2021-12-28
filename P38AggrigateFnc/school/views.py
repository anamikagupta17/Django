from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from .models import Student
from django.db.models import Avg,Sum,Min,Max,Count

# Create your views here.

def home(req):
    students=Student.objects.all()
    average=students.aggregate(Avg('marks'))
    sum=students.aggregate(Sum('marks'))
    min=students.aggregate(Min('marks'))
    max=students.aggregate(Max('marks'))
    count=students.aggregate(Count('marks'))
    print("Return Data :",students)
    print('--------------------')
    print("Query : ",students.query)
    return render(req,'home.html',{'students':students,'average':average,'min':min,'sum':sum,'max':max,'count':count})
