from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Home Page")

def learnDjango(request):   # request is the request object 
    return HttpResponse('<h1>Hello Anamika this is first function of Django</h1>')

def otherFunction(request):
    a="""<h2> 
    Hi <br>
    this is second function of Django<br>
    thank You<br>
    Anamika Gupta
    <h2>"""
    return HttpResponse(a)

def learnMath(request):
    b=20+40
    return HttpResponse(f'Calculation  a= {b} ')  # formatting
    
    
