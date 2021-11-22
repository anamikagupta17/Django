from django.shortcuts import render

def course(request):
    return render(request,'course.html',{'d':'dot Net'})

# Create your views here.
