from django.shortcuts import render
from .models import ExamCenter,Student

# Create your views here.

def home(req):
    students=Student.objects.all()
    centers=ExamCenter.objects.all()
    return render(req,'home.html',{'students':students,'centers':centers}) 