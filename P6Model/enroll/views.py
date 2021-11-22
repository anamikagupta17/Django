from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')


def studentInfo(request):
    stuAll=Student.objects.all()  #fetch all records
    stuSingle=Student.objects.get(pk=2)  # fetch single record
    return render(request,'studentInfo.html',{'stu':stuAll,'stuSg':stuSingle})
