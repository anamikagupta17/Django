from django.shortcuts import render
from .models import Student,Teacher,Construction

# Create your views here.

def home(req):
    students=Student.objects.all()
    teachers=Teacher.objects.all()
    contractors=Construction.objects.all()
    context={'students':students,'teachers':teachers,'contractors':contractors}
    return render(req,'home.html',context)